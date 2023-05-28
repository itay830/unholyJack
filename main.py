# Packeges :
from sys import exit
from appClass import App
from buttonClass import Button
from tileClass import TileMap
from spritesheetClass import Spritesheet
from playerClass import Player
from cameraClass import *
import time
import pygame

# Check starter file :
if __name__ != '__main__':
    pygame.quit()
    exit()

pygame.init()
app = App()  # States : ['main menu', 'options', 'map']

WIDTH, HEIGHT = 1920, 1080
CENTER = (WIDTH/2, HEIGHT/2)
screen = pygame.display.set_mode((WIDTH, HEIGHT), ) #  flags=pygame.FULLSCREEN
clock = pygame.time.Clock()
start_dt_time = time.time()
FPS = 60

# Buttons :
start_button = Button(surf=pygame.Surface((100, 100)), pos=CENTER)

# Player
player = Player(CENTER)


tileMap = TileMap('resources/spritesheets/city/ground.csv', Spritesheet('resources/spritesheets/city/citySpritesheet.png'), 150, (0, 0))

# Camera
camera = Camera(player)


# Main loop :
while 1:

    dt = clock.tick(FPS) * .001 * FPS
    keys = pygame.key.get_pressed()

    screen.fill((0, 0, 0))
    app.check_events()

    if app.state == 'main menu':
        start_button.check_click_state()
        start_button.draw(screen)

        if start_button.clickState:
            app.state = 'map'

    if app.state == 'map':

        if keys[pygame.K_a]:
            player.left = True
        else:
            player.left = False

        if keys[pygame.K_d]:
            player.right = True
        else:
            player.right = False

        if keys[pygame.K_w]:
            player.up = True
        else:
            player.up = False

        if keys[pygame.K_s]:
            player.down = True
        else:
            player.down = False

        player.move()

        tileMap.rect.center = (0 - camera.offset.x, 0 - camera.offset.y)
        camera.follow([tileMap.rect.left - WIDTH, tileMap.rect.right - WIDTH, tileMap.rect.top - HEIGHT, tileMap.rect.bottom - HEIGHT])

        tileMap.draw_map(screen, tileMap.rect)
        player.draw(screen, (player.rect.x - camera.offset.x, player.rect.y - camera.offset.y))




    pygame.display.update()

