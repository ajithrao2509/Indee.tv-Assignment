import http.server
import socketserver

# Set the port number you want to use
PORT = 8080

# Set the directory to serve files from. The current directory is represented by "."
Handler = http.server.SimpleHTTPRequestHandler

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}/")
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever()