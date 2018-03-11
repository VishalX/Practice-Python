import socket

# Create a socket handle
sockhand = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to web server
sockhand.connect(('data.pr4e.org', 80))

# Create command to send to the web server
# HTTP Protocol
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

# Send Command
sockhand.send(cmd)

# Receive data
while True:
    data = sockhand.recv(512)
    if len(data) < 1:
        break
    print(data.decode().strip())

sockhand.close()