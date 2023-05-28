import pygame, csv, os

import spritesheetClass


class Tile:
    def __init__(self, image, x, y, spritesheet: spritesheetClass.Spritesheet, size=(75, 75), name: str=''):
        self.image = pygame.transform.scale(spritesheet.parse_sprite(image), size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.name = name

    def draw(self, draw_surf):
        draw_surf.blit(self.image, self.rect)


class TileMap:
    def __init__(self, file_path: str, spritesheet: spritesheetClass.Spritesheet, tile_size, pos):
        self.map_w, self.map_h = 0, 0

        self.tile_size = tile_size
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(file_path)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()
        self.rect = self.map_surface.get_rect(center=pos)

    def draw_map(self, surface, pos):
        surface.blit(self.map_surface, pos)

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
        tiles = set()
        map = self.read_csv(file_path)
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile == '-1':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif tile == '0':
                    tiles.add(Tile('grass.png', x * self.tile_size, y * self.tile_size, self.spritesheet, (self.tile_size, self.tile_size), 'grass'))
                elif tile == '1':
                    tiles.add(Tile('wood.png', x * self.tile_size, y * self.tile_size, self.spritesheet, (self.tile_size, self.tile_size), 'wood'))
                elif tile == '2':
                    tiles.add(Tile('door1.png', x * self.tile_size, y * self.tile_size, self.spritesheet, (self.tile_size, self.tile_size), 'door'))
                elif tile == '3':
                    tiles.add(Tile('door2.png', x * self.tile_size, y * self.tile_size, self.spritesheet, (self.tile_size, self.tile_size), 'door'))

                x += 1

            y += 1
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles

    def resize_maps(self, w, h):
        self.map_surface = pygame.transform.scale(self.map_surface, (w, h))