import machine
import time
import logging
from machine import ADC

logging.basicConfig(logging.INFO)#, 'log.txt')
_log = logging.getLogger('main')

_pin = machine.Pin(2, machine.Pin.OUT)

adc = ADC(0)            # create ADC object on ADC pin

minValue = 1024
maxValue = 1

def calculateSleep(val):
    global minValue, maxValue
    minValue = min(minValue, val)
    maxValue = max(maxValue, val)
    if maxValue == minValue:
        return 1000
    normalized = (val - minValue) / (maxValue - minValue)
    return int(normalized*1024)

while True:
    _pin.on()
    val = adc.read()
    sleep = calculateSleep(val)
    _log.info("pin value=%d, sleep value=%d, lo=%d, hi=%d", val, sleep, minValue, maxValue)
    time.sleep_ms(sleep)
    _pin.off()
    time.sleep_ms(sleep)
