# Packeges :
from sys import exit
from appClass import App
from buttonClass import Button
import pygame

# Check starter file :
if __name__ != '__main__':
    pygame.quit()
    exit()

pygame.init()
app = App() # States : ['main menu', 'options', 'map']

WIDTH, HEIGHT = 1200, 1200
CENTER = (WIDTH/2, HEIGHT/2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Buttons :
start_button = Button(surf=pygame.Surface((100, 100)), pos=CENTER)

# Main loop :
while 1:
    screen.fill((0, 0, 0))
    app.check_events()

    if app.state == 'main menu':
        start_button.check_click_state()
        start_button.draw(screen)

        if start_button.click_state:
            app.state = 'map'

    if app.state == 'map':
        ...



    pygame.display.update()

