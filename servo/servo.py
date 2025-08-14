from piservo import Servo
import time


#Parametry serva
servo_signal_pin = 13 #pin musi podporovat HW PWM - viz RasPi pinout (pinout.xyz)
servo_min_pos = 0 #mozna bude stacit nastavit meze tady
servo_max_pos = 180 
servo_min_pulse = 0.5 #Z datasheetu vyrobce
servo_max_pulse = 2.5
servo_frequency = 50

servo = Servo(servo_signal_pin, servo_min_pos, servo_max_pos, servo_min_pulse, servo_max_pulse, servo_frequency)


#for i in range(0,180,1):
#    servo.write(i)
#    time.sleep(1)

#servo.write(180)


for i in range(3):
    servo.write(0)
    time.sleep(5)
    servo.write(170)
    time.sleep(5)

servo.stop()
