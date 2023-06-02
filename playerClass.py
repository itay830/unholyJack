import pygame

import tileClass


class Player:
    def __init__(self, pos):
        self.offset = pygame.math.Vector2()
        self.image = pygame.image.load('resources/player/jack.png').convert_alpha()
        self.offsetedRect = self.image.get_rect(center=pos)
        self.rect = self.image.get_rect(center=pos)
        self.speed = 15
        self.dir = pygame.math.Vector2()

    def draw(self, draw_surf: pygame.Surface, pos):
        draw_surf.blit(self.image, pos)

    def set_dir(self, keys):
        if keys[pygame.K_d]:
            self.dir.x = 1
        elif keys[pygame.K_a]:
            self.dir.x = -1
        else:
            self.dir.x = 0

        if keys[pygame.K_w]:
            self.dir.y = -1
        elif keys[pygame.K_s]:
            self.dir.y = 1
        else:
            self.dir.y = 0
    def walk(self, keys):
        self.set_dir(keys)
        self.rect.x += self.dir.x * self.speed
        self.rect.y += self.dir.y * self.speed

    def walk_offseted_rect(self, keys):
        self.set_dir(keys)
        self.offsetedRect.x += self.dir.x * self.speed
        self.offsetedRect.y += self.dir.y * self.speed

    def collisions(self, objects: list[tileClass.Tile]):
        ...




