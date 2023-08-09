#RohanRenganathan

import pygame
import sys

from Buttons.button import Button

pygame.init()

black = (0, 0, 0)
lightBlack = (50, 50, 50)
blue = (0, 0, 200)
orange = (255, 128, 0)
lime = (156, 186, 33)


class CustomiseCar:
    # initializing constructor for player  to choose car
    def __init__(self, gameDisplays):
        self.width = 1300
        self.height = 660
        self.screen = gameDisplays
        self.img = pygame.image.load("BackgroundImages/Background3.png")
        self.garage = ["CustomCars/Custom1.png",
                       "CustomCars/Custom2.png", "CustomCars/Custom3.png",
                       "CustomCars/Custom4.png", "CustomCars/Custom5.png", "CustomCars/Custom6.png",
                       "CustomCars/Custom7.png", "CustomCars/Custom8.png", "CustomCars/Custom9.png",
                       "CustomCars/Custom10.png"]
        self.playerCar = 0  # default car will always be first car for player
        self.currentCar = self.playerCar    # points to the car currently being displayed on customisation screen
        self.power = ["POWER: 425 HP", "POWER: 386 HP", "POWER: 291 HP", "POWER: 572 HP", "POWER: 297 HP", "POWER: 302 HP", "POWER: 587 HP", "POWER: 252 HP", "POWER: 298 HP", "POWER: 307 HP"]
        self.torque = ["TORQUE: 507 NM", "TORQUE: 412 NM", "TORQUE: 398 NM", "TORQUE: 532 NM", "TORQUE: 406 NM", "TORQUE: 418 NM", "TORQUE: 582 NM", "TORQUE: 346 NM", "TORQUE: 408 NM", "TORQUE: 416 NM"]
        self.traction = ["TRACTION: AWD", "TRACTION: RWD", "TRACTION: RWD", "TRACTION: AWD", "TRACTION: AWD", "TRACTION: RWD", "TRACTION: AWD", "TRACTION: RWD", "TRACTION: AWD", "TRACTION: AWD"]
        self.weight = ["WEIGHT: 1500 KG", "WEIGHT: 1500 KG", "WEIGHT: 1600 KG", "WEIGHT: 1470 KG", "WEIGHT: 1280 KG", "WEIGHT: 1268 KG", "WEIGHT: 728 KG", "WEIGHT: 1420 KG", "WEIGHT: 1248 KG", "WEIGHT: 1332 KG"]


    # function for previous arrow key
    def previousCar(self):
        if self.currentCar == 0:
            self.currentCar = len(self.garage)-1    # on first car so currentCar = last car in list

        else:
            self.currentCar = self.currentCar-1

    # function for next arrow key
    def nextCar(self):
        if self.currentCar == len(self.garage)-1:
            self.currentCar = 0     # reached final car so currentCar = first car in list

        else:
            self.currentCar = self.currentCar + 1

    # creates a text object and returns text
    def carAttributes(self, textX, textY, text, rectX, rectY, rectHeight, rectWidth):
        # creates rectangle to display car attributes
        rect = pygame.Rect(rectX, rectY, rectHeight, rectWidth)
        pygame.draw.rect(self.screen, lightBlack, rect)
        smallText = pygame.font.Font("freesansbold.ttf", 16)
        textsurface = smallText.render(text, True, lime)
        textRect = textsurface.get_rect()
        # position text in centre of rectangle underneath car
        textRect.center = (textX, textY)
        return textsurface, textRect

    # function for displaying the appropriate car to the player
    def customization(self):
        customize = True

        rect = pygame.Rect(450, 72, 100, 100)
        pygame.draw.rect(self.screen, blue, rect)
        smalltext = pygame.font.Font("freesansbold.ttf", 90)
        textsurface = smalltext.render("GARAGE", True, orange)
        textRect = rect

        previousImageButton = pygame.image.load("Buttons/previousButton.png")
        prevRect = pygame.Rect(65, 312, previousImageButton.get_width(), previousImageButton.get_height())

        nextImageButton = pygame.image.load("Buttons/nextButton.png")
        nextRect = pygame.Rect(1135, 312, nextImageButton.get_width(), nextImageButton.get_height())

        backButton = Button(self.screen, "BACK", 100, 575, 100, 50, black, lightBlack, orange)
        selectButton = Button(self.screen, "SELECT", 1100, 575, 100, 50, black, lightBlack, orange)

        carImg0 = pygame.image.load(self.garage[0])
        carImg1 = pygame.image.load(self.garage[1])
        carImg2 = pygame.image.load(self.garage[2])
        carImg3 = pygame.image.load(self.garage[3])
        carImg4 = pygame.image.load(self.garage[4])
        carImg5 = pygame.image.load(self.garage[5])
        carImg6 = pygame.image.load(self.garage[6])
        carImg7 = pygame.image.load(self.garage[7])
        carImg8 = pygame.image.load(self.garage[8])
        carImg9 = pygame.image.load(self.garage[9])

        while customize:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    if prevRect.collidepoint(mouse):
                        self.previousCar()

                    elif nextRect.collidepoint(mouse):
                        self.nextCar()

                    elif backButton.rect.collidepoint(mouse):
                        action = "menu"
                        return action

                    elif selectButton.rect.collidepoint(mouse):
                        action = "select"
                        self.playerCar = self.currentCar
                        print("Player Car: " + str(self.playerCar))
                        return action

            self.screen.blit(self.img, (0, 0))
            self.screen.blit(textsurface, textRect)

            mouse = pygame.mouse.get_pos()

            self.screen.blit(previousImageButton, prevRect)
            self.screen.blit(nextImageButton, nextRect)

            backButton.setButtonStatus(mouse)
            selectButton.setButtonStatus(mouse)

            # below lines blits the car in centre of screen and specific attributes underneath
            if self.currentCar == 0:
                self.screen.blit(carImg0, (((self.width / 2) - carImg0.get_rect().width / 2), ((self.height / 2) - carImg0.get_rect().height / 2)))
                tsurface, trect = self.carAttributes(360, 550, self.power[0], 285, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(530, 550, self.torque[0], 455, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(700, 550, self.traction[0], 625, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(870, 550, self.weight[0], 795, 527, 150, 40)
                self.screen.blit(tsurface, trect)

            elif self.currentCar == 1:
                self.screen.blit(carImg1, (((self.width / 2) - carImg1.get_rect().width / 2), ((self.height / 2) - carImg1.get_rect().height / 2)))
                tsurface, trect = self.carAttributes(360, 550, self.power[1], 285, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(530, 550, self.torque[1], 455, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(700, 550, self.traction[1], 625, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(870, 550, self.weight[1], 795, 527, 150, 40)
                self.screen.blit(tsurface, trect)

            elif self.currentCar == 2:
                self.screen.blit(carImg2, (((self.width / 2) - carImg2.get_rect().width / 2), ((self.height / 2) - carImg2.get_rect().height / 2)))
                tsurface, trect = self.carAttributes(360, 550, self.power[2], 285, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(530, 550, self.torque[2], 455, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(700, 550, self.traction[2], 625, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(870, 550, self.weight[2], 795, 527, 150, 40)
                self.screen.blit(tsurface, trect)

            elif self.currentCar == 3:
                self.screen.blit(carImg3, (((self.width / 2) - carImg3.get_rect().width / 2), ((self.height / 2) - carImg3.get_rect().height / 2)))
                tsurface, trect = self.carAttributes(360, 550, self.power[3], 285, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(530, 550, self.torque[3], 455, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(700, 550, self.traction[3], 625, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(870, 550, self.weight[3], 795, 527, 150, 40)
                self.screen.blit(tsurface, trect)

            elif self.currentCar == 4:
                self.screen.blit(carImg4, (((self.width / 2) - carImg4.get_rect().width / 2), ((self.height / 2) - carImg4.get_rect().height / 2)))
                tsurface, trect = self.carAttributes(360, 550, self.power[4], 285, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(530, 550, self.torque[4], 455, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(700, 550, self.traction[4], 625, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(870, 550, self.weight[4], 795, 527, 150, 40)
                self.screen.blit(tsurface, trect)

            elif self.currentCar == 5:
                self.screen.blit(carImg5, (((self.width / 2) - carImg5.get_rect().width / 2), ((self.height / 2) - carImg5.get_rect().height / 2)))
                tsurface, trect = self.carAttributes(360, 550, self.power[5], 285, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(530, 550, self.torque[5], 455, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(700, 550, self.traction[5], 625, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(870, 550, self.weight[5], 795, 527, 150, 40)
                self.screen.blit(tsurface, trect)

            elif self.currentCar == 6:
                self.screen.blit(carImg6, (((self.width / 2) - carImg6.get_rect().width / 2), ((self.height / 2) - carImg6.get_rect().height / 2)))
                tsurface, trect = self.carAttributes(360, 550, self.power[6], 285, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(530, 550, self.torque[6], 455, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(700, 550, self.traction[6], 625, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(870, 550, self.weight[6], 795, 527, 150, 40)
                self.screen.blit(tsurface, trect)

            elif self.currentCar == 7:
                self.screen.blit(carImg7, (((self.width / 2) - carImg7.get_rect().width / 2), ((self.height / 2) - carImg7.get_rect().height / 2)))
                tsurface, trect = self.carAttributes(360, 550, self.power[7], 285, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(530, 550, self.torque[7], 455, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(700, 550, self.traction[7], 625, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(870, 550, self.weight[7], 795, 527, 150, 40)
                self.screen.blit(tsurface, trect)

            elif self.currentCar == 8:
                self.screen.blit(carImg8, (((self.width / 2) - carImg8.get_rect().width / 2), ((self.height / 2) - carImg8.get_rect().height / 2)))
                tsurface, trect = self.carAttributes(360, 550, self.power[8], 285, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(530, 550, self.torque[8], 455, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(700, 550, self.traction[8], 625, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(870, 550, self.weight[8], 795, 527, 150, 40)
                self.screen.blit(tsurface, trect)

            elif self.currentCar == 9:
                self.screen.blit(carImg9, (((self.width / 2) - carImg9.get_rect().width / 2), ((self.height / 2) - carImg9.get_rect().height / 2)))
                tsurface, trect = self.carAttributes(360, 550, self.power[9], 285, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(530, 550, self.torque[9], 455, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(700, 550, self.traction[9], 625, 527, 150, 40)
                self.screen.blit(tsurface, trect)
                tsurface, trect = self.carAttributes(870, 550, self.weight[9], 795, 527, 150, 40)
                self.screen.blit(tsurface, trect)

            pygame.display.update()













