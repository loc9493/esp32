from machine import Pin, PWM

R = 14
G = 12
B = 27

#Frequency: [0,78125]. Step 5000Hz.
#Duty cycle: [0, 1023]
def RGB(r,g,b):    
    red = PWM(Pin(R), freq=1000, duty=int(1023*r/255))
    green = PWM(Pin(G), freq=1000, duty=int(1023*g/255))
    blue = PWM(Pin(B), freq=1000, duty=int(1023*b/255))

import time
while True:
    RGB(255,0,0)
    time.sleep_ms(500)
    RGB(0,255,0)
    time.sleep_ms(500)
    RGB(0,0,255)
    time.sleep_ms(500)
