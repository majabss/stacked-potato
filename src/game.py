import pygame
import sys
import math
import random

import player
import camera
import block
import level
import input_manager
import inventory
import draw


""" Main game loop """
def run_game(screen, s_height, s_width):

    FPS = 60
    clock = pygame.time.Clock()
    game_running = True

    level_manager = level.LevelManager()
    level_manager.set_level(0)

    cam = camera.Camera(s_height, s_width)
    level_renderer = draw.Renderer(screen, level_manager.curr_level, cam)

    input_handler = input_manager.InputManager()

    # Game loop
    while game_running:

        delta = clock.tick(FPS) / 1000

        level_renderer.clear()
        curr_input = input_handler.get_input() 
        level_manager.curr_level.update(curr_input, delta)
        cam.update(level_manager.curr_level.player)
        level_renderer.draw_level()


def screen_setup():
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    window_mode = pygame.FULLSCREEN

    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], window_mode)
    pygame.display.set_caption("Cool game 0.1.0")
    
    return screen, SCREEN_WIDTH, SCREEN_HEIGHT


if __name__ == '__main__':
    screen, s_width, s_height = screen_setup()
    run_game(screen, s_width, s_height)