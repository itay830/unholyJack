import pygame, csv, os

import spritesheetClass


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spritesheet: spritesheetClass.Spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, draw_surf):
        draw_surf.blit(self.image, self.rect)


class TileMap:
    def __init__(self, file_path: str, spritesheet: spritesheetClass.Spritesheet):
        self.map_w, self.map_h = 0, 0

        self.tile_size = 16
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(file_path)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw_map(self, surface):
        surface.blit(self.map_surface, (0, 0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    @staticmethod
    def read_csv(file_path: str):
        map = []
        with open(os.path.join(file_path)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self, file_path: str):
        tiles = []
        map = self.read_csv(file_path)
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile == '0':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif tile == '1':
                    tiles.append(Tile('grass.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '2':
                    tiles.append(Tile('grass2.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                x += 1

            y += 1
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles
