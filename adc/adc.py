#!/usr/bin/env python
import time

from ads1015 import ADS1015
import smbus2

#Parametry pro převod
adc_range = 6.144

#Proudove cidlo

sensitivity = 0.185
vref = 3.3
samples = 100
#current_offset = 0.347
current_offset = adc_range/2

angle_Vmin = 0.23
angle_Vmax = 2.98

#Nastaveni ADC

#CHANNELS = ["in0/ref", "in1/ref", "in2/ref"]
CHANNELS = ["in0/gnd", "in1/gnd", "in2/gnd"]

angle_channel = "in0/gnd"
current_channel = "in2/gnd"

bus = smbus2.SMBus(5)

ads1115 = ADS1015(i2c_dev=bus)
chip_type = ads1115.detect_chip_type()

if chip_type == "ADS1015":
    ads1115.set_sample_rate(1600)
else:
    ads1115.set_sample_rate(860)

print("Found: {}".format(chip_type))

ads1115.set_mode("single")
ads1115.set_programmable_gain(adc_range)




#Kalibrace 

sum_current_raw = 0.0
for i in range(samples):
    sum_current_raw += ads1115.get_voltage(current_channel)
current_offset = sum_current_raw / samples


while True:

    #Poloha
    
    angle_raw = ads1115.get_voltage(angle_channel) 
    angle = (angle_raw - angle_Vmin) * 180 / (angle_Vmax - angle_Vmin)

    print("Angle: {:6.1f} raw: {:6.3f} V".format(angle, angle_raw), end=" | ")

    #Proud
    
    #sum_current = 0.0
    #for i in range(samples):
    #    sum_current += ads1115.get_voltage(current_channel)
#
    #current_avg = (sum_current / samples) * (adc_range / 1023.0)
    #current = (current_avg - current_offset) / sensitivity
#
    current_raw = ads1115.get_voltage(current_channel)
    current = (current_raw - current_offset) / sensitivity

    print("Current: {:2.4f} A raw: {:6.1f}".format(current, current_raw))
    #print("Proud: {:6.3f} A".format(current))
