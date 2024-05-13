import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (200,200,200)

class Hangman:
    def __init__(self, surface):
        self.condition=0
        self.surface=surface
    
    def draw(self):
        for i in range(self.condition):
            if i == 0:
                pygame.draw.line(self.surface, GREY, (10,400),(300,400),8)#baseline
                pygame.draw.line(self.surface, GREY, (50,50),(50,400),8)#stick1
                pygame.draw.line(self.surface, GREY, (50,60),(250,60),8)#stick2
                pygame.draw.line(self.surface, GREY, (150,60),(150,100),8)#rope
                pygame.draw.circle(self.surface, GREY, (150,150),50,8)#head
                pygame.draw.line(self.surface, GREY, (150,200),(150,300),8)#body
                pygame.draw.line(self.surface, GREY, (150,210),(100,250),8)#lefthand
                pygame.draw.line(self.surface, GREY, (150,210),(200,250),8)#righthand
                pygame.draw.line(self.surface, GREY, (150,300),(100,350),8)#leftleg
                pygame.draw.line(self.surface, GREY, (150,300),(200,350),8)#rightleg

            elif i == 1:
                pygame.draw.line(self.surface, BLACK, (10,400),(300,400),8)#baseline

            elif i == 2:
                pygame.draw.line(self.surface, BLACK, (50,50),(50,400),8)#stick1

            elif i == 3:
                pygame.draw.line(self.surface, BLACK, (50,60),(250,60),8)#stick2

            elif i == 4:
                pygame.draw.line(self.surface, BLACK, (150,60),(150,100),8)#rope

            elif i == 5:
                pygame.draw.circle(self.surface, BLACK, (150,150),50,8)#head

            elif i == 6:
                pygame.draw.line(self.surface, BLACK, (150,200),(150,300),8)#body

            elif i == 7:
                pygame.draw.line(self.surface, BLACK, (150,210),(100,250),8)#lefthand

            elif i == 8:
                pygame.draw.line(self.surface, BLACK, (150,210),(200,250),8)#righthand

            elif i == 9:
                pygame.draw.line(self.surface, BLACK, (150,300),(100,350),8)#leftleg

            elif i == 10:
                pygame.draw.line(self.surface, BLACK, (150,300),(200,350),8)#rightleg

            #game over
            elif i == 11:
                pygame.draw.line(self.surface, BLUE, (10,400),(300,400),8)#baselineDisplay
                pygame.draw.circle(self.surface, BLUE, (150,150),50,8)#head
                pygame.draw.line(self.surface, BLUE, (150,200),(150,300),8)#body
                pygame.draw.line(self.surface, BLUE, (150,210),(100,250),8)#lefthand
                pygame.draw.line(self.surface, BLUE, (150,210),(200,250),8)#righthand
                pygame.draw.line(self.surface, BLUE, (150,300),(100,350),8)#leftleg
                pygame.draw.line(self.surface, BLUE, (150,300),(200,350),8)#rightleg

    @staticmethod
    def prehangman(surface):
        """ Draw the Whole Hangman """
        pygame.draw.line(surface, GREEN, (10,400),(190,400),8)#baseline
        pygame.draw.line(surface, GREEN, (30,90),(30,400),8)#stick1
        pygame.draw.line(surface, GREEN, (30,100),(160,100),8)#stick2
        pygame.draw.line(surface, GREEN, (100,100),(100,120),8)#rope
        pygame.draw.circle(surface, GREEN, (100,170),50,8)#head
        pygame.draw.line(surface, GREEN, (100,220),(100,320),8)#body
        pygame.draw.line(surface, GREEN, (100,230),(50,270),8)#lefthand
        pygame.draw.line(surface, GREEN, (100,230),(150,270),8)#righthand
        pygame.draw.line(surface, GREEN, (100,320),(50,360),8)#leftleg
        pygame.draw.line(surface, GREEN, (100,320),(150,360),8)#rightleg