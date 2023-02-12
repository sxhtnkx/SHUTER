import pygame
from data import *


class Wall(pygame.Rect):
    def __init__(self, x, y,image, width = 20, height = 100 ):
        super().__init__(x, y, width, height)
        self.IMAGE = image

class Sprite(pygame.Rect):
    def __init__(self,x,y,image1,image2,image3,image4,speed,width = 50,height = 50):
        super().__init__(x, y, width, height)
        self.SPEED = speed
        
        self.MOVE_IMAGE = 0
        self.IMAGE_MOVE_LIST = [image1,image2,image3,image4] 
    def moves(self,value,coff):
        if value % coff == 0:
            return 1
        return 0
        
        
    
                    

class Bot(Sprite):
    def __init__(self,x,y,image1,image2,image3,image4,speed,width = 50,height = 50):
        super().__init__(x,y,image1,image2,image3,image4,speed,width,height)
        self.IMAGE = image1
        self.SPEED = speed
        

    def make_move(self):
        self.y += self.SPEED
        if self.y > 500:
            self.SPEED *= -1
        elif self.y < 25:
            self.SPEED *= -1          

class Hero(Sprite):
    def __init__(self,x,y,image1,image2,image3,image4,speed,width = 50,height = 50):
        super().__init__(x,y,image1,image2,image3,image4,speed,width,height)
        self.IMAGE = image1
        self.MOVE = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}
    def move(self):
        if self.MOVE["UP"] and self.y > 0:            #РУХ ВВЕРХ
            self.y -= self.SPEED
            if self.collidelist(wall_list) != -1:
                self.y +=self.SPEED
            self.IMAGE = self.IMAGE_MOVE_LIST[0]
        elif self.MOVE["DOWN"] and self.y < setting_win["HEIGHT"]:
            self.y += self.SPEED
            if self.collidelist(wall_list) != -1:
                self.y -=self.SPEED
            self.IMAGE = self.IMAGE_MOVE_LIST[1]
        elif self.MOVE["LEFT"] and self.y > 0:
            self.x -= self.SPEED
            if self.collidelist(wall_list) != -1:
                self.x +=self.SPEED
            self.IMAGE = self.IMAGE_MOVE_LIST[2]
        elif self.MOVE["RIGHT"] and self.y < setting_win["WIDTH"]:
            self.x += self.SPEED
            if self.collidelist(wall_list) != -1:
                self.x -=self.SPEED
            self.IMAGE = self.IMAGE_MOVE_LIST[3]
def create_wall(present_map):
    x, y = 0, 0

    for string in maps[present_map]:
        for element in string:
            if element == "1":
                wall_list.append(Wall(x, y, wall_image))
            elif element == "2":
                wall_list.append(Wall(x, y, pygame.transform.rotate(wall_image, 90),width = 100, height = 20))
            x += 50
        x = 0
        y += 50






    