import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from action_interface.action import GripperMove

import std_msgs.msg

from ads1015 import ADS1015
import smbus2

import time

#Parametry pro převod
ADC_RANGE = 6.144

ANGLE_CHANNEL = "in0/gnd"
CURRENT_CHANNEL = "in1/gnd"

I2C_BUS = smbus2.SMBus(5) #Zde nastavit cislo rozhrani

#Nastaveni proudoveho cidla - viz: https://github.com/pimoroni/ads1015-python
ads1115 = ADS1015(i2c_dev=I2C_BUS)
ads1115.set_mode("single")
ads1115.set_programmable_gain(ADC_RANGE)
ads1115.set_sample_rate(860)

#Proudove cidlo

SENSITIVITY = 0.185 #Podle rozsahu cidla [V/A]
SAMPLES = 100 #Pocet vzorku pri kalibraci

#current_offset = 0.347
current_offset = ADC_RANGE/2 #Vychozi klidova hodnota, presnejsi zjistena kalibraci

#Vychozi okrajove hodnoty uhlu, presnejsi ziskane kalibraci
angle_Vmin = 0.23 
angle_Vmax = 2.98

CLOSED_ANGLE = 10
OPEN_ANGLE = 100

#Specialni pripady - vyuzito pro zasilani action zprav pro kalibraci
CLOSE = -1
OPEN = -2

class adcNode(Node):

    #current = 0
    #current_offset = 0
    #angle = 0

    def __init__(self):
        super().__init__("adc_readout")

        self.get_logger().info("Node started")

        self.sensitivity = SENSITIVITY 
        self.samples = SAMPLES
        self.angle_Vmin = 0.23
        self.angle_Vmax = 2.98

        self.max_angle = OPEN_ANGLE
        self.min_angle = CLOSED_ANGLE

        self.timer = self.create_timer(0.01, self.publish_readings)
        self.current_readout_publisher = self.create_publisher(std_msgs.msg.Float32, "adc_current", 10)
        self.angle_readout_publisher = self.create_publisher(std_msgs.msg.Int32, "adc_angle", 10)
        
        self.gripper_action_client = ActionClient(self, GripperMove, "gripper_move")

        self.calibrate_current_sens()
        self.calibrate_angle_sens()

    def read_values(self):

        current_raw = ads1115.get_voltage(CURRENT_CHANNEL)
        self.current = (current_raw - self.current_offset) / self.sensitivity

        angle_raw = ads1115.get_voltage(ANGLE_CHANNEL)

        self.angle = (angle_raw - self.angle_Vmin) * (self.max_angle - self.min_angle) / (self.angle_Vmax - self.angle_Vmin) + self.min_angle

        #self.get_logger().info(str(current_raw))
        #self.get_logger().info(str(self.current_offset))
        #self.get_logger().info(str(self.sensitivity))

        

    def calibrate_current_sens(self):
        self.get_logger().info("Calibrating current...")
        
        #Zmeri N vzorku a vypocita prumer 
        sum_current_raw = 0.0
        for i in range(self.samples):
            sum_current_raw += ads1115.get_voltage(CURRENT_CHANNEL)
        self.current_offset = sum_current_raw / self.samples

        self.get_logger().info("Current calbritated - offset: {} V".format(self.current_offset))

    def calibrate_angle_sens(self):
        
        #Kalibrace krajnich hodnot polohy (potenciometru) serva
        #Pomoci actionu zasle na krajni hodnotu -> Zmeri N vzorku a vypocita prumer -> Ulozi hodnotu
        #Opakuje druhou krajni hodnotu

        #Pouziva 0 a 180, misto opravdovych krajnich metod, protoze se muzou menit
        #Logika gripper controlleru si prekroceni mezi pohlida

        self.get_logger().info("Calibrating servo angle....")
        action_msg = GripperMove.Goal()
        action_msg.action = 0

        self.get_logger().info("Sending action message to servo")
        self.gripper_action_client.send_goal_async(action_msg)

        self.gripper_action_client.wait_for_server()

        time.sleep(0.5) #Zajisti ze servo je opravdu v krajni hodnote
        sum_angle_raw = 0
        for i in range(self.samples):
            sum_angle_raw += ads1115.get_voltage(ANGLE_CHANNEL)
        self.angle_Vmin = sum_angle_raw / self.samples
        self.get_logger().info("Min angle calibrated, value:{} V".format(self.angle_Vmin))

        action_msg.action = 180
        self.get_logger().info("Sending action message to servo")
        self.gripper_action_client.send_goal_async(action_msg)

        self.gripper_action_client.wait_for_server()

        time.sleep(0.5)
        sum_angle_raw = 0
        for i in range(self.samples):
            sum_angle_raw += ads1115.get_voltage(ANGLE_CHANNEL)
        self.angle_Vmax = sum_angle_raw / self.samples
        self.get_logger().info("Max angle calibrated, value:{} V".format(self.angle_Vmax))

        action_msg.action = 0
        self.get_logger().info("Returning to default position")
        self.gripper_action_client.send_goal_async(action_msg)


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
    node = adcNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
