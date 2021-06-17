import network

# Connect to WiFi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Tenda_F6BEC0', '')

#Setup webserver
import tinyweb


# Create web server application
app = tinyweb.webserver()

# Index page
@app.route('/')
async def index(request, response):
    # Start HTTP response with content-type text/html
    await response.start_html()
    # Send actual HTML page
    await response.send('<html><body><h1>Hello, world! (<a href="/table">table</a>)</h1></html>\n')


def run():
    app.run(host='0.0.0.0', port=8081)
    

run()