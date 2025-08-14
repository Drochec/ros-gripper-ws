import rclpy
from rclpy.node import Node

import std_msgs.msg

from ads1015 import ADS1015
import smbus2

from rclpy.action import ActionClient
from action_interface.action import GripperMove

#Parametry pro převod
ADC_RANGE = 6.144

ANGLE_CHANNEL = "in0/gnd"
CURRENT_CHANNEL = "in2/gnd"

I2C_BUS = smbus2.SMBus(5)

ads1115 = ADS1015(i2c_dev=I2C_BUS)
ads1115.set_mode("single")
ads1115.set_programmable_gain(ADC_RANGE)

#Proudove cidlo

SENSITIVITY = 0.185
SAMPLES = 100

#current_offset = 0.347
current_offset = ADC_RANGE/2

#Uhel okrajove hodnoty
angle_Vmin = 0.23
angle_Vmax = 2.98

CLOSED_POS = 0
OPEN_POS = 170

class adcNode(Node):

    #current = 0
    #current_offset = 0
    #angle = 0

    def __init__(self,current_sens_sensitivity, current_calibration_samples, angle_Vmin, angle_Vmax):
        super().__init__("adc_readout")

        self.get_logger().info("Node started")

        self.sensitivity = current_sens_sensitivity
        self.samples = current_calibration_samples
        self.angle_Vmin = angle_Vmin
        self.angle_Vmax = angle_Vmax

        self.calibrate_current_sens()

        self.timer = self.create_timer(0.05, self.publish_readings)
        self.current_readout_publisher = self.create_publisher(std_msgs.msg.Float32, "adc_current_raw", 10)
        self.angle_readout_publisher = self.create_publisher(std_msgs.msg.Int32, "adc_angle_raw", 10)
        
        self.gripper_action_client = ActionClient(self, GripperMove, "gripper_move")

    def read_values(self):
        current_raw = ads1115.get_voltage(CURRENT_CHANNEL)
        self.current = (current_raw - self.current_offset) / self.sensitivity

        angle_raw = ads1115.get_voltage(ANGLE_CHANNEL)
        self.angle = (angle_raw - self.angle_Vmin) * 180 / (self.angle_Vmax - self.angle_Vmin)

        #self.get_logger().info(str(current_raw))
        #self.get_logger().info(str(self.current_offset))
        #self.get_logger().info(str(self.sensitivity))

        

    def calibrate_current_sens(self):
        sum_current_raw = 0.0
        for i in range(self.samples):
            sum_current_raw += ads1115.get_voltage(CURRENT_CHANNEL)
        self.current_offset = sum_current_raw / self.samples
        self.get_logger().info("Current calbritated - offset: {} A".format(self.current_offset))

    def calibrate_angle_sens(self):
        action_msg = GripperMove.Goal()
        action_msg.action = 0

        self.gripper_action_client.send_goal(action_msg)

        self.gripper_action_client.wait_for_server()

        sum_angle_raw = 0
        for i in range(self.samples):
            sum_angle_raw += ads1115.get_voltage(ANGLE_CHANNEL)
        self.angle_Vmin = int(sum_angle_raw / self.samples)

        action_msg.action = 180
        self.gripper_action_client.send_goal(action_msg)

        self.gripper_action_client.wait_for_server()

        sum_angle_raw = 0
        for i in range(self.samples):
            sum_angle_raw += ads1115.get_voltage(ANGLE_CHANNEL)
        self.angle_Vmax = int(sum_angle_raw / self.samples)


    def publish_readings(self):
        self.read_values()

        self.publish_current()
        self.publish_angle()

        #self.get_logger().info("Publishing values - Angle: {} | Current: {} A".format(self.angle, self.current))

    def publish_current(self):
        msg = std_msgs.msg.Float32()
        msg.data = float(self.current)

        self.current_readout_publisher.publish(msg)


    def publish_angle(self):
        msg = std_msgs.msg.Int32()
        msg.data = int(self.angle)

        self.angle_readout_publisher.publish(msg)
        


def main(args=None):

    rclpy.init(args=args)
    node = adcNode(current_sens_sensitivity=SENSITIVITY, current_calibration_samples=SAMPLES, angle_Vmin=angle_Vmin, angle_Vmax=angle_Vmax)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()