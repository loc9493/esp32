import dht
import machine, time

signal = 15
d = dht.DHT11(machine.Pin(signal))
#d.measure()
while True:
    d.measure()
    print("Temp: ", d.temperature()) # eg. 23 (°C)
    print("Humid: ", d.humidity())    # eg. 41 (% RH)
    time.sleep(1)