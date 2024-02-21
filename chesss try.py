from turtle import *
from random import *
shelly = Turtle()
shelly.speed(0)
#1
def row(x = -500,y = 250):
    shelly.penup()
    shelly.goto(x,y)
    shelly.pendown()
    num = 100
    num2 = 100
    if x ==500:
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
    row(x+num)
    
row()
#2
def row(x = -500,y = 150):
    shelly.penup()
    shelly.goto(x,y)
    shelly.pendown()
    num = 100
    num2 = 100
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
            
    row(x+num)

row()
#3
def row(x = -500,y = 50):
    shelly.penup()
    shelly.goto(x,y)
    shelly.pendown()
    num = 100
    num2 = 100
    if x ==500:
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
    row(x+num)

row()
#4
def row(x = -500,y = -50):
    shelly.penup()
    shelly.goto(x,y)
    shelly.pendown()
    num = 100
    num2 = 100
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
            
    row(x+num)

row()

#5
def row(x = -500,y = -150):
    shelly.penup()
    shelly.goto(x,y)
    shelly.pendown()
    num = 100
    num2 = 100
    if x ==500:
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
    row(x+num)

row()
#6
def row(x = -500,y = -250):
    shelly.penup()
    shelly.goto(x,y)
    shelly.pendown()
    num = 100
    num2 = 100
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
            
    row(x+num)

row()

#7
def row(x = -500,y = -350):
    shelly.penup()
    shelly.goto(x,y)
    shelly.pendown()
    num = 100
    num2 = 100
    if x ==500:
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
    row(x+num)

row()
