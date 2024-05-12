import pygame
from src.state_manager import StateManager

class Canvas:
    def __init__(self, w, h, name="None"):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((w,h),0, 32)
        pygame.display.set_caption(name)

    @staticmethod
    def update():
        pygame.display.update()

    def draw_text(self, text, size, x, y):
        pygame.font.init()
        font = pygame.font.SysFont("comicsans", size)
        render = font.render(text, 1, (0,0,0))
        self.screen.blit(render, (x,y))

    def get_canvas(self):
        return self.screen

    def draw_background(self, color=(255, 255, 255)):
        self.screen.fill(color)