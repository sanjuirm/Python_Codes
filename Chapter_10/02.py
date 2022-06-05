from graphics import *
from button import Button
from matplotlib.pyplot import draw, text

class Box:

    def __init__(self,win,point,width,input_txt):
        self.Entry(point,width)
        self.Entry.draw(win)
        self.input_txt=Text(point,input_txt)
        self.input_txt.draw(win)
      

class Info:

    def __init__(self,win,point,label):
        self.label=Text(point,label)
        self.label.draw(win)
      

def main():
     win=GraphWin(640,320,'Conversion Window')
     win.setCoords(0.0,0.0,3.0,4.0)

     inf1=Info(win,Point(1,3),'Celcius')
     inf2=Info(win,Point(1,1),'Farenheit')

     bx1=Box(win,Point(2.25,3),5,'0.0')
     bx2=Box(win,Point(2.25,1),5,'0.0')

     b1=Button(win,Point(5,4.5),6,1, 'Convert')
     b2=Button(win,Point(5,2),2,1, 'Quit')
     
     pt=win.getMouse()

     while not b2.clicked(pt):
         if b1.clicked(pt):
             celcius=float(bx1.getLabel())
             fr=9.0/5.0*celcius+32
             bx2.setText(fr)
             b2.activate()
         pt=win.getMouse()
     
     win.close()

             

