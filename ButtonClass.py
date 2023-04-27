import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.clickStage = 0
        self.surf = pygame.Surface((200, 100))
        self.rect = self.surf.get_rect(center=pos)

    def draw(self, display):
        display.blit(self.surf, self.rect)

    def logic(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.clickStage = 0
            self.surf.fill((255, 0, 0))
            if pygame.mouse.get_pressed()[0]:
                self.held = True
                self.surf.fill((0, 255, 0))
            if self.held and not pygame.mouse.get_pressed()[0]:
                self.clickStage = 1

        else:
            self.clickStage = False
            self.held = False
            self.surf.fill((0, 0, 255))

    def update(self, display):
        self.logic()
        self.draw(display)
