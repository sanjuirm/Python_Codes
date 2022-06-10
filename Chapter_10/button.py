
from graphics import *

class Button:

    def __init__(self,win,points,width,height,label):
    
        w,h=width/2.0,height/2.0
        x,y=points.getX(),points.getY()
        self.xmin,self.xmax=x-w,x+w
        self.ymin,self.ymax=y-h,y+h
        p1=Point(self.xmin,self.ymin)
        p2=Point(self.xmax,self.ymax)
        self.rect=Rectangle(p1,p2)
        self.rect.setFill('lightgrey')
        self.rect.draw(win)
        self.label=Text(points,label)
        self.label.draw(win)
        self.deactivate()
    
    def clicked(self,pt):
        return (self.active and 
        self.xmin<=pt.getX()>=self.xmax and
        self.ymin<=pt.getY()>=self.ymax)

    def getLabel(self):
        return self.label.getText()
    
    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active=True

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active=False
    
    


