# Packeges :
from sys import exit
from appClass import App
from buttonClass import Button
from tileClass import TileMap
from spritesheetClass import Spritesheet
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
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.FULLSCREEN)
clock = pygame.time.Clock()
start_dt_time = time.time()
FPS = 60

# Buttons :
start_button = Button(surf=pygame.Surface((100, 100)), pos=CENTER)


# Tiles
map = TileMap('resources/spritesheets/city/ground.csv', Spritesheet('resources/spritesheets/city/ground.png'))

# Main loop :
while 1:
    clock.tick(FPS)
    dt = time.time() - start_dt_time * .001 * FPS
    start_dt_time = time.time()

    screen.fill((0, 0, 0))
    app.check_events()

    if app.state == 'main menu':
        start_button.check_click_state()
        start_button.draw(screen)

        if start_button.clickState:
            app.state = 'map'

    if app.state == 'map':
        map.draw_map(screen)



    pygame.display.update()

