import pygame

import tileClass


class Player:
    def __init__(self, pos):
        self.image = pygame.image.load('resources/player/jack.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.right = self.left = self.up = self.down = False
        self.speed = 5

    def draw(self, draw_surf: pygame.Surface, pos):
        draw_surf.blit(self.image, pos)

    def move(self):
        if self.right:
            self.rect.x += self.speed
        if self.left:
            self.rect.x -= self.speed
        if self.up:
            self.rect.y -= self.speed
        if self.down:
            self.rect.y += self.speed

    def collisions(self, objects: list[tileClass.Tile]):
        ...




