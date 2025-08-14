#!/usr/bin/env python3 

import rclpy
import rclpy.node
import rclpy.action
import std_msgs.msg
from action_interface.action import GripperMove

import piservo

from enum import Enum

#Parametry serva
servo_signal_pin = 13 #pin musi podporovat HW PWM - viz RasPi pinout (pinout.xyz)
servo_min_pos = 0 #mozna bude stacit nastavit meze tady
servo_max_pos = 180 
servo_min_pulse = 0.5 #Z datasheetu vyrobce
servo_max_pulse = 2.5
servo_frequency = 50

servo = piservo.Servo(servo_signal_pin, servo_min_pos, servo_max_pos, servo_min_pulse, servo_max_pulse, servo_frequency)


class ServoPos(Enum):
    CLOSED = -1
    OPEN = -2



#Ridici Node pro ovladani gripperu
#Topicy:
# - subscriber: cmd_pos - nastaveni pozice manualne
# - listnener: act_pos - aktualni pozice gripperu

#Actions - Move - open/close

class controlNode(rclpy.node.Node):
    


    def __init__(self,lower_angle_limit,upper_angle_limit):


        super().__init__("control_node")
        
        #Horni a spodni limit pozice pro otevreni/zavreni gripperu
        #Nechceme rozervat nastavec.... znova
        self.lower_angle_limit = lower_angle_limit
        self.upper_angle_limit = upper_angle_limit

        self.open_angle = 170
        self.close_angle = 0

        self.overcurrent_start = None
        self.overload_active = False
        self.overcurrent_threshold = 0.5   # amps
        self.overcurrent_duration = 0.1    # seconds
        self.stop_angle_offset = 0         # example

        self.servo_angle = 0
        self.stop_angle_offset = 1
        self.stop_current = 0.4


        self.timer = self.create_timer(1.0, self.publish_pos) #Kazdou sekundu posle nastavenou pozici
        self.cmd_pos_pub = self.create_publisher(std_msgs.msg.Int32, "cur_pos", 10)
        self.cmd_pos_sub = self.create_subscription(std_msgs.msg.Int32, "cmd_pos", self.receive_pos, 10) #Pri poslani dat na topic posune na zadanou pozici

        self.current_sub = self.create_subscription(std_msgs.msg.Float32, "adc_current", self.gripper_watchdog, 10)
        self.angle_sub = self.create_subscription(std_msgs.msg.Int32, "adc_angle", self.store_angle, 10)

        self.action_server = rclpy.action.ActionServer(self, GripperMove, 'gripper_move', self.gripper_move_action)

        self.get_logger().info("Control node started")
        self.move_servo(self.close_angle)
        self.get_logger().info("Default position set")

    def publish_pos(self):
        msg = std_msgs.msg.Int32()
        msg.data = self.angle
        
        self.cmd_pos_pub.publish(msg)
    
    def receive_pos(self, pos: std_msgs.msg.Int32):
        self.get_logger().info("Received pos: " + str(pos.data))
        self.reset_overload()
        self.angle = pos.data
        servo.write(pos.data)

    def move_servo(self, angle):
        self.get_logger().info('Moving gripper....')
        
        if angle > self.upper_angle_limit:
            angle = 180
        elif angle < self.lower_angle_limit:
            angle = 0

        self.angle = angle
        servo.write(angle)
        self.get_logger().info('Set desired servo angle to: {}....'.format(angle))

        return True

    def gripper_move_action(self, goal):
        
        
        received_angle = goal.request.action

        #Specialni pripady => -1 zavrit, -2 otevrit

        if (received_angle == ServoPos.CLOSED):
            received_angle = self.close_angle
            print(received_angle)
        elif (received_angle == ServoPos.OPEN):
            received_angle = self.open_angle
            print(received_angle)

        self.reset_overload()

        self.move_servo(received_angle)

        goal.succeed()
        result = GripperMove.Result()
        result.complete = True
        return result

    def gripper_watchdog(self, current_msg):
        now = self.get_clock().now()

        if not self.overload_active:
            if current_msg.data >= self.overcurrent_threshold:
                if self.overcurrent_start is None:
                    self.overcurrent_start = now
                elif (now - self.overcurrent_start).nanoseconds * 1e-9 >= self.overcurrent_duration:
                    self.get_logger().warn(
                        f'Prolonged overload ({current_msg.data:.3f} A)! Stopping'
                    )
                    self.move_servo(self.servo_angle - self.stop_angle_offset)
                    self.overload_active = True  # latch so it won’t trigger again
            else:
                self.overcurrent_start = None
        else:
            # Already in overload, ignore readings until reset
            pass

    def reset_overload(self):
        self.overload_active = False
        self.overcurrent_start = None

    def store_angle(self, angle_msg):
        self.servo_angle = angle_msg.data

def main(args=None):
    rclpy.init(args=args)
    node = controlNode(lower_angle_limit=0,upper_angle_limit=180)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()