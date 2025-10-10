# Displays file list and download a specific file

import socket
import sys

# This was tested on 10.10.10.215:9001 can be changed
HOST = "10.10.10.215"
PORT = 9001

# --- Step 1: Check host and port availability ---
try:
    test_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    test_sock.settimeout(5)
    test_sock.connect((HOST, PORT))
    print(f"[+] Successfully connected to {HOST}:{PORT}")
    test_sock.close()
except Exception as e:
    print(f"[!] Connection failed: {e}")
    sys.exit()

# --- Step 2: Create client to request file list ---
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect((HOST, PORT))
print("[+] Connected to server for file listing")

request = f"GET / HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
client1.sendall(request.encode())

response = b""
while True:
    data = client1.recv(4096)
    if not data:
        break
    response += data

print("\n[+] Files available on server:")
print(response.decode(errors="ignore"))
client1.close()


# --- Step 3: Create new client to download a specific file ---
filename = "file1.txt"
print(f"\n[+] Starting download of {filename}")

client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect((HOST, PORT))

request = f"GET /{filename} HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
client2.sendall(request.encode())

file_data = b""
while True:
    chunk = client2.recv(4096)
    if not chunk:
        break
    file_data += chunk

with open(filename, "wb") as f:
    f.write(file_data)

print(f"[+] File '{filename}' downloaded successfully.")
client2.close()
print("[+] Connection closed.")
