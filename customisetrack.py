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
orangeNew = (204, 102, 0)

# class to allow player to choose which race track to play with
class CustomiseTrack:
    # initializing constructor for player  to choose track
    def __init__(self, gameDisplays):
        self.width = 1300
        self.height = 660
        self.screen = gameDisplays
        self.img = pygame.image.load("BackgroundImages/Background3.png")
        self.tracks = ["CustomTrack/track1.png", "CustomTrack/track2.png", "CustomTrack/track3.png", "CustomTrack/track4.png"]#, "CustomTrack/track5.png"]
        self.playerTrack = 0
        self.currentTrack = self.playerTrack


    # function for previous arrow key
    def previousTrack(self):
        if self.currentTrack == 0:
            self.currentTrack = len(self.tracks)-1

        else:
            self.currentTrack = self.currentTrack-1

    # function for next arrow key
    def nextTrack(self):
        if self.currentTrack == len(self.tracks)-1:
            self.currentTrack = 0

        else:
            self.currentTrack = self.currentTrack + 1

    # function for displaying the appropriate track to the player
    def customization(self):
        customize = True

        rect = pygame.Rect(312, 72, 100, 100)
        pygame.draw.rect(self.screen, blue, rect)
        smalltext = pygame.font.Font("freesansbold.ttf", 90)
        textsurface = smalltext.render("RACE TRACKS", True, orange)
        textRect = rect

        previousImageButton = pygame.image.load("Buttons/previousButton.png")
        prevRect = pygame.Rect(65, 312, previousImageButton.get_width(), previousImageButton.get_height())

        nextImageButton = pygame.image.load("Buttons/nextButton.png")
        nextRect = pygame.Rect(1135, 312, nextImageButton.get_width(), nextImageButton.get_height())

        backButton = Button(self.screen, "BACK", 100, 575, 100, 50, black, lightBlack, orange)
        selectButton = Button(self.screen, "SELECT", 1100, 575, 100, 50, black, lightBlack, orange)

        trackImg0 = pygame.image.load(self.tracks[0])
        trackImg1 = pygame.image.load(self.tracks[1])
        trackImg2 = pygame.image.load(self.tracks[2])
        trackImg3 = pygame.image.load(self.tracks[3])
        # trackImg4 = pygame.image.load(self.tracks[4])
        # trackImg5 = pygame.image.load(self.tracks[5])
        # trackImg6 = pygame.image.load(self.tracks[6])
        # trackImg7 = pygame.image.load(self.tracks[7])
        # trackImg8 = pygame.image.load(self.tracks[8])
        # trackImg9 = pygame.image.load(self.tracks[9])

        while customize:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    if prevRect.collidepoint(mouse):
                        self.previousTrack()

                    elif nextRect.collidepoint(mouse):
                        self.nextTrack()

                    elif backButton.rect.collidepoint(mouse):
                        action = "menu"
                        return action

                    elif selectButton.rect.collidepoint(mouse):
                        action = "select"
                        self.playerTrack = self.currentTrack
                        print ("Player Track: " + str(self.playerTrack))
                        return action

            self.screen.blit(self.img, (0, 0))
            self.screen.blit(textsurface, textRect)

            mouse = pygame.mouse.get_pos()

            self.screen.blit(previousImageButton, prevRect)
            self.screen.blit(nextImageButton, nextRect)

            backButton.setButtonStatus(mouse)
            selectButton.setButtonStatus(mouse)

            # below lines blits the track in centre of screen
            if self.currentTrack == 0:
                self.screen.blit(trackImg0, (((self.width / 2) - trackImg0.get_rect().width / 2), ((self.height / 2) - trackImg0.get_rect().height / 2)))

            elif self.currentTrack == 1:
                self.screen.blit(trackImg1, (((self.width / 2) - trackImg1.get_rect().width / 2), ((self.height / 2) - trackImg1.get_rect().height / 2)))

            elif self.currentTrack == 2:
                self.screen.blit(trackImg2, (((self.width / 2) - trackImg2.get_rect().width / 2), ((self.height / 2) - trackImg2.get_rect().height / 2)))

            elif self.currentTrack == 3:
                self.screen.blit(trackImg3, (((self.width / 2) - trackImg3.get_rect().width / 2), ((self.height / 2) - trackImg3.get_rect().height / 2)))

            # elif self.currentTrack == 4:
            #     self.screen.blit(trackImg4, (((self.width / 2) - trackImg4.get_rect().width / 2), ((self.height / 2) - trackImg4.get_rect().height / 2)))
            # 
            # elif self.currentTrack == 5:
            #     self.screen.blit(trackImg5, (((self.width / 2) - trackImg5.get_rect().width / 2), ((self.height / 2) - trackImg5.get_rect().height / 2)))
            # 
            # elif self.currentTrack == 6:
            #     self.screen.blit(trackImg6, (((self.width / 2) - trackImg6.get_rect().width / 2), ((self.height / 2) - trackImg6.get_rect().height / 2)))
            # 
            # elif self.currentTrack == 7:
            #     self.screen.blit(trackImg7, (((self.width / 2) - trackImg7.get_rect().width / 2), ((self.height / 2) - trackImg7.get_rect().height / 2)))
            # 
            # elif self.currentTrack == 8:
            #     self.screen.blit(trackImg8, (((self.width / 2) - trackImg8.get_rect().width / 2), ((self.height / 2) - trackImg8.get_rect().height / 2)))
            # 
            # elif self.currentTrack == 9:
            #     self.screen.blit(trackImg9, (((self.width / 2) - trackImg9.get_rect().width / 2), ((self.height / 2) - trackImg9.get_rect().height / 2)))

            pygame.display.update()













