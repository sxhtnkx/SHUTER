import os
import pygame

setting_win = {
    "WIDTH": 1000,
    "HEIGHT": 700,
    "NAME_GAME": "Maze",
    "FPS": 60
}

maps = {
    "MAP1": [
                "00100000000000000000",
                "00000000000000000000",
                "00100000000000000100",
                "00000000000000000000",
                "00100000000000000100",
                "00000000000000000000",
                "00100000000000000100",
                "00000000000000000000",
                "00100000000000000100",
                "00000000000000000000",
                "00102020000000000100",
                "00203000000000000000",
                "00000000000000000000",
                "00000000000000000000",
                
            ]
}

wall_list = list()

abs_path = os.path.abspath(__file__ + '/..') + "\\image\\"

wall_image = pygame.image.load(abs_path + "wall.png")
hero_image = pygame.image.load(abs_path + "hero.png")
hero2_image = pygame.image.load(abs_path + "hero2.png")
hero3_image = pygame.image.load(abs_path + "hero3.png")
hero4_image = pygame.image.load(abs_path + "hero4.png")
hero5_image = pygame.image.load(abs_path + "hero5.png")
bot_image = pygame.image.load(abs_path + "bot.png")