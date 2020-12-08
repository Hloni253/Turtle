#Turtle Designs

import turtle
import random

o = random.randint(0,100)
km = turtle.Turtle()
km.speed(0)

print(o)
for i in range(o):
    for i in range(o):
        km.forward(o)
        km.right(o)
        km.forward(o)
        km.right(o)
    km.right(o)