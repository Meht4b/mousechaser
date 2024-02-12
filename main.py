from classes import *
import pygame
pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode((1920,1080))
a = []

#no. of particles
n = 10
a.append(circle(vector(500,500),1,(200,200,150),0.01, 0.1,None))
for i in range(n):
    a.append(circle(vector(random.randint(0,1000),random.randint(0,1000)),random.randint(100,750)*0.01,(255,255,255)))

reset = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                reset = True

    if reset:
        print('tru')     
    clock.tick(50)
    window.fill((0,0,0))
    circle.classupdate(window,reset)
    reset = False
    pygame.display.update()