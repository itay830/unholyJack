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
camera = Camera(camera_size=(WIDTH, HEIGHT))


# Main loop :
while 1:
    # Regular setup :
    dt = clock.tick(FPS) * .001 * FPS
    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    app.check_events()

    # Main menu :
    if app.state == 'main menu':
        start_button.check_click_state()
        start_button.draw(screen)

        if start_button.clickState:
            app.state = 'map'


    # 2d map :
    if app.state == 'map':
        player.walk_offseted_rect(keys)

        camera.calc_offset(player.offsetedRect)

        tileMap.offset = tileMap.rect.topleft - camera.offset + camera.camera_center
        tileMap.draw_map(screen, tileMap.offset)

        player.offset = player.offsetedRect.topleft - camera.offset
        player.rect.center = (player.offset.x + player.image.get_width()//2, player.offset.y + player.image.get_height()//2)
        player.draw(screen, player.offset)
        pygame.draw.rect(screen, (255, 0, 0), player.offsetedRect)
        pygame.draw.rect(screen, (0, 255, 0), player.rect)




    pygame.display.update()

