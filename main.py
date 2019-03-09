import machine
import time
import logging

logging.basicConfig(logging.INFO)#, 'log.txt')
_log = logging.getLogger('main')

_pin = machine.Pin(2, machine.Pin.OUT)

while True:
    _pin.on()
    _log.info("pin value=%s", _pin.value())
    time.sleep(1)
    _pin.off()
    _log.info("pin value=%s", _pin.value())
    time.sleep(1)
