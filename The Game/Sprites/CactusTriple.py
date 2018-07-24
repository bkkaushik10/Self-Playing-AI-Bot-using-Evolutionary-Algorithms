import pygame
class CactusTriple(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y, 51, 30)
        self.imageName = "Sprites/GameImages/tripleCactus.png"

    def drawCharacter(self, canvas):
        canvas.blit(pygame.image.load(self.imageName), (self.x,self.y))
        self.hitbox = (self.x + 3, self.y + 3, 45, 30)
        #pygame.draw.rect(canvas, (255, 0, 0), self.hitbox, 2)

    def propagate(self, step):
        self.x -= step
