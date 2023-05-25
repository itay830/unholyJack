import pygame


class Button:
    def __init__(self, pos: tuple[float, float], surf: pygame.Surface):
        self.surf = surf
        self.rect = self.surf.get_rect(center=pos)
        self.click_state = False

    def check_click_state(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.surf.fill((0, 0, 255))
            self.click_state = False
            if pygame.mouse.get_pressed()[0]:
                self.surf.fill((0, 255, 0))
                self.click_state = True
        else:
            self.surf.fill((255, 0, 0))
            self.click_state = False

    def draw(self, draw_surf: pygame.Surface):
        draw_surf.blit(self.surf, self.rect)