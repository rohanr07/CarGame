#RohanRenganathan ji


import pygame


class Car():
    def __init__(self, carImg, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.carImg = carImg

    def draw(self, screen):
        screen.blit(self.carImg, self.rect)














