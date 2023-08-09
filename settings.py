# RohanRenganathan

import pygame
import sys

from Buttons.button import Button

black = (0, 0, 0)
blue = (0, 0, 200)
brightBlue = (0, 0, 255)
orange = (255, 128, 0)
lime = (156, 186, 33)
lightBlack = (50, 50, 50)


# class for settings button of game
class Settings:
    # initializing constructor for settings screen
    def __init__(self, screen, musicOnOff):
        self.screen = screen
        self.musicOnOff = musicOnOff
        self.img = pygame.image.load("BackgroundImages/Background3.png")

    def draw(self):
        settings = True

        rect = pygame.Rect(375, 72, 100, 100)
        pygame.draw.rect(self.screen, blue, rect)
        smalltext = pygame.font.Font("freesansbold.ttf", 90)
        textsurface = smalltext.render("Game Controls", True, orange)
        textRect = rect

        customizeCarButton = Button(self.screen, "Customise Car", 550, 200, 250, 50, black, lightBlack, lime)
        customizeTrackButton = Button(self.screen, "Customise Track", 550, 300, 250, 50, black, lightBlack, lime)
        musicButton = Button(self.screen, "Music On/Off", 550, 400, 250, 50, black, lightBlack, lime)
        modeButton = Button(self.screen, "Game Mode", 550, 500, 250, 50, lightBlack, lightBlack, lime)
        backButton = Button(self.screen, "BACK", 100, 575, 100, 50, black, lightBlack, orange)

        while settings:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if customizeCarButton.rect.collidepoint(mouse):
                        action = "customizeCar"
                        return action

                    elif customizeTrackButton.rect.collidepoint(mouse):
                        action = "customizeTrack"
                        return action

                    elif backButton.rect.collidepoint(mouse):
                        action = "menu"
                        return action

                    elif musicButton.rect.collidepoint(mouse):
                        musicButton.toggleButtonText()

                        # pauses and unpauses music based on boolean flag
                        if not self.musicOnOff:
                            self.musicOnOff = True

                            if not pygame.mixer.music.get_busy():
                                pygame.mixer.music.play(-1)     # -1 means music will play in loop
                            else:
                                pygame.mixer.music.unpause()

                        else:
                            self.musicOnOff = False
                            pygame.mixer.music.pause()

            self.screen.blit(self.img, (0, 0))
            self.screen.blit(textsurface, textRect)

            mouse = pygame.mouse.get_pos()
            customizeCarButton.setButtonStatus(mouse)
            customizeTrackButton.setButtonStatus(mouse)
            musicButton.setButtonStatus(mouse)
            modeButton.setButtonStatus(mouse)
            backButton.setButtonStatus(mouse)

            pygame.display.update()
