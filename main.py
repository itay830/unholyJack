import pygame
from sys import exit

BLACK, WHITE = (0, 0, 0), (255, 255, 255)

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

    while 1:
        if app.gameState == "main menu":
            screen.fill(BLACK)


        app.event_check()



        pygame.display.update()

