import pygame


class Button:
    def __init__(self, pos: tuple[float, float], surf: pygame.Surface):
        self.surf = surf
        self.rect = self.surf.get_rect(center=pos)
        self.clickState = False

        self.held = False

    def check_click_state(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.surf.fill((0, 0, 255))
            self.clickState = False
            if pygame.mouse.get_pressed()[0]:
                self.surf.fill((0, 255, 0))
                self.held = True
            elif self.held and not pygame.mouse.get_pressed()[0]:
                self.held = False
                self.clickState = True

        else:
            self.surf.fill((255, 0, 0))
            self.clickState = False
            self.held = False

    def draw(self, draw_surf: pygame.Surface):
        draw_surf.blit(self.surf, self.rect)
