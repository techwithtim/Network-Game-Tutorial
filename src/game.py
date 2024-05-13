import pygame
from src.network import Network
from src.player import Player
from src.canvas import Canvas
from src.game_states import *
from src.state_manager import StateManager

class Game:
    def __init__(self, w, h, host, port):
        self.net = Network(host, port)
        self.width = w
        self.height = h
        self.player = Player(50, 50)
        self.player2 = Player(100,100)
        self.canvas = Canvas(self.width, self.height, "Guess Word")
        self.game_state = StateManager(StartState())
        
    def run(self):
        self.game_state.run(self)

    def send_data(self):
        """
        Send position to server
        :return: None
        """
        data = str(self.net.id) + ":" + str(self.player.x) + "," + str(self.player.y)
        reply = self.net.send(data)
        return reply

    @staticmethod
    def parse_data(data):
        try:
            d = data.split(":")[1].split(",")
            return int(d[0]), int(d[1])
        except:
            return 0,0
