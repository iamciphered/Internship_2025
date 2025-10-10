# Setup a connection using hostname and port

import socket
import sys
import html2text

print(sys.argv[0])

if len(sys.argv) !=3:
    print(f"Usage: python3 {sys.argv[0]} <hostname> <port>")
    sys.exit(1)

#check port number if is valid
try:
    port = int(sys.argv[2])
    if port < 1 or port > 65535:
        raise ValueError
except ValueError:
    print("Error: Port number should be an interger betweeen 0 and 65535")
    sys.exit(1)

hostname = sys.argv[1]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AFINET is for IPV4, SOCK_STREAM is for TCP
client.connect((hostname, port))
print(f"Connected to {hostname} on port {port}")
client.send(b"GET / HTTP/1.1\r\n\r\n")

response = client.recv(4096)
response.decode('utf-8')
print(response)
client.close()
