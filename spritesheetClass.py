import json, pygame


class Spritesheet:
    def __init__(self, file_path: str):
        self.filePath = file_path
        self.spriteSheet = pygame.image.load(self.filePath).convert_alpha()
        self.data = self.filePath.replace(self.filePath[-3::], 'json')
        with open(self.data) as f:
            self.data = json.load(f)

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.spriteSheet, (0, 0), (x, y, w, h))
        return sprite

    def parse_sprite(self, name):
        sprite: dict = self.data['frames'][name]['frame']
        x, y, w, h = tuple(sprite.values())
        image = self.get_sprite(x, y, w, h)
        return image

