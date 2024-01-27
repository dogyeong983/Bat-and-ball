import pygame
from pygame.locals import * 
import sys
import random
import math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((160, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
        self.pos = vec((WIDTH/2, HEIGHT-50))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    
    def move(self):
        self.acc = vec(0,0)
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC   
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH - 80:
            self.pos.x = WIDTH- 80
        if self.pos.x < 80:
            self.pos.x = 80
            
        self.rect.center = self.pos

class Box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((80, 40))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (100, 100))

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((15, 15))
        self.surf.fill((0,0,255))
        self.rect = self.surf.get_rect()
        self.pos = vec((WIDTH/2, HEIGHT-100)) 
        self.ang = random.randint(181, 359)
        self.rad = 0

    def move(self): 
        self.rad = math.pi * (self.ang / 180)
        self.pos.x += 10*math.cos(self.rad)
        self.pos.y += 10*math.sin(self.rad)
        if self.pos.x >= WIDTH:
            self.pos.x = WIDTH
            self.ang = 180-self.ang
        if self.pos.x <= 0:
            self.pos.x = 0
            self.ang = 180 - self.ang 
        if self.pos.y <= 0:
            self.ang = -self.ang     
        hits = pygame.sprite.spritecollide(PB ,Controller, False)
        if hits:
            self.pos.y = 720
            self.ang = -self.ang  
        self.rect.center = self.pos 

pygame.init()
vec = pygame.math.Vector2

HEIGHT = 800
WIDTH = 1000 
FPS = 30
ACC = 0.5
FRIC = -0.06
FramePerSec = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game") 

PT1 = Box()
P1 = Player()
PB = Ball()
Block = pygame.sprite.Group()
Block.add(PT1)
Controller = pygame.sprite.Group()
Controller.add(P1)
Ball_object = pygame.sprite.Group()
Ball_object.add(PB)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    screen.fill((0,0,0))
    
    for entity in Block:
        screen.blit(entity.surf, entity.rect)
    for entity in Controller:
        screen.blit(entity.surf, entity.rect)
    for entity in Ball_object:
        screen.blit(entity.surf, entity.rect)    
    P1.move()
    PB.move()
    pygame.display.update()
    FramePerSec.tick(FPS)
