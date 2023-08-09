#RohanRenganathan

import pygame
from linestreet import Line

pygame.init()

# class stores line in list and call previous class to display 3 lines on street
class Street:
    # initializing construtor to create street
    def __init__(self, lineImg):
        self.line1 = Line(150, -800, 50, 50, lineImg)
        self.line2 = Line(450, -800, 50, 50, lineImg)
        self.line3 = Line(800, -800, 50, 50, lineImg)
        self.line4 = Line(150, -500, 50, 50, lineImg)
        self.line5 = Line(450, -500, 50, 50, lineImg)
        self.line6 = Line(800, -500, 50, 50, lineImg)
        self.line7 = Line(150, -200, 50, 50, lineImg)
        self.line8 = Line(450, -200, 50, 50, lineImg)
        self.line9 = Line(800, -200, 50, 50, lineImg)

        # list to store each lane of the game
        self.firstColumn = [self.line1, self.line2, self.line3]
        self.secondColumn = [self.line4, self.line5, self.line6]
        self.thirdColumn = [self.line7, self.line8, self.line9]

        # speed varies as user plays game
        self.speed = 2
    
    # function loops through
    def draw(self, screen):
        for firstColumn in self.firstColumn:
            firstColumn.rect.y += self.speed

            # line returns to top of screen when previous line reaches bottom of screen
            if firstColumn.rect.y > 500:
                firstColumn.rect.y = -400

            firstColumn.draw(screen)

        for secondColumn in self.secondColumn:
            secondColumn.rect.y += self.speed

            # line will return to top if it leaves the screen
            if secondColumn.rect.y > 500:
                secondColumn.rect.y = -400
            secondColumn.draw(screen)

        for thirdColumn in self.thirdColumn:
            thirdColumn.rect.y += self.speed

            # line will return to top of it leaves the screen
            if thirdColumn.rect.y > 500:
                thirdColumn.rect.y = -400

            thirdColumn.draw(screen)
