from HTTPServer import HTTPServer, Response, JSONResponse
from jwt import *
import network

def index_handler(method, path, **kwargs):
    response = JSONResponse()
    response.set_json_body({"message": "Welcome to the index page!"})
    return response

# Create server instance
server = HTTPServer("0.0.0.0", 8080)

# Add routes and their handlers
server.add_route("/", index_handler)

secret_key = "secret_key"

#Middlewares

# Print IP Info
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print(wlan.ifconfig())


# Start the server
error = server.start()
raise error
