import pygame
import time

pygame.init()
width, height = 800,  600
dvd_logo_speed = [1, 1]
backgroundColor = 0,  0,  0

# dvd_logo_path = "C:\Users\Sam\Google Drive\My Projects\PythonStuff\pygame_tests\dvd_bounce"


screen = pygame.display.set_mode((width, height))

# Asset - the DVD Logo

dvd_logo = pygame.image.load("dvd_logo.png")

dvd_logo_r = dvd_logo.get_rect()

running = True

while running:
    screen.fill(backgroundColor)
    screen.blit(dvd_logo, dvd_logo_r)
    pygame.display.flip()
    time.sleep(10 / 1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
