import pytmx
import pygame, block, player

""" Maintains and loads Level instances """
class LevelManager:
    def __init__(self):
        self.levels = self.load_levels()
        self.curr_level = None

    def load_levels(self):
        num_levels = 1
        levels = []
        for i in range(num_levels):
            new_level = Level('../assets/level' + str(i) + ".tmx")
            levels.append(new_level)
        return levels

    def set_level(self, level_id):
        self.curr_level = self.levels[level_id]

    def curr_level(self):
        return self.curr_level


""" Contains level information, e.g. platforms, enemies """
class Level:

    def __init__(self, path, spawn_position=(50,50)):
        self.tiled_map = pytmx.util_pygame.load_pygame(path)
        self.spawn_position = spawn_position
        self.bg = pygame.Surface([640, 480])
        self.bg.fill((100, 200, 200))
        self.platforms = []
        self.entities = []

        for x, y, img in self.tiled_map.layers[0].tiles():
            self.platforms.append(block.Block(x * 50, y * 50))

        self.entities.append(player.Player())
        self.entities[0].set_col(self.platforms)

        self.player = self.entities[0]

    def update(self, curr_input, delta):
        
        for entity in self.entities:
            entity.update(curr_input, delta)

    