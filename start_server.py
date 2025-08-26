import http.server
import socketserver
import os
import sys
import webbrowser
from functools import partial
from datetime import datetime

PORT = 5500
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        pass

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

def main():
    directory = os.getcwd()
    Handler = partial(NoCacheHandler, directory=directory)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("="*60)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Local server running")
        print(f"Serving directory: {directory}")
        print(f"URL: http://localhost:{PORT}/")
        print("Common pages:")
        for page in ["index.html", "life.html", "research.html", "projects.html", "cv.html"]:
            if os.path.exists(os.path.join(directory, page)):
                print(f"  - {page}: http://localhost:{PORT}/{page}")
        print("="*60)
        try:
            # Try to open the index page automatically
            if os.path.exists(os.path.join(directory, "index.html")):
                webbrowser.open(f"http://localhost:{PORT}/index.html")
            else:
                webbrowser.open(f"http://localhost:{PORT}/")
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down...")

if __name__ == "__main__":
    main()