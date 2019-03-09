# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
import network
import time
webrepl.start()
gc.collect()
network.WLAN(network.AP_IF).active(False)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('PLAY INTERNET 4G LTE-9CC6', '02583353')
count = 0
while not sta_if.isconnected():
	time.sleep_ms(1)
	count += 1
	if count==10000:
		print('Not connected')
		break
print('Config: ', sta_if.ifconfig())