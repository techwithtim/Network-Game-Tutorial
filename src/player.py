import pygame

class Player():
    width = height = 50

    def __init__(self, startx, starty, color=(255,0,0)):
        self.x = startx
        self.y = starty
        self.velocity = 2
        self.color = color

    def draw(self, g):
        pygame.draw.rect(g, self.color ,(self.x, self.y, self.width, self.height), 0)

    def move(self, dirn):
        """
        :param dirn: 0 - 3 (right, left, up, down)
        :return: None
        """

        if dirn == 0:
            self.x += self.velocity
        elif dirn == 1:
            self.x -= self.velocity
        elif dirn == 2:
            self.y -= self.velocity
        else:
            self.y += self.velocity