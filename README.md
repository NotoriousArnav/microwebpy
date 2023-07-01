# MicroWebPy
MicroWebPy: Miniature Web Server in MicroPython
This is a simple HTTP server implementation in MicroPython. It allows you to create routes and handle HTTP requests easily.

## HTTPServer.py

This file contains the core implementation of the HTTP server.

### Classes

#### Response

- `Response` is a base class for creating HTTP responses.
- Methods:
  - `set_header(key, value)`: Sets a header field in the response.
  - `set_status(status)`: Sets the HTTP status code for the response.
  - `set_body(body)`: Sets the body of the response.
  - `send(sock)`: Sends the response to the client.

#### JSONResponse

- `JSONResponse` is a subclass of `Response` that simplifies creating JSON responses.
- Methods:
  - `set_json_body(data)`: Sets the response body as JSON data.

#### HTTPServer

- `HTTPServer` is the main class that represents the HTTP server.
- Methods:
  - `__init__(host, port)`: Initializes the server with the specified host and port.
  - `add_route(path, handler)`: Adds a route and its corresponding request handler to the server.
  - `start()`: Starts the server and listens for incoming connections.
  - `handle_request(request)`: Handles an incoming HTTP request.
  - `default_handler()`: Default handler for 404 Not Found responses.

## main.py

This file demonstrates the usage of the HTTP server.

### Example Usage

```python
from HTTPServer import HTTPServer, Response, JSONResponse
import network

# Define request handlers
def index_handler(method, path):
    response = JSONResponse()
    response.set_json_body({"message": "Welcome to the index page!"})
    return response

# Create server instance
server = HTTPServer("0.0.0.0", 8080)

# Add routes and their handlers
server.add_route("/", index_handler)

# Start the server
server.start()
```
