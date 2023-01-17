#!/usr/bin/env python3
import pygame

# Initialize Pygame
pygame.init()

# Set the size of the window
size = (700, 500)

# Create the window
screen = pygame.display.set_mode(size)

# Set the caption of the window
pygame.display.set_caption("Help Desk Interface")

# Run the main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Update the display
    pygame.display.flip()

# Exit Pygame
pygame.quit()
