import pygame
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos,lookright):
        super().__init__()
        self.image=pygame.image.load("assets/player/axe/3.png")
        self.image=pygame.transform.scale(self.image,(32,32))
        self.lookright=lookright
        self.rect=self.image.get_rect(bottomleft=(pos))

    def shoot(self):
        if self.lookright==True:
            self.rect.x+=2*5
        else:
            self.rect.x-=2*5
       
    def update(self):
        self.shoot()
