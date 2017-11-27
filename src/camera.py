import pygame

class Camera:

    def __init__(self, screen_width, screen_height):
        self.curr_state = pygame.Rect(0, 0, screen_width, screen_height)
        self.smooth = 0.08

    # Center camera on sprite
    def update(self, sprite):
        self.curr_state.left = self.lerp(self.curr_state.left,
                                         self.curr_state.width / 2 - sprite.rect.left, self.smooth)
        self.curr_state.top = self.lerp(self.curr_state.top,
                                        self.curr_state.height / 2 - sprite.rect.top, self.smooth)
    
    def lerp(self, start, end, smooth):
        return start + smooth * (end - start)

    # Apply position offset to entity
    def apply(self, sprite):
        return sprite.rect.move(self.curr_state.topleft)
