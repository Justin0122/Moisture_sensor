import rp2
import ubinascii
import machine
import time
import utime
from secrets import secrets
from machine import ADC, Pin

min_moisture=0
max_moisture=65535
min_moisture_percent=0
max_moisture_percent=100

soil = ADC(Pin(26))

readDelay = 0.5
while True:
    moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture) 
    print("moisture: " + "%.2f" % moisture +"% (adc: "+str(soil.read_u16())+")")
    utime.sleep(readDelay)



