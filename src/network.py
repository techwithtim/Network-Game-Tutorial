import socket
import pickle
from .request import Request
from .player import Player

class Network:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host # For this to work on your machine this must be equal to the ipv4 address of the machine running the server
                                    # You can find this address by typing ipconfig in CMD and copying the ipv4 address. Again this must be the servers
                                    # ipv4 address. This feild will be the same for all your clients.
        self.port = port
        self.addr = (self.host, self.port)
        self.id = self.connect() 


    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def send(self, data):
        """
        :param data: bytes
        :return: bytes
        """
        try:
            self.client.send(data)
            reply = self.client.recv(2048)
            return reply
        except socket.error as e:
            return str(e)
        
    currentId = "0"
    states = [Request(0, Player()), Request(1, Player())]
    @staticmethod
    def threaded_client(conn):
        conn.send(str.encode(Network.currentId))
        Network.currentId = "1"
        while True:
            try:
                data = conn.recv(2048)
                if not data:
                    conn.send(str.encode("Goodbye"))
                    break
                else:
                    request:Request = pickle.loads(data)
                    player:Player = request.get_player()
                    id:int = request.get_net_id()
                    ready:bool = player.get_ready()
                    try:
                        Network.states[id] = Request(id, player)
                    except Exception as e:
                        print(str(e))
                    print(f"ID: {id}, ready: {ready}")
                    if id == 0: nid = 1
                    if id == 1: nid = 0
                try:
                    reply = pickle.dumps(Network.states[nid])
                    conn.sendall(reply)
                except Exception as e:
                    print(str(e))
            except:
                print("An Error has Occurred")
                break

        print("Connection Closed")
        conn.close()
