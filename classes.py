from vector import vector
import random
import pygame

class circle:
    circles = []
    friction = 0 

    def __init__(self,pos,mass,color,forceMagnitude,FrictionMagnitude,Range):        
        self.mass =mass
        self.pos = pos
        self.color = color
        self.velocity = vector()
        self.accel = vector()
        self.radius = mass*2
        self.ForceMagnitude = forceMagnitude
        self.FrictionMagnitude = FrictionMagnitude
        self.Range = Range
        self.trail = [self.pos,self.pos,self.pos]
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
    def classupdate(cls,win,reset):
        cls.collision()
        for i in cls.circles:
            i.update(win,reset)

    def update(self,win,reset):
        f = vector(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])-self.pos

        #to change the magnitude of force 
        if self.Range:
            if f.magnitude()<self.Range:            
                self.force(f*self.ForceMagnitude)
        else:   
            self.force(f*self.ForceMagnitude)

        self.force(self.velocity*-self.FrictionMagnitude)


        self.pos += self.velocity

        #uncomment if you want border

        #if self.pos.x < 0 or self.pos.x>1000:
            #self.velocity.x = self.velocity.x*-1
        #if self.pos.y < 0 or self.pos.y>1000:
            #self.velocity.y = self.velocity.y*-1
        if reset:
            self.velocity = vector()
        

        self.velocity += self.accel
        self.accel = vector()
        self.display(win)
        self.trail.append(self.pos)
        self.trail.pop(0)

    def display(self,win):
        pygame.draw.circle(win,self.color,self.pos.tup(),self.radius)
        pygame.draw.line(win,self.color,self.pos.tup(),self.trail[0].tup())


#for i in range(10000):
    #a.append(circle(vector(random.randint(0,5000),random.randint(0,5000)),random.randint(0,5)))
