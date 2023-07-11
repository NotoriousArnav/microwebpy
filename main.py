from HTTPServer import HTTPServer, Response, JSONResponse
import network
from middlewares import BaseMiddleware

def index_handler(method, path, **kwargs):
    response = JSONResponse()
    response.set_json_body({"message": "Welcome to the index page!"})
    return response

def header_check(method, path, middleware_data):
    response = JSONResponse()
    response.set_json_body({
        'headers': middleware_data['base_middleware']
    })
    return response

# Create server instance
server = HTTPServer("0.0.0.0", 8080)

# Add routes and their handlers
server.add_route("/", index_handler)
server.add_route("/headers", header_check)
secret_key = "secret_key"

#Middlewares
base_m = BaseMiddleware()
server.middleware.append(base_m)

# Print IP Info
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print(wlan.ifconfig())


# Start the server
error = server.start()
raise error
