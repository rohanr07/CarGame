#RohanRenganathan


import pygame

class gameBackground:
    # initializing constructor for background of game
    def __init__(self, lineImg):
        self.grass = pygame.image.load("Street/grass.png")
        self.strip = pygame.image.load("Street/strip.png")
        self.line = pygame.image.load(lineImg)
        self.y2 = 5

    # setting up the original display of the game (background, grass, white lines)
    def drawBackground(self, screen):
            screen.blit(self.grass, (0, 0))
            screen.blit(self.grass, (0, 200))
            screen.blit(self.grass, (0, 400))
            screen.blit(self.grass, (1197, 0))
            screen.blit(self.grass, (1197, 200))
            screen.blit(self.grass, (1197, 400))

            screen.blit(self.strip, (120, 0))
            screen.blit(self.strip, (120, 100))
            screen.blit(self.strip, (120, 200))
            screen.blit(self.strip, (1180, 0))
            screen.blit(self.strip, (1180, 100))
            screen.blit(self.strip, (1180, 200))

            # blit the background images of the game to make it appear dynamic
            realY = self.y2 % self.grass.get_rect().width
            screen.blit(self.grass, (0, realY - self.grass.get_rect().width))
            screen.blit(self.grass, (1197, realY - self.grass.get_rect().width))

            # blit the white lines to make it appear dynamic
            screen.blit(self.grass, (0, realY))
            screen.blit(self.grass, (1197, realY))

            # blit the strip to make it appear dynamic
            screen.blit(self.strip, (120, realY - 200))
            screen.blit(self.strip, (120, realY + 20))
            screen.blit(self.strip, (120, realY + 30))
            screen.blit(self.strip, (1180, realY - 100))
            screen.blit(self.strip, (1180, realY + 20))
            screen.blit(self.strip, (1180, realY + 30))

            self.y2 += 3









