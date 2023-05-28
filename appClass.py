import pygame


class App:
    def __init__(self):
        self.state = 'main menu'

    @staticmethod
    def exit_game():
        pygame.quit()
        exit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit_game()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.exit_game()


