import pygame
from src.hangman import Hangman

class StartState():
    def run(self, entity):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type in (pygame.QUIT, pygame.K_ESCAPE):
                    run = False
            entity.canvas.draw_background()
            Hangman.prehangman(entity.canvas.get_canvas())
            message="waiting for opponent"
            entity.canvas.draw_text(message, 20, entity.width/2 -len(message)*2.5, entity.height/2)
            entity.canvas.update()
    

class CountDownState():
    pass

class GameState():
    def run(self,entity):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type in (pygame.QUIT, pygame.K_ESCAPE):
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                if entity.player.x <= entity.width - entity.player.velocity:
                    entity.player.move(0)

            if keys[pygame.K_LEFT]:
                if entity.player.x >= entity.player.velocity:
                    entity.player.move(1)

            if keys[pygame.K_UP]:
                if entity.player.y >= entity.player.velocity:
                    entity.player.move(2)

            if keys[pygame.K_DOWN]:
                if entity.player.y <= entity.height - entity.player.velocity:
                    entity.player.move(3)

            # Send Network Stuff
            entity.player2.x, entity.player2.y = entity.parse_data(entity.send_data())

            # Update Canvas
            entity.canvas.draw_background()
            entity.player.draw(entity.canvas.get_canvas())
            entity.player2.draw(entity.canvas.get_canvas())
            entity.canvas.update()

class EndState():
    pass