#Random Turtle Designs

import turtle
import random

wnd = turtle.Screen()
wnd.bgcolor("black")

t = turtle.Turtle()
t.color("red")
t.speed(0)
r = random.randint(0,87)

for i in range(100):
   t.fd(57)
   t.left(93)
   t.back(43)
   t.right(r)