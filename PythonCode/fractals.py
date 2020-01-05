# By: Jonathan Murphy
# Fractals

from graphics import *
from random import * 



def randomLineGeneration():
    win = GraphWin("Fractals",800,800)
    #win.setCoords(0,0,800,800)
    ax1,ax2,ay1,ay2 = 1,1,1,1
    a = Line(Point(ax1,ay1),Point(ax2,ay2))
    a.draw(win)   
    a.setOutline("blue")
    a.setWidth(1)
    
    varEight = 28.2842712475 
    slope = random() * 1.5
   # print("slope", slope)
    
    while True:
    
        ax1,ay1 = random() * 800, random() * 800
        
        ax2,ay2 = random() * varEight, random() * varEight
        
        
        if  slope - .01 < ay1/ax1 < slope + .01:
            print("ax1",ax1,"ay1",ay1)
            scalex = random() * random() * 800
            scaley = random() * random() * 800
            ax2,ay2 = ax2 * scalex, ay2 * scaley
        
            a = Line(Point(ax1,ay1),Point(ax2,ay2))
            p = Point(ax1,ay1)
            a.draw(win) 
            
        
    
    win.getMouse()
    win.close()

#randomLineGeneration()

def structuredLineGeneration():
    win = GraphWin("Fractals",1000,800)
        
    x = 500
    y = 0
    
    xdir = .9
    ydir = 1
    
    while True:
        if (x >= 0 and y >= 0) and (x <= 1000 and y <= 800):
            c1 = Circle(Point(x,y),20)
            c1.setFill("blue")
            c1.draw(win)
            x += 1 * xdir
            y += 1 * ydir
        else:
            if y < 0:
                ydir = 1
                y += 2
                print("y less than 0")
            
                
            elif y > 800:
                ydir = -1 
                y -= 2
                print("y greater than 800")
            
                
            elif x < 0:
                xdir = .9
                x += 2
                print("x less than 0")
            
            elif x > 1000:
                xdir = -.9
                x -= 2
                print("x greater than 1000")
           
        #print("x",x,"y",y)
    
    
structuredLineGeneration()


