import network

# Connect to WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Tenda_F6BEC0', '')

#LED Control
from machine import Pin, PWM

R = 14
G = 12
B = 27
db = {'1': {'firstname': 'Alex', 'lastname': 'River'},
      '2': {'firstname': 'Lannie', 'lastname': 'Fox'}}
next_id = 3
#Frequency: [0,78125]. Step 5000Hz.
#Duty cycle: [0, 1023]
def RGB(r,g,b):    
    red = PWM(Pin(R), freq=1000, duty=int(1023*r/255))
    green = PWM(Pin(G), freq=1000, duty=int(1023*g/255))
    blue = PWM(Pin(B), freq=1000, duty=int(1023*b/255))
    
    
import dht, time

signal = 15
dht11 = dht.DHT11(Pin(signal))
#Setup webserver
import tinyweb


# Create web server application
app = tinyweb.webserver()

class LedControl():
    def get(self, data):
        """Return list of all customers"""
        return db

    def post(self, data):
        """Add customer"""
        global next_id
        print(data)
        RGB(int(data['red']), int(data['green']), int(data['blue']))
        db[str(next_id)] = data
        next_id += 1
        # Return message AND set HTTP response code to "201 Created"
        return {'message': 'created'}, 201

@app.route('/css/<fn>')
async def files_css(req, resp, fn):
    file = 'static/css/{}'.format(fn)
    await resp.send_file(file)

@app.route('/js/<fn>')
async def files_js(req, resp, fn):
    file = 'static/js/{}'.format(fn)
    await resp.send_file(file)
    
@app.resource('/dht11')
def user(data):
    dht11.measure()
    return {'temp': dht11.temperature(), 'humid': dht11.humidity()}
# Index page
@app.route('/')
async def index(request, response):
    # Start HTTP response with content-type text/html
    await response.send_file('static/index.html')
#    await response.start_html()
    # Send actual HTML page
 #   await response.send('<html><body><h1>Hello, world! (<a href="/table">table</a>)</h1></html>\n')

def run():
    app.add_resource(LedControl, '/rgb')
    app.run(host='0.0.0.0', port=8081)
    
run()
