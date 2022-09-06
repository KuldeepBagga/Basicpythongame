from pickle import FALSE
import pygame
from settings import Screen_Height, Screen_Width
from support import import_folder
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,size,surface):
        super().__init__()
        self.display_surface=surface
        self.import_player_assets()
        self.frame_index=0
        self.amimation_speed=0.03
        self.status='idle'
        self.image=self.animations[self.status][self.frame_index]
        self.rect=self.image.get_rect(bottomleft=pos)
        self.pos=pos
        self.direction=pygame.math.Vector2()
        self.speed=10
        self.gravity=0.8
        self.jump_speed=-19
        self.jump_status=True
        self.lookright=False
        self.on_ground=True
        self.player_health()
        self.bullet_sprite=pygame.sprite.Group() 
        self.can_shoot=False
        self.shoot_counter=0

    def player_health(self):
        self.healthbar=pygame.Surface((100,15)).convert_alpha()
        self.healthbar.fill("green")
        self.health=self.healthbar.get_rect(topleft=(10,10))

    def import_player_assets(self):
        image_path="assets/player/"
        self.animations={'idle':[],'run':[]}
        for animations in self.animations.keys():
            full_path=image_path + animations
            self.animations[animations]=import_folder(full_path)

    def animate(self):
        animation=self.animations[self.status]

        self.frame_index+=self.amimation_speed

        if self.frame_index>=len(animation):
            self.frame_index=0
        image=animation[int(self.frame_index)]


        if self.lookright==True:
            self.image=image
        else:
            flipped_image=pygame.transform.flip(image,True,False)
            self.image=flipped_image

    def get_status(self):
        if self.direction.x!=0:
            self.status='run'
        else:
            self.status='idle'

    
    def get_input(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x=+1
            self.lookright=True
        elif keys[pygame.K_LEFT]:
            self.direction.x=-1
            self.lookright=False
        else:
            self.direction.x=0

        if keys[pygame.K_SPACE] and self.on_ground==True:
            self.on_ground=False
            self.jump()

        if keys[pygame.K_LCTRL] and self.can_shoot==True and self.shoot_counter==0:
            self.shoot()

    def shoot(self):
        if self.shoot_counter==0:
           self.shoot_counter=20
           self.bullet_sprite.add(Bullet(self.rect.center,self.lookright))

    def shoot_counters(self):
        if self.shoot_counter>0:
            self.shoot_counter-=1

    def apply_gravity(self):
        self.direction.y+=self.gravity
        self.rect.y+=self.direction.y

    def jump(self):
        self.direction.y=self.jump_speed

    def move(self):
        self.rect.x+=self.direction.x*self.speed
    
    def update(self):
        #player Input for left right movement
        self.get_input()
        #player direction update
        self.move()

        self.shoot_counters()
        
        self.bullet_sprite.draw(self.display_surface)
        
        self.bullet_sprite.update()

        self.display_surface.blit(self.healthbar,self.health)

        self.animate()
        self.get_status()

        
        
        