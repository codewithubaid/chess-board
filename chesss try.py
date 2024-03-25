#Updatation by learning More...!

from turtle import *
from random import *
shelly = Turtle()
shelly.speed(0)

#even Row
def evenRow(x,y):
    shelly.penup()
    shelly.goto(x,y)
    shelly.pendown()
    num = 100
    if x ==500: #Base Condition
        return 0    
    else:
        if ((-(x))//100)%2==0:
            shelly.color("black")
            shelly.begin_fill()
            for i in range(4):
                shelly.forward(100)
                shelly.left(90)
            shelly.end_fill()
        else:
            for i in range(4):
                shelly.forward(100)
                shelly.left(90)
    
    #Recursive Call
    evenRow(x+num,y)

#odd Row 
def oddRow(x,y):
    shelly.penup()
    shelly.goto(x,y)
    shelly.pendown()
    num = 100
    if x ==500:
        return 0
    else:
        if (-(x//100))%2==0:
            for i in range(4):
                shelly.forward(100)
                shelly.left(90)
        else:
            shelly.color("black")
            shelly.begin_fill()
            for i in range(4):
                shelly.forward(100)
                shelly.left(90)
            shelly.end_fill()
    
    #Recursive Call        
    oddRow(x+num,y)

#Calling Functions
evenRow(-500,150)
oddRow(-500,250)
evenRow(-500,-50)
oddRow(-500,50)
evenRow(-500,-250)
oddRow(-500,-150)
oddRow(-500,-250)