#Visually Interesting Turtle Design

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("HloniArt")

player = turtle.Turtle()
player.color("red")
player.speed(0)

for i in range(400):
    player.fd(i)
    player.left(9)
    player.fd(-i)
    player.left(80)
player.hideturtle()

another = turtle.Turtle()
another.color("black")
another.speed(0)

for i in range(400):
    another.fd(i)
    another.left(9)
    another.fd(-i)
    another.left(80)
