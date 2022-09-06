import pygame
from bullet import Bullet
from player import Player
from tile import Tile
from settings import Level_Map, Screen_Height, Screen_Width, Tile_Size
from weapons import Weapons

class Level:
    def __init__(self):
        self.display_screen=pygame.display.set_mode((Screen_Width,Screen_Height))
        self.display_surface=pygame.display.get_surface()
        self.tile_sprite=pygame.sprite.Group()
        self.weapon_sprite=pygame.sprite.Group()
        self.player_sprite=pygame.sprite.GroupSingle()
        self.weapon_sprite=pygame.sprite.Group()
        self.worldshift=0
        self.setup_level(Level_Map)
    
    def setup_level(self,Level_Map):
        for row_index,row in enumerate(Level_Map):
            for col_index , col in enumerate(row):
                x=col_index*Tile_Size
                y=row_index*Tile_Size

                if col=="p":
                    self.player=Player((x,y),Tile_Size,self.display_surface)
                    self.player_sprite.add(self.player)
                if col=="1":
                    self.tile=Tile((x,y),Tile_Size)
                    self.tile_sprite.add(self.tile)
                if col=="9":
                    self.weapons=Weapons((x,y),Tile_Size)
                    self.weapon_sprite.add(self.weapons)

    def get_upgrades(self):
        for weapons in self.weapon_sprite.sprites():
            if weapons.rect.colliderect(self.player_sprite.sprite.rect):
                self.player.rect=weapons.rect

                if self.player.rect==weapons.rect:
                    self.player.can_shoot=True
                

    def scroll_x(self):
        if self.player.rect.x<Screen_Width/4 and self.player.direction.x<0:
            self.worldshift=8
            self.player.speed=0
        elif self.player.rect.x>Screen_Width/4 and self.player.direction.x>0:
            self.worldshift=-8
            self.player.speed=0
        else:
            self.worldshift=0
            self.player.speed=10
    
    def horizontal_collission(self):
        for allsprite in self.tile_sprite.sprites():
            if allsprite.rect.colliderect(self.player.rect): 
                if self.player.direction.x < 0:
                    self.player.rect.left=allsprite.rect.right
                    self.player.direction.x=0
                elif self.player.direction.x > 0:
                    self.player.rect.right=allsprite.rect.left
                    self.player.direction.x=0
                   
    def vertical_collission(self):
        self.player.apply_gravity()

        for tile_sprite in self.tile_sprite.sprites():
            if tile_sprite.rect.colliderect(self.player.rect):    
                if self.player.direction.y >= 0:
                    self.player.rect.bottom=tile_sprite.rect.top
                    self.player.direction.y=0
                    self.player.on_ground=True
                elif self.player.direction.y < 0:
                    self.player.rect.top=tile_sprite.rect.bottom
                    self.player.direction.y=0
                    self.player.on_ground=False

    def run(self):
        
        self.display_surface.fill("grey")

        self.get_upgrades()

        #update all sprites (tiles)
        self.tile_sprite.update(self.worldshift)
        #update player sprite
        self.player_sprite.update()

        self.weapon_sprite.update(self.worldshift,self.player.rect,self.weapons.rect)

        #drawing all sprites (tiles)
        self.tile_sprite.draw(self.display_surface) 
        
        #horizontal collission player with ground and tiles
        self.horizontal_collission()
        
        #draw the player
        self.player_sprite.draw(self.display_surface)

        #vertical collission player with ground and tiles
        self.vertical_collission()

        self.weapon_sprite.draw(self.display_surface)

        self.scroll_x()

        
       
       


        