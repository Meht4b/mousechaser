from vector import vector
import random
import pygame

class circle:
    circles = []
    friction = 0 

    def __init__(self,pos,mass):        
        self.mass =mass
        self.pos = pos
        self.velocity = vector()
        self.accel = vector()
        self.radius = mass
        circle.circles.append(self)

    def force(self,force):
        self.accel += force/self.mass

    @staticmethod
    def partition(array, low, high):
    
        pivot = array[high].pos.x
        i = low - 1
        for j in range(low, high):
            if array[j].pos.x <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1
 
    @staticmethod
    def quicksort(array, low, high):
        if low < high:

            pi = circle.partition(array, low, high)
            circle.quicksort(array, low, pi - 1)
            circle.quicksort(array, pi + 1, high)

    @classmethod
    def collision(cls):
        possibleCollision = []
        circle.quicksort(circle.circles,0,len(circle.circles)-1)
        i,j = 0,1
        
        while i<len(circle.circles)-1:
            Start = circle.circles[i].pos.x+circle.circles[i].radius
            End = circle.circles[j].pos.x-circle.circles[j].radius
            if End < Start:
                possibleCollision.append((circle.circles[i],circle.circles[j]))
                if j==len(circle.circles)-1:
                    i+=1
                else:
                    j+=1

            else:
                i+=1
        
        for i in possibleCollision:
            dis = (i[0].pos - i[1].pos).magnitude()
            if dis<i[0].radius+i[1].radius:
                total_mass = i[0].mass + i[1].mass
                v1x = (i[0].velocity.x * (i[0].mass - i[1].mass) + 2 * i[1].mass * i[1].velocity.x) / total_mass
                v1y = (i[0].velocity.y * (i[0].mass - i[1].mass) + 2 * i[1].mass * i[1].velocity.y) / total_mass
                v2x = (i[1].velocity.x * (i[1].mass - i[0].mass) + 2 * i[0].mass * i[0].velocity.x) / total_mass
                v2y = (i[1].velocity.y * (i[1].mass - i[0].mass) + 2 * i[0].mass * i[0].velocity.y) / total_mass
                
                i[0].velocity = vector(v1x,v1y)
                i[1].velocity = vector(v2x,v2y)

    def __repr__(self):
        return str(self.pos.x)
    
    @classmethod
    def classupdate(cls,win):
        cls.collision()
        for i in cls.circles:
            i.update(win)

    def update(self,win):
        f = vector(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])-self.pos
        self.force(f*0.01)
        self.force(self.velocity*-0.05)
        self.pos += self.velocity
        print(type(self.velocity),type(self.accel))
        self.velocity += self.accel
        self.accel = vector()
        self.display(win)

    def display(self,win):
        pygame.draw.circle(win,(0,0,0),self.pos.tup(),self.radius)


#for i in range(10000):
    #a.append(circle(vector(random.randint(0,5000),random.randint(0,5000)),random.randint(0,5)))
