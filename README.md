# EX01 Developing a Simple Webserver

# Date: 25/08/2025
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:

``` python
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
```

# OUTPUT:

![alt text](<Screenshot 2025-08-25 060133.png>)

![alt text](<Screenshot 2025-08-25 060140.png>)

# RESULT:
The program for implementing simple webserver is executed successfully.
