from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
import socketserver
from pathlib import Path
import os

HOST = "127.0.0.1"
PORT =  9999

class WebRequestHandler(BaseHTTPRequestHandler):

    # Initialize the directory to serve requests from www
    BASE_DIR = Path(__file__).parent / "www"
    ALLOWED_FILES = {"index.html"}
   
    def do_GET(self):
        
        # Convert the URL to a file system path
        if self.path == "/":
            self.path = "/index.html"
        
        # Sanitize user input 
        requested_path = Path(self.path.lstrip("/"))

        # Normalize the file path 
        full_path = (self.BASE_DIR / requested_path).resolve()
        
        # Make sure the file path is relative to the www directory
        # and the filename is whitelisted
        if (not full_path.is_relative_to(self.BASE_DIR) 
            or full_path.name not in self.ALLOWED_FILES
        ):
            self.send_response(HTTPStatus.FORBIDDEN)
            self.end_headers()
            return
        
        try:
           with full_path.open("rb") as file:
               self.send_response(HTTPStatus.OK)
               self.send_header("Content-Type", "text/html")
               self.end_headers()
               self.wfile.write(file.read())
               return
        except FileNotFoundError:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.end_headers()
            return
                
     
with socketserver.TCPServer((HOST, PORT), WebRequestHandler) as server:
    print("Starting")
    server.serve_forever()