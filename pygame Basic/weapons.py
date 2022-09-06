import pygame

class Weapons(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image=pygame.image.load("assets/player/gun/gun.PNG").convert_alpha()
        self.image=pygame.transform.scale(self.image,(size,size)).convert_alpha()
        self.rect=self.image.get_rect(bottomleft=pos)

    def update(self,worldshift,player_rect,weapon_rect):
        if player_rect != weapon_rect:
            self.rect.x+=worldshift