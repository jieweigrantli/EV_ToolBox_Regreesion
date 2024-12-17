from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

REDIRECT_URI = 'http://localhost:8080'

class OAuthRedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        authorization_code = query.get('code', [None])[0]

        if authorization_code:
            print(f"Authorization code: {authorization_code}")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Authorization code received. You can close this window.")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Authorization code not found.")

def start_local_server():
    print(f"Starting server at {REDIRECT_URI}")
    server = HTTPServer(('localhost', 8080), OAuthRedirectHandler)
    server.serve_forever()

start_local_server()