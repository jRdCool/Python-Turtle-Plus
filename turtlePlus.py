import turtle as t
from turtle import *
import random

#Version 1.2.1
#Updated 2/8/2021 @ 9:46 pm
#Writen By jRdCool

def functionList():
    functions = [
        "functionList: Lists Funcions in Turtle Plus",
        "penJump: Jumps turtle without drawing a line",
        "showLoc: Displays in the console where turtle is when run",
        "move: Lets you move turtle around the screen and record\nit's position to the console (from the move library by jSdCool)",
        "drawFilledCircle: Draws a filled in circle ",
        "fillSquare: Draws a filled in square",
        "drawRandomFilledCircle: Draws a circle of random size in a \nrandom place",
        "fillRandomPoly: Draws a polygon with a random number of \nsides of equil lenght in a random position on the screen",
        "hlfRec: Draws a rectangle that is exactly half as tall as \nit is wide",
        "rectangle: Draws a rectangle",
        "door: Draws a door",
        "window: Draws a Square widow",
        "isotri: Draws an isometric triangle",
        "triangle: Draws a triangle with three virtices",
        "equiTri: Draws a equilaterial triangle"
    ]
    for a in range(len(functions)):
        print(a+1,": ",functions[a])
    
def penJump(x,y):#jumps turtle without drawing a line
    t.penup()
    t.goto(x,y)
    t.pendown()


def showLoc():#display turtle's curent location
    print(t.position())
    print(t.heading())

colors=("red","blue","orange","green","pink","yellow","brown")
colorChoice=random.choice(colors)

#*****************************************Move Library Intergration*******************************************************

def move():
    def k1():
        t.forward(2)

    def k2():
        t.left(5)

    def k3():
        t.right(5)

    def k4():
        t.back(2)
    def cor():
        print(t.pos())

    onkeypress(k1, "w")
    onkeypress(k2, "a")
    onkeypress(k3, "d")
    onkeypress(k4, "s")
    onkey(cor , "q")
    onkey(t.penup(),"p")
    
    listen()
    mainloop()

#**********************************************End Move Library***********************************************************

def drawFilledCircle(radius,x,y,colorChoice):#draws a filled in circle
    
    t.fillcolor(colorChoice)
    penJump(x,y)
    t.begin_fill()
    t.color(colorChoice)
    t.circle(radius)
    t.end_fill()


def fillSquare(sideLength,x,y,colorChoice):#draws a filled square
    t.color(colorChoice)
    t.fillcolor(colorChoice)
    t.setheading(0)
    penJump(x,y)
    t.begin_fill()
    for a in range(4):
        t.forward(sideLength)
        t.left(90)
    
    t.end_fill()
    
    
def drawRandomFilledCircle(colorChoice):#randomly draws a filled circle with the color of your choice
    t.fillcolor(colorChoice)
    x=random.randint(-500,500)
    y=random.randint(-500,500)
    penJump(x,y)    
    t.begin_fill()
    t.color(colorChoice)
    t.circle(random.randint(10,100))
    t.end_fill()

def fillRandomPoly(colorChoice):#draws a random polygon in a random place 
    
    t.fillcolor(colorChoice)
    x=random.randint(-500,500)
    y=random.randint(-500,500)
    z=random.randint(3,10)
    penJump(x,y)    
    t.begin_fill()
    t.color(colorChoice)
    t.circle(random.randint(10,75),360,z)
    t.end_fill()

def hlfRec(width):#creates a rectangle that is exactly half as high as it is wide
    t.setheading(270) 
    
    t.begin_fill()    
    t.forward(width/2)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(width/2)
    t.left(90)
    t.forward(width)    
    t.end_fill()

def rectangle(x,y,h,w,color):#draws and fills in a rectangle
    penJump(x,y)
    t.fillcolor(color)
    t.begin_fill()
    t.setheading(0)
    t.color(color)
    for a in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def door(x,y,color,hcolor):#makes a door
    rectangle(x,y,46,30,color)
    drawFilledCircle(1,x+26,y+20,hcolor)

def window(x,y,size,frameColor,frameThickness):#Draws a window
    pp=frameThickness
    rectangle(x,y,size+pp,size+pp,frameColor)
    a=((size-pp*3)/2)*1.3
    fillSquare(a,x+pp,y+pp,"lightblue")
    fillSquare(a,x+pp*2+a,y+pp,"lightblue")
    fillSquare(a,x+pp,y+pp*2+a,"lightblue")
    fillSquare(a,x+pp*2+a,y+pp+pp+a,"lightblue")
    #print(a)
    #print(size)
    
def isotri(x,y,b,h,color):#draws an isometric triangle
    t.color(color)
    penJump(x,y)
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x+b,y)
    t.goto(x+b/2,y+h)
    t.end_fill()

def triangle(x1,y1,x2,y2,x3,y3,color):#draws a triangle
    t.color(color)
    t.fillcolor(color)
    penJump(x1,y1)
    
    t.begin_fill()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.end_fill()

def equiTri(x,y,direction,sideLength,color):#Draws an equilateral triangle
    t.setheading(direction)
    t.color(color)
    t.fillcolor(color)
    penjump(x,y)
    t.begin_fill()
    for a in range(3):
        t.forward(sideLength)
        t.left(120)
    t.end_fill()
    t.setheading(0)

