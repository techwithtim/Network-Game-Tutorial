import socket
from _thread import *
from src.network import Network
import sys

if len(sys.argv) != 2:
    print("Usage: python server.py <port_no>")
    exit()
count_client = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'localhost'
port = int(sys.argv[1])
server_ip = socket.gethostbyname(server)
try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))
s.listen(2)

while count_client != 2:
    print(f"Waiting for {2-count_client} connection")
    conn, addr = s.accept()
    print("Connected to: ", addr)
    count_client = count_client + 1
    start_new_thread(Network.threaded_client, (conn,))

while True:
    pass