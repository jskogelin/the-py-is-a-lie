import json
import socketserver
from pprint import pprint
from http.server import BaseHTTPRequestHandler, HTTPServer

from model import Model, ModelCollection

# Sets up a http server
# Reads a config json

with open('pylie.json') as j:
    data = json.load(j)

class Router:
    def __init__(self, route_config):
        self.route_config = route_config
        self.routes = {}

    def map_models(self):
        for attr, value in self.route_config.items():
            self.routes[attr] = ModelCollection(config_range=value['range'], data=value['data'])

    def route_request(self, path):
        response = {}
        if path in self.routes:
            response['data'] = self.routes[path].get_model_data()
            response['status'] = 200

        return json.dumps(response).encode()

router = Router(route_config=data['routes'])
router.map_models()

# Check it out https://gist.github.com/bradmontgomery/2219997
class ServerHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        response = router.route_request(self.path)
        self._set_headers()
        self.wfile.write(response)

def run(server=HTTPServer, handler=ServerHandler, port=80):
   address = ('', port) 
   httpd = server(address, handler)
   print('Here we go!')
   httpd.serve_forever()

run()
