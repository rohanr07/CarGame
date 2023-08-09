#RohanRenganathan


import pygame

pygame.init()

# class to draw only 1 line on street
class Line:
    # initiliazing constructor for loading line image for street
    def __init__(self, x, y, width, height, lineImg):
        self.rect = pygame.Rect(x, y, width, height)
        self.line = pygame.image.load(lineImg)


    # function to draw rectangle on screen
    def draw(self, screen):
        screen.blit(self.line, self.rect)

