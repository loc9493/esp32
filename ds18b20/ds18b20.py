import network

# Connect to WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Tenda_F6BEC0', '')

#LED Control
from machine import Pin
import onewire, time, ds18x20

signal = 15
ow = onewire.OneWire(Pin(signal))
ds = ds18x20.DS18X20(ow)

while True:
    roms = ds.scan()
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(ds.read_temp(rom))
    

# db = {'1': {'firstname': 'Alex', 'lastname': 'River'},
#       '2': {'firstname': 'Lannie', 'lastname': 'Fox'}}
# next_id = 3
# #Frequency: [0,78125]. Step 5000Hz.
# #Duty cycle: [0, 1023]
# def RGB(r,g,b):    
#     red = PWM(Pin(R), freq=1000, duty=int(1023*r/255))
#     green = PWM(Pin(G), freq=1000, duty=int(1023*g/255))
#     blue = PWM(Pin(B), freq=1000, duty=int(1023*b/255))
# #Setup webserver
# import tinyweb
# 
# 
# # Create web server application
# app = tinyweb.webserver()
# 
# class LedControl():
# 
#     def get(self, data):
#         """Return list of all customers"""
#         return db
# 
#     def post(self, data):
#         """Add customer"""
#         global next_id
#         print(data)
#         RGB(data['red'], data['green'], data['blue'])
#         db[str(next_id)] = data
#         next_id += 1
#         # Return message AND set HTTP response code to "201 Created"
#         return {'message': 'created'}, 201
#     
# # Index page
# @app.route('/')
# async def index(request, response):
#     # Start HTTP response with content-type text/html
#     await response.start_html()
#     # Send actual HTML page
#     await response.send('<html><body><h1>Hello, world! (<a href="/table">table</a>)</h1></html>\n')@app.route('/rgb', methods=['POST'])
# 
# def run():
#     app.add_resource(LedControl, '/rgb')
#     app.run(host='0.0.0.0', port=8081)
#     
# run()
