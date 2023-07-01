import socket
import select
import json

class Response:
    def __init__(self):
        self.status = 200
        self.headers = {}
        self.body = b""

    def set_header(self, key, value):
        self.headers[key] = value

    def set_status(self, status):
        self.status = status

    def set_body(self, body):
        self.body = body

    def send(self, sock):
        self.set_header("Content-Length", str(len(self.body)))
        response = "HTTP/1.1 {} OK\r\n".format(self.status)
        for key, value in self.headers.items():
            response += "{}: {}\r\n".format(key, value)
        response += "\r\n"
        print(response, self.body, sep='\n')
        sock.sendall(response.encode('utf-8'))
        sock.sendall(self.body)

class JSONResponse(Response):
    def __init__(self):
        super().__init__()
        self.set_header("Content-Type", "application/json")

    def set_json_body(self, data):
        json_data = json.dumps(data)
        self.set_body(json_data.encode("utf-8"))

class HTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.routes = {}

    def add_route(self, path, handler):
        self.routes[path] = handler

    def start(self):
        server_socket = socket.socket()
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)

        inputs = [server_socket]
        print("Server listening on {}:{}".format(self.host, self.port))

        while True:
            readable, _, _ = select.select(inputs, [], [])

            for sock in readable:
                if sock is server_socket:
                    client_socket, client_address = server_socket.accept()
                    inputs.append(client_socket)
                else:
                    try:
                        request = sock.recv(4098)
                        if request:
                            response = self.handle_request(request)
                            response.send(sock)
                        else:
                            sock.close()
                            inputs.remove(sock)
                    except Exception as e:
                        print("Exception:", e)
                        sock.close()
                        inputs.remove(sock)

    def handle_request(self, request):
        request = request.decode("utf-8")
        print(request)
        method, path, version = request.split('\r\n')[0].split(" ")
        #method, path, _, _, _ = request.split("\r\n", 4)
        print(f"{method=}\t{path=}\t{version=}")
        if path in self.routes:
            handler = self.routes[path]
            response = handler(method, path)
        else:
            response = self.default_handler()

        return response

    def default_handler(self):
        response = Response()
        response.set_status(404)
        response.set_body(b"404 Not Found")
        return response

