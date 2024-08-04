import http.server
import socketserver

PORT = 8000
SERVER_ADDRESS = "localhost"

# class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def end_headers(self):
#         self.send_header('Content-Type', 'application/json;charset=utf-8')
#         super().end_headers()

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
      ".js": "application/javascript",
})

httpd = socketserver.TCPServer((SERVER_ADDRESS, PORT), Handler)
httpd.serve_forever()