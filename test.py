# Packeges :
from sys import exit
import time
import pygame
import json
import csv

# Check starter file :
if __name__ != '__main__':
    pygame.quit()
    exit()

pygame.init()

# Screen
WIDTH, HEIGHT = 1920, 1080
CENTER = (WIDTH/2, HEIGHT/2)
screen = pygame.display.set_mode((WIDTH, HEIGHT), ) #  flags=pygame.FULLSCREEN
clock = pygame.time.Clock()
start_dt_time = time.time()
FPS = 60


# App event handling :
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


app = App()  # States : ['main menu', 'options', 'map']


# Buttons :
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

    def draw(self):
        screen.blit(self.surf, self.rect)


start_button = Button(surf=pygame.Surface((100, 100)), pos=CENTER)


# Player
class Player:
    def __init__(self, pos):
        self.image = pygame.image.load('resources/player/jack.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.right = self.left = self.up = self.down = False
        self.speed = 5

    def draw(self):
        screen.blit(self.image, self.rect)

    def walk(self, dt):
        if self.right:
            self.rect.x += self.speed * dt
        if self.left:
            self.rect.x -= self.speed * dt
        if self.up:
            self.rect.y -= self.speed * dt
        if self.down:
            self.rect.y += self.speed * dt


player = Player(CENTER)


# Tiles
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


class Tile:
    def __init__(self, image, x, y, spritesheet: Spritesheet, size=(75, 75)):
        self.image = pygame.transform.scale(spritesheet.parse_sprite(image), size)
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, draw_surf):
        draw_surf.blit(self.image, self.rect)


class TileMap:
    def __init__(self, file_path: str, spritesheet: Spritesheet, tile_size):
        self.map_w, self.map_h = 0, 0

        self.tile_size = tile_size
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(file_path)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw_map(self, pos):
        screen.blit(self.map_surface, pos)

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    @staticmethod
    def read_csv(file_path: str):
        map = []
        with open(file_path) as data:
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
                if tile == '-1':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif tile == '0':
                    tiles.append(Tile('grass.png', x * self.tile_size, y * self.tile_size, self.spritesheet, (self.tile_size, self.tile_size)))
                elif tile == '1':
                    tiles.append(Tile('wood.png', x * self.tile_size, y * self.tile_size, self.spritesheet, (self.tile_size, self.tile_size)))
                elif tile == '2':
                    tiles.append(Tile('door1.png', x * self.tile_size, y * self.tile_size, self.spritesheet, (self.tile_size, self.tile_size)))
                elif tile == '3':
                    tiles.append(Tile('door2.png', x * self.tile_size, y * self.tile_size, self.spritesheet, (self.tile_size, self.tile_size)))

                x += 1

            y += 1
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles

    def resize_map(self, w, h):
        self.map_surface = pygame.transform.scale(self.map_surface, (w, h))


tileMap = TileMap('resources/spritesheets/city/ground.csv', Spritesheet('resources/spritesheets/city/citySpritesheet.png'), 150)


# Camera
class Camera:
    def __init__(self, target: Player):
        self.offsetx = 0
        self.target = target

    def get_offsetx(self, display: pygame.Surface):
        return display.get_width() / 2 - self.target.rect.centerx + self.target.speed

    def get_offsety(self, display: pygame.Surface):
        return display.get_height() / 2 - self.target.rect.centery


camera = Camera(player)




# Main loop :
while 1:
    dt = clock.tick(FPS) * .001 * FPS
    keys = pygame.key.get_pressed()

    screen.fill((0, 0, 0))
    app.check_events()

    if app.state == 'main menu':
        start_button.check_click_state()
        start_button.draw()

        if start_button.clickState:
            app.state = 'map'

    if app.state == 'map':
        tileMap.draw_map((camera.get_offsetx(screen), camera.get_offsety(screen)))

        if keys[pygame.K_a]:
            player.left = True
        else:
            player.left = False

        if keys[pygame.K_d]:
            player.right = True
        else:
            player.right = False

        if keys[pygame.K_w]:
            player.up = True
        else:
            player.up = False

        if keys[pygame.K_s]:
            player.down = True
        else:
            player.down = False

        player.walk(dt)
        player.draw()
    pygame.display.update()
