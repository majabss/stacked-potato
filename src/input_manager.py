""" Handle control input logic """

import pygame
import sys


class InputManager():

    def __init__(self):
        # Set up game controller
        self.use_cont = True if pygame.joystick.get_count() > 0 else False
        if self.use_cont: 
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

        
        self.key_mappings = {

            "ESCAPE": pygame.K_ESCAPE,
            "LEFT": pygame.K_a,
            "RIGHT": pygame.K_d,
            "JUMP": pygame.K_i,
            "DOWN": pygame.K_s,
            "UP": pygame.K_w,
            "INV": pygame.K_p,
            "RESTART": pygame.K_o

        }

    


    def get_input(self):
        curr_input = dict()

        # Player movement
        keys = pygame.key.get_pressed()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == self.key_mappings["INV"]:
                    curr_input["inv"] = True
                if event.key == self.key_mappings["ESCAPE"]:
                    sys.exit()
        
        keys = pygame.key.get_pressed()

        if keys[self.key_mappings["LEFT"]]:
            curr_input["left"] = True
        if keys[self.key_mappings["RIGHT"]]:
            curr_input["right"] = True
        if keys[self.key_mappings["JUMP"]]:
            curr_input["jump"] = True
        if keys[self.key_mappings["RESTART"]]:
            curr_input["restart"] = True


        # Joystick
        if self.use_cont:
            h_axis = self.joystick.get_axis(0)
            v_axis = self.joystick.get_axis(1)
            if h_axis > 0.5:
                curr_input["right"] = True
            if h_axis < -0.5:
                curr_input["left"] = True
            if v_axis > 0.5:
                curr_input["down"] = True
            if v_axis < 0.5:
                curr_input["up"] = True

            if self.joystick.get_button(1) == 1:
                curr_input["jump"] = True
            if self.joystick.get_button(3) == 1:
                curr_input["inv"] = True

        return curr_input
