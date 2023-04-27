import pygame
from sys import exit
from ButtonClass import Button
# just a comment


# Happy Halloween
class App:
    def __init__(self):
        self.gameState = 'main menu'

    @staticmethod
    def event_check():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


if __name__ == '__main__':
    app = App()
    WIDTH, HEIGHT = 1200, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('UnholyJack')


    # Testing
    BLACK, WHITE = (0, 0, 0), (255, 255, 255)

    b = Button((WIDTH/2, HEIGHT/2))


    while 1:
        if app.gameState == "main menu":
            screen.fill(BLACK)
            b.update(screen)


        app.event_check()



        pygame.display.update()

