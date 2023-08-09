# RohanRenganathan

import sys
import pygame
import time

from gamebackground import gameBackground
from player import Player
from obstacles import Obstacles
from customisecar import CustomiseCar
from customisetrack import CustomiseTrack
from street import Street
from settings import Settings

pygame.init()

grass = pygame.image.load("Street/Grass.png")
strip = pygame.image.load("Street/strip.png")

# makes the size of the screen dynamic (will change according to user's size of screen)
# displaySize = pygame.display.Info()
# gameDisplays = pygame.display.set_mode((displaySize.current_w, displaySize.current_h))


# initilaising the size of the display for the game
displayWidth = 1300
displayHeight = 660

# colours
black = (0, 0, 0)
lightBlack = (50, 50, 50)
white = (255, 255, 255)
red = (200, 0, 0)
blue = (0, 0, 200)
green = (0, 200, 0)
brightRed = (255, 0, 0)
brightBlue = (0, 0, 255)
turquoise = (0, 102, 102)
brightGreen = (0, 255, 0)
orange = (255, 128, 0)
lime = (156, 186, 33)
darkLime = (107, 129, 19)
darkYellow = (185, 185, 0)
gray = (128, 128, 128)

musicOnOff = False  # boolean flag to represent if music is on / off during game
pygame.mixer.music.load("Music/BackgroundMusic2.mp3")

if musicOnOff:
    pygame.mixer.music.play(-1)

smallText = pygame.font.Font("freesansbold.ttf", 20)
mediumText = pygame.font.Font("freesansbold.ttf", 40)
largeText = pygame.font.Font("freesansbold.ttf", 80)

gameDisplays = pygame.display.set_mode((displayWidth, displayHeight))
customCars = CustomiseCar(gameDisplays)
customTracks = CustomiseTrack(gameDisplays)

# storing all images of cars for player to choose from
playerGarage = ["PlayerCars/playerCar1.png", "PlayerCars/playerCar2.png", "PlayerCars/playerCar3.png",
                "PlayerCars/playerCar4.png", "PlayerCars/playerCar5.png", "PlayerCars/playerCar6.png",
                "PlayerCars/playerCar7.png", "PlayerCars/playerCar8.png", "PlayerCars/playerCar9.png",
                "PlayerCars/playerCar10.png"]

# storing all images of race tracks for player to choose from
gameTracks = ["Street/lineWhite.png", "Street/linePink.png", "Street/lineBlue.png", "Street/lineGreen.png"]
gameBkGround = [black, turquoise, darkYellow, gray]

pygame.display.set_caption("DASH & DODGE")
clock = pygame.time.Clock()

playerCarImg = pygame.image.load(playerGarage[customCars.playerCar])

# images for the background of the game
introBackground = pygame.image.load("BackgroundImages/Background1.png")
instructionBackground = pygame.image.load("BackgroundImages/Background2.png")
settingsBackground = pygame.image.load("BackgroundImages/Background3.png")


# boolean value set to True when the player presses the pause button
pause = False


# pauses and unpauses music based on boolean flag
def musicToggle():
    global musicOnOff

    if not musicOnOff:
        musicOnOff = True

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)     # -1 means music will play in loop
        else:
            pygame.mixer.music.unpause()

    else:
        musicOnOff = False
        pygame.mixer.music.pause()



# function for the home page of the game
def homeScreenLoop():
    intro = True

    settingsButton = pygame.image.load("Buttons/settingsButton.png")
    startButton = pygame.image.load("Buttons/startButton.png")
    instructionsButton = pygame.image.load("Buttons/instructionsButton.png")
    quitButton = pygame.image.load("Buttons/quitButton.png")
    signaturePic = pygame.image.load("signature.png")

    settingsButtonRect = pygame.Rect(250, 587, settingsButton.get_width(), settingsButton.get_height())
    startButtonRect = pygame.Rect(450, 587, startButton.get_width(), startButton.get_height())
    instructionsButtonRect = pygame.Rect(650, 587, instructionsButton.get_width(), instructionsButton.get_height())
    quitButtonRect = pygame.Rect(850, 587, quitButton.get_width(), quitButton.get_height())
    signaturePicRect = pygame.Rect(1127, 607, signaturePic.get_width(), signaturePic.get_height())


    while intro:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if settingsButtonRect.collidepoint(mouse):
                    settings()

                elif instructionsButtonRect.collidepoint(mouse):
                    instructions()

                elif startButtonRect.collidepoint(mouse):
                    countdown()

                elif quitButtonRect.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

            # display game name on home screen
            gameDisplays.blit(introBackground, (0, 0))
            largeText = pygame.font.Font("freesansbold.ttf", 120)
            textSurf, textRect = textObjects("DASH & DODGE", largeText, orange)
            textRect.center = (650, 100)
            gameDisplays.blit(textSurf, textRect)

        gameDisplays.blit(settingsButton, settingsButtonRect)
        gameDisplays.blit(instructionsButton, instructionsButtonRect)
        gameDisplays.blit(startButton, startButtonRect)
        gameDisplays.blit(quitButton, quitButtonRect)
        gameDisplays.blit(signaturePic, signaturePicRect)


        # all the buttons on the home screen of game
        #button("SETTINGS", 173, 599, 175, 50, turquoise, brightTurquoise, "settings")
        #button("START", 432, 598, 100, 50, green, brightGreen, "play")
        #button("INSTRUCTIONS", 550, 598, 200, 50, blue, brightBlue, "intro")
        #button("QUIT", 800, 598, 100, 50, red, brightRed, "quit")
        pygame.display.update()
        clock.tick(50)

# function to create button object
def button(msg, x, y, buttonWidth, buttonHeight, inactiveColour, activeColour, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(gameDisplays, inactiveColour, (x, y, buttonWidth, buttonHeight))

    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = textObjects(msg, smalltext, orange)
    textRect.center = ((x + (buttonWidth / 2)), (y + (buttonHeight / 2)))
    gameDisplays.blit(textSurf, textRect)

    if x + buttonWidth > mouse[0] > x and y + buttonHeight > mouse[1] > y:
        if (click[0] == 1) and (action != None):
            if action == "settings":
                settings()

            elif action == "play":
                countdown()

            elif action == "intro":
                instructions()

            elif action == "menu":
                homeScreenLoop()

            elif action == "pause":
                paused()

            elif action == "unpause":
                unpaused()

            elif action == "quit":
                pygame.quit()
                sys.exit()

        else:
            pygame.draw.rect(gameDisplays, activeColour, (x, y, buttonWidth, buttonHeight))
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = textObjects(msg, smalltext, orange)
        textRect.center = ((x + (buttonWidth / 2)), (y + (buttonHeight / 2)))
        gameDisplays.blit(textSurf, textRect)

# function for instructions of the game
def instructions():
    instructions = True
    while instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplays.blit(instructionBackground, (0, 0))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        mediumText = pygame.font.Font("freesansbold.ttf", 40)
        largeText = pygame.font.Font("freesansbold.ttf", 80)

        textSurf, textRect = textObjects("INSTRUCTIONS", largeText, orange)
        textRect.center = ((632), (100))

        gameDisplays.blit(textSurf, textRect)

        cTextSurf, cTextRect = textObjects("CONTROLS", mediumText, darkLime)
        cTextRect.center = ((165), (195))

        pTextSurf, pTextRect = textObjects("BUTTON P: PAUSE", smallText, lime)
        pTextRect.midleft = ((32), (268))

        mTextSurf, mTextRect = textObjects("BUTTON M: MUSIC", smallText, lime)
        mTextRect.midleft = ((32), (321))

        rTextSurf, rTextRect = textObjects("ARROW RIGHT: MOVE RIGHT", smallText, lime)
        rTextRect.midleft = ((32), (374))

        lTextSurf, lTextRect = textObjects("ARROW LEFT: MOVE LEFT", smallText, lime)
        lTextRect.midleft = ((32), (427))

        fTextSurf, fTextRect = textObjects("ARROW FORWARD: ACCELERATOR", smallText, lime)
        fTextRect.midleft = ((32), (480))

        bTextSurf, bTextRect = textObjects("ARROW BACKWARD: BRAKE", smallText, lime)
        bTextRect.midleft = ((32), (533))

        aogTextSurf, aogTextRect = textObjects("Aim of Game", mediumText, darkLime)
        aogTextRect.center = ((832), (185))

        ioTextSurf, ioTextRect = textObjects("* This is a car game in which you need to avoid the incoming obstacles *", smallText, lime)
        ioTextRect.midleft = ((458), (265))

        psTextSurf, psTextRect = textObjects("* As you pass an obstacle you score a point and the higher the score the faster it gets! *", smallText, lime)
        psTextRect.midleft = ((458), (318))

        ctTextSurf, ctTextRect = textObjects("* Car and Race Track can be customized on the Settings screen *", smallText, lime)
        ctTextRect.midleft = ((458), (371))

        bgmTextSurf, bgmTextRect = textObjects("* Background music can be turned On/Off on the Settings screen *", smallText, lime)
        bgmTextRect.midleft = ((458), (424))

        spTextSurf, spTextRect = textObjects("* Game Mode currently only avaliable as Single Player *", smallText, lime)
        spTextRect.midleft = ((458), (477))

        gameDisplays.blit(cTextSurf, cTextRect)
        gameDisplays.blit(pTextSurf, pTextRect)
        gameDisplays.blit(mTextSurf, mTextRect)
        gameDisplays.blit(rTextSurf, rTextRect)
        gameDisplays.blit(lTextSurf, lTextRect)
        gameDisplays.blit(fTextSurf, fTextRect)
        gameDisplays.blit(bTextSurf, bTextRect)
        gameDisplays.blit(aogTextSurf, aogTextRect)
        gameDisplays.blit(ioTextSurf, ioTextRect)
        gameDisplays.blit(psTextSurf, psTextRect)
        gameDisplays.blit(ctTextSurf, ctTextRect)
        gameDisplays.blit(bgmTextSurf, bgmTextRect)
        gameDisplays.blit(bgmTextSurf, bgmTextRect)
        gameDisplays.blit(spTextSurf, spTextRect)

        button("BACK", 100, 575, 100, 50, black, lightBlack, "menu")
        pygame.display.update()
        clock.tick(30)


# function for when the player pauses the game
def paused():
    global pause
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        largeText = pygame.font.Font("freesansbold.ttf", 132)
        TextSurf, TextRect = textObjects("PAUSED", largeText, orange)
        TextRect.center = ((displayWidth / 2), 120)
        gameDisplays.blit(TextSurf, TextRect)
        button("Continue", 357, 450, 150, 50, green, brightGreen, "unpause")
        button("Restart", 557, 450, 150, 50, blue, brightBlue, "play")
        button("Main Menu", 757, 450, 200, 50, red, brightRed, "menu")
        pygame.display.update()
        clock.tick(30)


# function when the player unpauses the game
def unpaused():
    global pause
    pause = False


# function for the background of the countdown
def countdownBackground():
    #font = pygame.font.SysFont(None, 25)
    x = (displayWidth * 0.45)
    y = (displayHeight * 0.8)

    gameDisplays.blit(grass, (0, 0))
    gameDisplays.blit(grass, (0, 200))
    gameDisplays.blit(grass, (0, 400))
    gameDisplays.blit(grass, (1197, 0))
    gameDisplays.blit(grass, (1197, 200))
    gameDisplays.blit(grass, (1197, 400))

    gameDisplays.blit(strip, (120, 200))
    gameDisplays.blit(strip, (120, 0))
    gameDisplays.blit(strip, (120, 100))
    gameDisplays.blit(strip, (1180, 100))

    gameDisplays.blit(strip, (1180, 0))
    gameDisplays.blit(strip, (1180, 200))

    gameDisplays.blit(playerCarImg, (x, y))


# function for the countdown before the race begins
def countdown():
    countdown = True

    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplays.fill(gameBkGround[customTracks.playerTrack])
        countdownBackground()
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        textSurf, textRect = textObjects("3", largeText, orange)
        textRect.center = ((displayWidth / 2), (displayHeight / 2))

        gameDisplays.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(1)
        gameDisplays.fill(gameBkGround[customTracks.playerTrack])
        countdownBackground()

        largeText = pygame.font.Font("freesansbold.ttf", 115)
        textSurf, textRect = textObjects("2", largeText, orange)
        textRect.center = ((displayWidth / 2), (displayHeight / 2))
        gameDisplays.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(1)
        gameDisplays.fill(gameBkGround[customTracks.playerTrack])
        countdownBackground()

        largeText = pygame.font.Font("freesansbold.ttf", 115)
        textSurf, textRect = textObjects("1", largeText, orange)
        textRect.center = ((displayWidth / 2), (displayHeight / 2))
        gameDisplays.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(1)
        gameDisplays.fill(gameBkGround[customTracks.playerTrack])
        countdownBackground()

        largeText = pygame.font.Font("freesansbold.ttf", 115)
        textSurf, textRect = textObjects("GO!", largeText, orange)
        textRect.center = ((displayWidth / 2), (displayHeight / 2))
        gameDisplays.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(1)
        gameLoop()

# function for settings screen called from main menu
def settings():
    global musicOnOff

    setting = Settings(gameDisplays, musicOnOff)
    action = setting.draw()

    # if music is set to on
    if setting.musicOnOff:
        musicOnOff = True

    else:
        musicOnOff = False

    if action == "customizeCar":
        customizeCar()

    elif action == "customizeTrack":
        customizeTrack()
    
    elif action == "menu":
        homeScreenLoop()


# function for choosing car in Settings Menu
def customizeCar():
    global playerCarImg

    action = customCars.customization()

    if action == "menu":
        settings()

    elif action == "select":
        playerCarImg = pygame.image.load(playerGarage[customCars.playerCar])


# function for choosing track in Settings Menu
def customizeTrack():
    global playerTrackImg

    action = customTracks.customization()

    if action == "menu":
        settings()

    elif action == "select":
        playerTrackImg = pygame.image.load(gameTracks[customTracks.playerTrack])



# function for customize car was here

# def obstacleFunc was here


# displays the score on game screen
def scoreSystem(score):
    font = pygame.font.SysFont(None, 25)
    score = font.render("Score " + str(score), True, white)
    gameDisplays.blit(score, (0, 30))


# checks if current score > maximum score and writes to file if True
def setMaximumScore():
    if totalScore > maxScore:
        filePointer2 = open("MaximumScore.txt", "w")
        filePointer2.write(str(totalScore))
        filePointer2.close()


# displays maximum score string on game screen
def getMaximumScore():
    font = pygame.font.SysFont(None, 25)
    highestScore = font.render("Max Score " + str(maxScore), True, white)
    gameDisplays.blit(highestScore, (0, 60))

# creates a text object and returns text
def textObjects(text, font, textColour):
    textsurface = font.render(text, True, textColour)
    return textsurface, textsurface.get_rect()


# function displaying a message when the user crashes the car
def messageDisplay(text):
    largeText = pygame.font.Font("freesansbold.ttf", 80)
    textsurface, textrect = textObjects(text, largeText, orange)
    textrect.center = ((displayWidth / 2), (displayHeight / 2))
    gameDisplays.blit(textsurface, textrect)
    pygame.display.update()
    time.sleep(3)
    gameLoop()


# function called when the user crashes the car
def crash():
    messageDisplay("YOU CRASHED")

# main loop for race track screen of game
def gameLoop():
    global pause

    timeToBlitObstacles = 0
    global totalScore
    global maxScore
    totalScore = 0

    # read maximum score from file and store in global variable
    filePointer = open("MaximumScore.txt", "r")
    maxScore = int(filePointer.readline())
    filePointer.close()

    background = gameBackground(gameTracks[customTracks.playerTrack])
    street = Street(gameTracks[customTracks.playerTrack])

    # creates 5 obstacles to display on the race track
    obstacles1 = Obstacles(1, displayWidth, displayHeight, gameDisplays)
    obstacles2 = Obstacles(2, displayWidth, displayHeight, gameDisplays)
    obstacles3 = Obstacles(3, displayWidth, displayHeight, gameDisplays)
    obstacles4 = Obstacles(4, displayWidth, displayHeight, gameDisplays)
    obstacles5 = Obstacles(5, displayWidth, displayHeight, gameDisplays)

    x = (displayWidth * 0.45)
    y = (displayHeight * 0.8)

    player = Player(playerGarage[customCars.playerCar], x, y, 50, 50)

    # function to increase speed of player's car, obstacles and lanes on race track
    def increaseSpeed(speed):
        player.speed += speed
        obstacles1.obstacleSpeed += speed
        obstacles2.obstacleSpeed += speed
        obstacles3.obstacleSpeed += speed
        obstacles4.obstacleSpeed += speed
        obstacles5.obstacleSpeed += speed
        street.speed += speed

    # moving the car along the x & y - axis
    xChange = 0

    crashed = False

    level1 = True
    level2 = True
    level3 = True
    level4 = True
    level5 = True
    level6 = True
    level7 = True
    level8 = True

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                setMaximumScore()
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    paused()

                elif event.key == pygame.K_m:
                    musicToggle()


            # checks what key the user presses and moves the car accordingly
            player.captureKeys(event)
        player.move()

        x += xChange

        pause = True

        gameDisplays.fill(gameBkGround[customTracks.playerTrack])

        background.drawBackground(gameDisplays)

        street.draw(gameDisplays)
        player.draw(gameDisplays)

        if timeToBlitObstacles >= 2000:
            obstacles1.drawObstacles(player.rect.y, player.carHeight)
            obstacles2.drawObstacles(player.rect.y, player.carHeight)
            obstacles3.drawObstacles(player.rect.y, player.carHeight)
            obstacles4.drawObstacles(player.rect.y, player.carHeight)
            obstacles5.drawObstacles(player.rect.y, player.carHeight)


            totalScore = obstacles1.score + obstacles2.score + obstacles3.score + obstacles4.score + obstacles5.score

            if (5 < totalScore <= 11) and level1:
                level1 = False
                increaseSpeed(2)

            elif (12 < totalScore <= 21) and level2:
                level2 = False
                increaseSpeed(2)

            elif (22 < totalScore <= 35) and level3:
                level3 = False
                increaseSpeed(3)

            elif (36 < totalScore <= 45) and level4:
                level4 = False
                increaseSpeed(2)

            elif (45 < totalScore <= 52) and level5:
                level5 = False
                increaseSpeed(2)

            elif (53 < totalScore <= 64) and level6:
                level6 = False
                increaseSpeed(3)

            elif (65 < totalScore <= 78) and level7:
                level7 = False
                increaseSpeed(2)

            elif (79 < totalScore <= 92) and level8:
                level8 = False
                increaseSpeed(2)

            # detects collision for any of the 5 obstacles
            collide1 = pygame.Rect(player.rect.x, player.rect.y, 40, 60).colliderect(pygame.Rect(obstacles1.obstacleStartx, obstacles1.obstacleStarty, 40, 60))
            collide2 = pygame.Rect(player.rect.x, player.rect.y, 40, 60).colliderect(pygame.Rect(obstacles2.obstacleStartx, obstacles2.obstacleStarty, 40, 60))
            collide3 = pygame.Rect(player.rect.x, player.rect.y, 40, 60).colliderect(pygame.Rect(obstacles3.obstacleStartx, obstacles3.obstacleStarty, 40, 60))
            collide4 = pygame.Rect(player.rect.x, player.rect.y, 40, 60).colliderect(pygame.Rect(obstacles4.obstacleStartx, obstacles4.obstacleStarty, 40, 60))
            collide5 = pygame.Rect(player.rect.x, player.rect.y, 40, 60).colliderect(pygame.Rect(obstacles5.obstacleStartx, obstacles5.obstacleStarty, 40, 60))

            scoreSystem(totalScore)
            getMaximumScore()

            if collide1 or collide2 or collide3 or collide4 or collide5:
                setMaximumScore()
                crash()

        else:
            scoreSystem(totalScore)
            getMaximumScore()
            timeToBlitObstacles += 8

        button("Pause", 1186, 0, 115, 50, black, lightBlack, "pause")

        pygame.display.update()
        clock.tick(60)


homeScreenLoop()
gameLoop()
pygame.quit()




# Things need to be included
# Introduce other obstacles (e.g. boulders)
# THINK OF CAR GAME NAME
# Change font of DASH & DODGE ON HOME SCREEN
# Incorporate flag 🏁 into game
# Add home button 🏡 in top right corner of every screen (apart from racing screen)
# Obstacle speed should be less than (<) speed of game background (otherwise stuck at top of screen and no new obstacles will blit)
# Make buttons on home screen all same size and font size
# Make sure every picture from code in documentation has got enough comments
# Pause screen change multi colour button to normal colour (change picture from documentation as well)
