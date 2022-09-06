import pygame,sys
from level import Level
from settings import *
pygame.font.init()
clock=pygame.time.Clock()

if __name__ == "__main__":
    level=Level()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
   
        level.run()
        pygame.display.update()
        dt=clock.tick(60)
        