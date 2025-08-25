from http.server import HTTPServer,BaseHTTPRequestHandler

content="""
<html>
<head>
<title>Department Strength</title>
</head>
<body bgcolor="lightyellow">

<h2 align="center">Department Strength</h2>

<center>
<table border="1" bgcolor="lightblue" cellpadding="10">
<tr bgcolor="orange">
  <th>S.No</th>
  <th>Department</th>
  <th>Strength</th>
</tr>
<tr>
  <td>1</td>
  <td>CSE</td>
  <td>2000</td>
</tr>
<tr>
  <td>2</td>
  <td>AIDS</td>
  <td>4000</td>
</tr>
<tr>
  <td>3</td>
  <td>AIML</td>
  <td>5000</td>
</tr>
<tr>
  <td>4</td>
  <td>ECE</td>
  <td>3000</td>
</tr>
<tr bgcolor="lightgreen">
  <td colspan="2" align="center"><b>Total</b></td>
  <td><b>14000</b></td>
</tr>
</table>
</center>

</body>
</html>
"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()