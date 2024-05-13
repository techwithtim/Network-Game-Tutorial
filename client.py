from src.game import Game
from src.game_states import *
import sys

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Usage: python client.py <host_ip> <port_no>")
        exit()
    
    # Start State if Not All Players Are Connected
    g = Game(500, 500, sys.argv[1], int(sys.argv[2]))
    g.run()