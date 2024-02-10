from classes import *
import pygame
pygame.init()

window = pygame.display.set_mode((1000,1000))
a = []
for i in range(100):
    a.append(circle(vector(random.randint(0,1000),random.randint(0,1000)),random.randint(1,10)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        

    window.fill((255,255,255))
    circle.classupdate(window)
    pygame.display.update()