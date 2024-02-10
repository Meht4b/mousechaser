from classes import *
import pygame
pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((1000,1000))
a = []

#no. of particles
n = 700
for i in range(n):
    a.append(circle(vector(random.randint(0,1000),random.randint(0,1000)),random.randint(1,750)*0.01,(0,0,0)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        
    clock.tick(50)
    window.fill((255,255,255))
    circle.classupdate(window)
    pygame.display.update()