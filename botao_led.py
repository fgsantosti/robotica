from machine import Pin
import utime

led = Pin(22, Pin.OUT)
boton = Pin(7, Pin.IN, Pin.PULL_UP)

while True:
    print ("estado", boton.value())
    if (boton.value()==0):
        led.value(1)
        utime.sleep_ms(300)
    
    if (boton.value()==1):
        led.value(0)
        utime.sleep_ms(300)
    
else:
    led.value(0)
