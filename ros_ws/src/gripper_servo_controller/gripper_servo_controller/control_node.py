#!/usr/bin/env python3 

import rclpy
import rclpy.node
import rclpy.action
import std_msgs.msg
from action_interface.action import GripperMove

import piservo

#Parametry serva
SERVO_SIGNAL_PIN = 13 #pin musi podporovat HW PWM - viz RasPi pinout (pinout.xyz)
SERVO_MIN_POS = 0 #mozna bude stacit nastavit meze tady
SERVO_MAX_POS = 180 
SERVO_MIN_PULSE = 0.5 #Z datasheetu vyrobce
SERVO_MAX_PULSE = 2.5
SERVO_FREQUENCY = 50

servo = piservo.Servo(SERVO_SIGNAL_PIN, SERVO_MIN_POS, SERVO_MAX_POS, SERVO_MIN_PULSE, SERVO_MAX_PULSE, SERVO_FREQUENCY)

#Specialni pripady prijate pozice
CLOSED = -1
OPEN = -2

#Horni a spodni limit pozice pro otevreni/zavreni gripperu
#Nechceme rozervat nastavec.... znova

OPEN_ANGLE = 100
CLOSED_ANGLE = 10

#Ridici Node pro ovladani gripperu
#Topicy:
# - subscriber: cmd_pos - nastaveni pozice manualne
# - listnener: act_pos - aktualni pozice gripperu

#Action - GripperMove

#Actions - Move - open/close

class controlNode(rclpy.node.Node):


    def __init__(self):

        super().__init__("control_node")
        
        #Nastaveni hodnot ochrany nadproudu
        self.overcurrent_start = None
        self.overload_active = False
        self.overcurrent_threshold = 0.75   # amps
        self.overcurrent_duration = 0.1    # seconds


        #self.samples = 100 #Pocet vzorku, pouzite pri kalibraci

        #Parametry proudoveho cidla 
        #self.current = 0.0 #Aktualni prijata hodnota z ADC nody
        #self.current_offset = 2.3 #Vychozi hodnota, presnejsi ziskana kalibraci
        #self.current_sensitivity = 0.185 #Z datasheetu vyrobce [V/A]
        
        #self.set_angle = 0 #Nastaveny uhel - posila na signal pin serva
        #self.servo_angle = 0.0 #Aktualni uhel - ziskany z ADC nody
        #self.stop_angle_offset = 0 #Offset pri pocitani finalni polohy serva po zastaveni kvuli prepeti


        self.timer = self.create_timer(1.0, self.publish_pos) #Kazdou sekundu posle nastavenou pozici
        self.cmd_pos_pub = self.create_publisher(std_msgs.msg.Int32, "cur_pos", 5) 
        self.cmd_pos_sub = self.create_subscription(std_msgs.msg.Int32, "cmd_pos", self.receive_pos, 5) #Pri poslani dat na topic posune na zadanou pozici

        #Hodnoty z ADC
        self.angle_sub = self.create_subscription(std_msgs.msg.Int32, "adc_angle", self.store_angle, 10)
        self.current_sub = self.create_subscription(std_msgs.msg.Float32, "adc_current", self.gripper_watchdog, 10)


        #self.adc_sub = self.create_subscription(std_msgs.msg.Float32MultiArray, "adc_data", self.read_sens, 10)

        self.action_server = rclpy.action.ActionServer(self, GripperMove, 'gripper_move', self.gripper_move_action)

        self.get_logger().info("Control node started")
        self.move_servo(CLOSED_ANGLE) #Nastavi vychozi hodnotu serva

    def publish_pos(self):
        msg = std_msgs.msg.Int32()
        msg.data = self.set_angle
        
        self.cmd_pos_pub.publish(msg)
    
    def receive_pos(self, angle: std_msgs.msg.Int32): 
        #Nastaveni pozice pomoci zpravy na topic

        self.get_logger().info("Received pos: " + str(angle.data))
        self.reset_overload() #Novy pohyb == reset kontroly nadproudu
        self.set_angle = angle.data
        self.move_servo(angle.data)

    def move_servo(self, angle):
        self.get_logger().info('Moving gripper....')
        
        #Kontrola prekroceni krajnich hodnot
        if angle > OPEN_ANGLE:
            angle = OPEN_ANGLE
        elif angle < CLOSED_ANGLE:
            angle = CLOSED_ANGLE

        self.set_angle = angle
        servo.write(angle)
        self.get_logger().info('Set desired servo angle to: {}....'.format(angle))

        return True

    def gripper_move_action(self, goal):
        
        
        received_angle = goal.request.action

        #Specialni pripady => -1 zavrit, -2 otevrit

        if (received_angle == CLOSED):
            received_angle = CLOSED_ANGLE
            self.get_logger().info(str(received_angle))
        elif (received_angle == OPEN):
            received_angle = OPEN_ANGLE
            self.get_logger().info(str(received_angle))

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
                    self.move_servo(self.servo_angle + self.stop_angle_offset)
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

    #def read_sens(self, raw_data: std_msgs.msg.Float32MultiArray):
    #    current_raw = raw_data.data[0]
    #    angle_raw = raw_data.data[1]
    #    
    #    self.current = (current_raw - self.current_offset) / self.current_sensitivity
    #    self.servo_angle = int((angle_raw - self.angle_Vmin) * 180 / (self.angle_Vmax - self.angle_Vmin))

    #def calibrate_sens(self):
    #    self.get_logger().info('Calibrating sensors')
#
#        sum_current_raw = 0.0
    #    for i in range(self.samples):
            
    #    self.current_offset = sum_current_raw / self.samples
        

def main(args=None):
    rclpy.init(args=args)
    node = controlNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()