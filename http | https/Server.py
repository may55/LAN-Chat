from http.server import BaseHTTPRequestHandler, HTTPServer

msgs = {} #{'a' : {'b' : ["hi", "hello"], 'c' : ["tata", "bbye"]}}

class RHC(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/')
        self.end_headers()
    
    def do_GET(self):
        self._set_headers()
        user = self.path.split('?')[1]
        if user in msgs:
        	data = ""
        	for lst in msgs[user].keys():
        		for msg in msgs[user][lst]:
        			data = data + "," + lst + ":" + msg
        	self.wfile.write(data.encode("utf-8"))
        	del msgs[user]
        else:
        	self.wfile.write("".encode("utf-8"))
    
    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        content_length = int(self.headers['Content-Length'])
        txt = self.rfile.read(content_length)
        txt = txt.decode("utf-8")
        
        to_user, msg = txt.split('}')
        to_user = to_user[1:]
        msg = msg.strip()

        user = self.path.split('?')[1]

  t      if to_user in msgs:
        	if user in msgs[to_user]:
        		msgs[to_user][user].append(msg)
        	else:
        		msgs[to_user][user] = [msg]
        else:
        	msgs[to_user] = {user : [msg]}
        self.wfile.write("posted".encode("utf-8"))

def run(server_class = HTTPServer, handler_class = RHC, port=1998):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print('Starting...')
    httpd.serve_forever()

run()