import pygame, sys

screen_width = 480
screen_height = 640
speed = 0.5

clock = pygame.time.Clock()
FPS = 60

class Player:
    def __init__(self, start_x, start_y, img):
        self.pos = [start_x, start_y]
        self.img = img
    
    def move(self, x_diff, y_diff, delta):
        self.pos[0] += x_diff * delta
        self.pos[1] += y_diff * delta
        

if __name__ == '__main__':

    # Create main screen
    screen = pygame.display.set_mode([screen_height, screen_width])

    # Main background
    bg = pygame.Surface([screen_height, screen_width])
    bg.fill((255, 255, 255))
    screen.blit(bg, [0, 0])

    # Load assets
    player_img = pygame.image.load('assets/face.png').convert()

    # Objects that need to be blitted
    dirty_objects = []
    
    # Instantiate player
    player = Player(50, 50, player_img)
    dirty_objects.append(player)

    game_loop = True
    while game_loop:

        delta = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
        
        screen.blit(bg, player.pos)
            
        # Player event handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move(0, -speed, delta)
            dirty_objects.append(player)
        if keys[pygame.K_DOWN]:
            player.move(0, speed, delta)
            dirty_objects.append(player)
        if keys[pygame.K_LEFT]:
            player.move(-speed, 0, delta)
            dirty_objects.append(player)
        if keys[pygame.K_RIGHT]:
            player.move(speed, 0, delta)
            dirty_objects.append(player)
    
        screen.blit(player.img, player.pos)
    
        pygame.display.update()
