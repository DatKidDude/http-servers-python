from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
import socketserver
from pathlib import Path
import os

HOST = "127.0.0.1"
PORT =  9999

class WebRequestHandler(BaseHTTPRequestHandler):

    # Initialize the directory to serve requests from www
    BASE_DIR = Path("www").resolve()
   
    def do_GET(self):
        
        # Convert the URL to a file system path
        if self.path == "/":
            self.path = "/index.html"

        # Sanitize user input 
        requested_path = Path(self.path.lstrip("/"))

        if requested_path.is_absolute():
            self.send_error(HTTPStatus.FORBIDDEN, "User path must be relative")
            return
        
        try:
            # Strict catches nonexistent files 
            # this can break with something simple like 'www/index' being passed
            full_path = (self.BASE_DIR / requested_path).resolve(strict=True)

            if full_path.exists():
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                with full_path.open("rb") as file:
                    self.wfile.write(file.read())
                return
        except FileNotFoundError:
            self.send_error(HTTPStatus.NOT_FOUND)
       
with socketserver.TCPServer((HOST, PORT), WebRequestHandler) as server:
    print("Starting")
    server.serve_forever()