import pygame

# has to be the first call!
pygame.init()
# surface
gameDisplay = pygame.display.set_mode((800, 600))
# window title
pygame.display.set_caption('A bit Racey')
# game clock
clock = pygame.time.Clock()


crashed = False
# game loop
while not crashed:

    # list of events per frame per second:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # player wanted to close the window
            crashed = True

        print(event)

    # update eyerything or only the one parameter
    pygame.display.update()

    #  frames per second
    clock.tick(60)

pygame.quit()
quit()