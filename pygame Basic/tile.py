import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
       # self.image=pygame.image.load("assets/floor.png").convert_alpha()
        self.image=pygame.Surface((size,size)).convert_alpha()
        self.image.fill("black")
        self.rect=self.image.get_rect(bottomleft=pos)

    def update(self,x_shift):
        self.rect.x+=x_shift    