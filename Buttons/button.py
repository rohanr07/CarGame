#RohanRenganathan

import pygame

black = (0, 0, 0)
orange = (255, 128, 0)
lime = (156, 186, 33)


class Button:
    def __init__(self, screen, text, x, y, buttonWidth, buttonHeight, inactiveColour, activeColour, textColour):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.inactiveColour = inactiveColour
        self.activeColour = activeColour
        self.textColour = textColour

        self.rect = pygame.Rect(x, y, buttonWidth, buttonHeight)

    # function renders the text object on top of the button
    def textObjects(self, text, font):
        textsurface = font.render(text, True, self.textColour)
        return textsurface, textsurface.get_rect()

    def toggleButtonText(self):
        if self.text == "Click to turn Music OFF":
            self.text = "Click to turn Music ON"

        else:
            self.text = "Click to turn Music OFF"

        pygame.draw.rect(self.screen, self.inactiveColour, self.rect)
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.textObjects(self.text, smalltext)
        textRect.center = ((self.x + (self.buttonWidth / 2)), (self.y + (self.buttonHeight / 2)))
        self.screen.blit(textSurf, textRect)

    # function sets the button to active by turning the button to active colour
    def setButtonActive(self):
        pygame.draw.rect(self.screen, self.activeColour, self.rect)
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.textObjects(self.text, smalltext)
        textRect.center = ((self.x + (self.buttonWidth / 2)), (self.y + (self.buttonHeight / 2)))
        self.screen.blit(textSurf, textRect)

    # function sets the button to inactive by turning the button inactive colour
    def setButtonInactive(self):
        pygame.draw.rect(self.screen, self.inactiveColour, self.rect)
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.textObjects(self.text, smalltext)
        textRect.center = ((self.x + (self.buttonWidth / 2)), (self.y + (self.buttonHeight / 2)))
        self.screen.blit(textSurf, textRect)

    # function sets the status of the button by setting it to active or inactive (based on mouse position)
    def setButtonStatus(self, mouse):
        if self.x + self.buttonWidth > mouse[0] > self.x and self.y + self.buttonHeight > mouse[1] > self.y:
            self.setButtonActive()

        else:
            self.setButtonInactive()



