import pygame
import random

""" Handles drawing logic """
class Renderer():

    def __init__(self, screen, level, camera=None):
        self.screen = screen
        self.cam = camera
        self.level = level

        self.hud = []
        self.follow_camera = []
        self.screen.blit(self.level.bg, [0, 0])


    def add_entities(self, entities, cam_on):
        if cam_on:
            self.follow_camera.append(entities)
        else:
            self.hud.append(entities)
    
    def clear(self):
        for entity in self.level.entities:
            self.screen.blit(self.level.bg, self.cam.apply(entity))
        
        for platform in self.level.platforms:
            self.screen.blit(self.level.bg, self.cam.apply(platform))

    def draw_level(self):

        for platform in self.level.platforms:
            self.screen.blit(platform.image, self.cam.apply(platform))

        for entity in self.level.entities:
            self.screen.blit(entity.image, self.cam.apply(entity))

        pygame.display.update()

