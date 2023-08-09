#RohanRenganathan

import pygame

class Player:
    # initializing attributes for the player's car
    def __init__(self, carImg, x, y, width, height):
        self.img = pygame.image.load(carImg)
        # Keys representing Left Down Right Up
        self.keys =[False, False, False, False]
        self.speed = 5
        self.carWidth = width
        self.carHeight = height
        self.rect = pygame.Rect(x, y, self.carWidth, self.carHeight)

    # draws the image of the player's car on the screen
    def draw(self, screen):
        screen.blit(self.img, self.rect)

    # capture relevant keys and store them in list
    def captureKeys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.keys[0] = True  # LEFT -> True

            elif event.key == pygame.K_DOWN:
                self.keys[1] = True  # DOWN -> True

            elif event.key == pygame.K_RIGHT:
                self.keys[2] = True  # RIGHT -> True

            elif event.key == pygame.K_UP:
                self.keys[3] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.keys[0] = False  # LEFT -> True

            elif event.key == pygame.K_DOWN:
                self.keys[1] = False  # DOWN -> True

            elif event.key == pygame.K_RIGHT:
                self.keys[2] = False  # RIGHT -> True

            elif event.key == pygame.K_UP:
                self.keys[3] = False

    # player car will move depending on the key pressed
    def move(self):
        # LEFT - RIGHT
        if self.keys[0]:
            self.rect.x -= self.speed

            # restricts the movement until left boundary
            if self.rect.x < 129:
                self.rect.x = 129

        elif self.keys[2]:
            self.rect.x += self.speed

            # restricts the movement until right boundary
            if self.rect.x > 1135:
                self.rect.x = 1135

        # DOWN - UP
        if self.keys[1]:
            self.rect.y += self.speed

            # restricts the movement up to top of screen
            if self.rect.y > 558:
                self.rect.y = 558

        elif self.keys[3]:
            self.rect.y -= self.speed

            #restricts the movement at bottom of screen
            if self.rect.y < 0:
                self.rect.y = 0






