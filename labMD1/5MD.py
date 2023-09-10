'''
Sierpinski triangle
'''
import turtle

x=turtle.Turtle()

def sierpinski(a, b):
    if a==0:
        x.forward(b)
        x.left(120)
        x.forward(b)
        x.left(120)
        x.forward(b)
        x.left(120)
    else:
        print(a, b)
        sierpinski(a-1, b/2) 
        print(a, b)
        x.forward(b/2)
        sierpinski(a-1, b/2)
        print(a, b)
        x.left(120)
        x.forward(b/2)
        x.right(120)
        sierpinski(a-1,b/2)
        print(a, b)
        x.right(120)
        x.forward(b/2)
        x.left(120)

w=turtle.Screen()
w.bgcolor("white")

x.color("black")
x.speed("fastest")

x.penup()
x.goto(-600,-400)
x.pendown()

level=int(input())
sierpinski(level,500)