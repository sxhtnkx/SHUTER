import pygame
from data import *
from ulit import *

pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption(setting_win["NAME_GAME"])

def run():
    game =True
    create_wall("MAP1")
    clock = pygame.time.Clock()

    hero = Hero(5,5, hero4_image,hero2_image, hero3_image, hero5_image, speed = 5)
    bot1 = Bot(150,50, bot_image,bot_image,bot_image,bot_image,speed = 5)



    while game:
        window.fill((0,0,0)
        event = pygame.event.get()

        for wall in wall_list:
            window.blit(wall.IMAGE, (wall.x, wall.y))

        window.blit(hero.IMAGE, (hero.x, hero.y))
        hero.move()
        window.blit(bot1.IMAGE, (bot1.x, bot1.y))
        bot1.make_move()
    


        for event in events:
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = True
                elif event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = True
                elif event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = True
                elif event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = True
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = False
                elif event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = False
                elif event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = False
                elif event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = False


        
        
        

        clock.tick(setting_win["FPS"])
        pygame.display.flip()    


run()
        



