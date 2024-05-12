import socket

class Network:
    currentId = "0"
    pos = ["0:50,50", "1:100,100"]
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
        :param data: str
        :return: str
        """
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)
        
    @staticmethod
    def threaded_client(conn):
        conn.send(str.encode(Network.currentId))
        Network.currentId = "1"
        reply = ''
        while True:
            try:
                data = conn.recv(2048)
                reply = data.decode('utf-8')
                if not data:
                    conn.send(str.encode("Goodbye"))
                    break
                else:
                    print("Recieved: " + reply)
                    arr = reply.split(":")
                    id = int(arr[0])
                    Network.pos[id] = reply

                    if id == 0: nid = 1
                    if id == 1: nid = 0

                    reply = Network.pos[nid][:]
                    print("Sending: " + reply)

                conn.sendall(str.encode(reply))
            except:
                break

        print("Connection Closed")
        conn.close()
