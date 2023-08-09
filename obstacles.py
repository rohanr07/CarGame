#RohanRenganathan

import pygame
import random

# class to display obstacles on the race track
class Obstacles:
    # initializing constructor to display obstacles
    def __init__(self, obstacleNumber, displayWidth, displayHeight, screen):

        # each obstacle speed will vary randomly
        self.obstacleSpeed = random.randrange(0, 4)
        self.obstacleNumber = obstacleNumber
        self.obstacle = random.randrange(0, 8)

        # initializing where the obstacle will from
        self.obstacleStartx = random.randrange(200, (displayWidth - 200))
        self.obstacleStarty = random.randrange(0, displayHeight)
        self.rect = pygame.Rect(self.obstacleStartx, self.obstacleStarty, displayWidth, displayHeight)
        self.obstacleWidth = 56
        self.obstacleHeight = 125
        self.screen = screen
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.score = 0  #stores number of obstacles passed

        # only active for first time when player begins race
        self.gameStart = True

        # boolean flag for player car to pass the obstacle car 1 time
        self.obstaclePassed = True

    # random selection of the obstacles
    def uniqueObstacle(self):
        if self.obstacleNumber == 1:
            obstacle = random.randrange(0, 1)

        elif self.obstacleNumber == 2:
            obstacle = random.randrange(2, 3)

        elif self.obstacleNumber == 3:
            obstacle = random.randrange(4, 5)

        elif self.obstacleNumber == 4:
            obstacle = random.randrange(6, 7)

        elif self.obstacleNumber == 5:
            obstacle = random.randrange(8)

        return obstacle


    # function for the other vehicles on the track
    def obstacleFunc(self, obstacle):
        if obstacle == 0:
            obstaclePic = pygame.image.load("Obstacles/Obstacle1.png")
            self.obstacleWidth = 43
            self.obstacleHeight = 96

        elif obstacle == 1:
            obstaclePic = pygame.image.load("Obstacles/Obstacle2.png")
            self.obstacleWidth = 43
            self.obstacleHeight = 96

        elif obstacle == 2:
            obstaclePic = pygame.image.load("Obstacles/Obstacle3.png")
            self.obstacleWidth = 46
            self.obstacleHeight = 80

        elif obstacle == 3:
            obstaclePic = pygame.image.load("Obstacles/Obstacle4.png")
            self.obstacleWidth = 40
            self.obstacleHeight = 89

        elif obstacle == 4:
            obstaclePic = pygame.image.load("Obstacles/Obstacle5.png")
            self.obstacleWidth = 40
            self.obstacleHeight = 89

        elif obstacle == 5:
            obstaclePic = pygame.image.load("Obstacles/Obstacle6.png")
            self.obstacleWidth = 41
            self.obstacleHeight = 86

        elif obstacle == 6:
            obstaclePic = pygame.image.load("Obstacles/Obstacle7.png")
            self.obstacleWidth = 38
            self.obstacleHeight = 87

        elif obstacle == 7:
            obstaclePic = pygame.image.load("Obstacles/Obstacle8.png")
            self.obstacleWidth = 43
            self.obstacleHeight = 96

        elif obstacle == 8:
            obstaclePic = pygame.image.load("Obstacles/Obstacle9.png")
            self.obstacleWidth = 43
            self.obstacleHeight = 97

        else :
            obstaclePic = pygame.image.load("Obstacles/Obstacle7.png")
            self.obstacleWidth = 38
            self.obstacleHeight = 87

        if self.gameStart:
            self.gameStart = False  #set to false after once obstacles are blit
            self.obstacleStartx = random.randrange(112, (self.displayWidth - 175))  #starts blitting obstacles from random x position
            self.obstacleStarty = 0

        self.rect = pygame.Rect(self.obstacleStartx, self.obstacleStarty, self.displayWidth, self.displayHeight)

        self.screen.blit(obstaclePic, self.rect)

    # function changes speed of obstacles on screen
    def drawObstacles(self, playerPositionY, playerCarHeight):
        # the moving background speed will be equal to the speed of the obstacles

        self.obstacleStarty -= (self.obstacleSpeed / 4)
        self.obstacleFunc(self.obstacle)
        self.obstacleStarty += self.obstacleSpeed

        # when obstacle reaches end of vertical screen display new obstacle will blit
        if self.obstacleStarty > self.displayHeight:
            self.obstacleStarty = 0 - self.obstacleHeight
            self.obstacleStartx = random.randrange(112, (self.displayWidth - 170)) # 170 is the width of the grass
            self.obstacle = self.uniqueObstacle()
            self.obstaclePassed = True

        # check if obstacle has passed player's car and increment score
        if (self.obstacleStarty > (playerPositionY + playerCarHeight)) and self.obstaclePassed:
            self.score += 1
            self.obstaclePassed = False


