import pygame, os
from pygame_aseprite_animation import *

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([300, 300])

# Set file directory
dirname = os.path.dirname(__file__)
aseprite_file_directory = str(dirname) + '/test.ase'

# Initialize animations
test_animation = Animation(aseprite_file_directory)
animationmanager = AnimationManager([test_animation], screen)


running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 0, 0))

    animationmanager.update_self(0, 0)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

