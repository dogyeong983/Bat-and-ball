import pygame
from pygame.locals import * 
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((120, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((HEIGHT/2, 385))
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
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
            
        self.rect.midbottom = self.pos

class Box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((40, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (30, 30))

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((15, 15))
        self.surf.fill((0,0,255))
        self.rect = self.surf.get_rect(center = (HEIGHT/2, 360))
        

pygame.init()
vec = pygame.math.Vector2

HEIGHT = 500
WIDTH = 500 
FPS = 60
ACC = 0.5
FRIC = -0.12
FramePerSec = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game") 

PT1 = Box()
P1 = Player()
PB = Ball()
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
all_sprites.add(PB)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    screen.fill((0,0,0))
    
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    P1.move()
    pygame.display.update()
    FramePerSec.tick(FPS)
