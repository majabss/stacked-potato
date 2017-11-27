import pygame

class Player(pygame.sprite.DirtySprite):

    def __init__(self, x=50, y=50):
        pygame.sprite.DirtySprite.__init__(self)
        self.rect = pygame.Rect(x, y, 50, 50)
        # Images
        self.walk_1 = pygame.image.load('../assets/player_walk_1.png').convert()
        self.walk_2 = pygame.image.load('../assets/player_walk_2.png').convert()
        self.jump = pygame.image.load('../assets/player_jump.png').convert()
        self.frames = [self.walk_1, self.walk_2, self.jump]
        self.image = self.frames[0]

        self.frames_per_image = 10
        self.curr_frame = 0
        self.image_index = 0

        self.x_speed = 0
        self.y_speed = 0
    
        self.JUMP_SPEED = -720
        self.WALK_SPEED = 300
        self.GRAV_ACCEL = 45
    
        self.on_ground = False

        self.potential_collisions = []
    
    def set_col(self, p_c):
        self.potential_collisions = p_c

    def update(self, curr_input, delta):

        if "left" in curr_input or "right" in curr_input:
            self.curr_frame += 1
            if self.curr_frame == self.frames_per_image:
                self.image_index += 1
                self.image_index = self.image_index % len(self.frames)
                self.image = self.frames[self.image_index]
                self.curr_frame = 0

        if self.x_speed != 0 or self.y_speed != 0:
            self.dirty = 1
        if "left" in curr_input:
            self.x_speed = -self.WALK_SPEED
        if "right" in curr_input:
            self.x_speed = self.WALK_SPEED
        if "jump" in curr_input:
            if self.on_ground:
                self.y_speed = self.JUMP_SPEED
        if not self.on_ground:
            self.y_speed += self.GRAV_ACCEL
        if "left" not in curr_input and "right" not in curr_input:
            self.x_speed = 0
        
        if "restart" in curr_input:
            self.rect.left = 50
            self.rect.top = 50

        self.rect.left += self.x_speed * delta
        self.detect_collisions_x(self.x_speed)

    
        self.on_ground = False 
        self.rect.top += self.y_speed * delta
        self.detect_collisions_y(self.y_speed)


    def detect_collisions_x(self, x_speed):
        for p in self.potential_collisions:
            if pygame.sprite.collide_rect(self, p):
                if x_speed > 0:
                    self.rect.right = p.rect.left
                if x_speed < 0:
                    self.rect.left = p.rect.right
    
    def detect_collisions_y(self, y_speed):
        for p in self.potential_collisions:
            if pygame.sprite.collide_rect(self, p):
                if y_speed < 0:
                    self.rect.top = p.rect.bottom
                    self.y_speed = 0
                if y_speed > 0:
                    self.rect.bottom = p.rect.top
                    self.y_speed = 0
                    self.on_ground = True




