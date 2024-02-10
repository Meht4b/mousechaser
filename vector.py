import math
import pygame

def coord(y):
    #return pygame.display.get_surface().get_size()[1]-y
    return y

class vector:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y)
    
    def __mul__(self,other):
        if isinstance(other,float) or isinstance(other,int):
            return vector(self.x*other,self.y*other)
    
    def __truediv__(self,other):
        if isinstance(other,int):
            return vector(self.x*1/other,self.y*1/other)
    
    def __repr__(self):
        return f'{self.x},{self.y}'

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
        
    def unitVector(self):
        return vector(self.x/self.magnitude(),self.y/self.magnitude())

    def tup(self):
        return (self.x,self.y)
    
    def tupAdj(self):
        
        return (self.x,coord(self.y))
    
    
