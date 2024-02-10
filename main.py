from classes import *
import pygame
pygame.init()

window = pygame.display.set_mode((1000,1000))
a = []
bright_colors = [
    (255, 0, 0),      # Red
    (255, 165, 0),    # Orange
    (255, 255, 0),    # Yellow
    (0, 255, 0),      # Lime
    (0, 255, 255),    # Cyan
    (0, 0, 255),      # Blue
    (128, 0, 128),    # Purple
    (255, 192, 203),  # Pink
    (255, 0, 255),    # Magenta
    (255, 255, 255),  # White
    (0, 0, 0)  
]
for i in range(750):
    a.append(circle(vector(random.randint(0,1000),random.randint(0,1000)),random.randint(1,1),(0,0,0)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        

    window.fill((255,255,255))
    circle.classupdate(window)
    pygame.display.update()