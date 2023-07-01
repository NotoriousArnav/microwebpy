from HTTPServer import HTTPServer, Response, JSONResponse
import network

def index_handler(method, path):
    response = JSONResponse()
    response.set_json_body({"message": "Welcome to the index page!"})
    return response

# Create server instance
server = HTTPServer("0.0.0.0", 8080)

# Add routes and their handlers
server.add_route("/", index_handler)

# Print IP Info
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Radhakul', 'Ihapwics123$')
print(wlan.ifconfig())


# Start the server
server.start()
