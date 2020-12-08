#Cool Turtle Designs -- Note: The designs are made randomly

import turtle
import random

wnd = turtle.Screen()
wnd.bgcolor("black")

player = turtle.Turtle()
player.color("red")
player.speed(0)

def shape(angle, side, limit):
    reverseDirection = 200
    player.fd(side)
    if side % (reverseDirection * 2) == 0:
        angle = angle + 2
        print(side)
    elif side % reverseDirection == 0:
        angle = angle - 2
        print(side)
    player.right(angle)
    side = side + 2
    if side < limit:
        shape(angle, side, limit)
angle = random.randint(0,200)
side = random.randint(0,20)
limit = random.randint(0,800)
shape(angle, side, limit)
