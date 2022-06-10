from math import *
class Projectile:

    def __init__(self,angle,velocity,height):
        self.xpos=0.0
        self.ypos=height
        thetha=radians(angle)
        self.xvel=velocity*cos(thetha)
        self.yvel=velocity*sin(thetha)
    
    def update(self,time):
        self.xpos=self.xpos+self.xvel*time
        yvel1=self.yvel-9.8*time
        self.ypos=self.ypos+time*(self.yvel+yvel1)/2.0
        self.yvel=yvel1
    
    def getX(self):
        return self.xpos
    
    def getY(self):
        return self.ypos