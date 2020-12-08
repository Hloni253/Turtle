#Screen Saver Loop

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Dumbass Loop")
wn.setup(width=800, height=600)

a = []

t = turtle.Turtle()
t.color("red")
t.speed(0)
t.shape("circle")
t.dx = 4
t.dy = 4

u = turtle.Turtle()
u.color("green")
u.speed(0)
u.shape("circle")
u.penup()
u.goto(-250,25)
u.pendown()
u.dx = 3
u.dy = 3



while True:
    t.sety(t.ycor()+t.dy)
    if t.ycor() > 280:
        t.dy *= -1
        a.append(t.xcor())
    if t.ycor() < -280:
        t.dy *= -1
        a.append(t.xcor())
        
    t.setx(t.xcor()+t.dx)
    if t.xcor() > 380:
        t.dx *= -1
    if t.xcor() < -380:
        t.dx *= -1
        
    u.sety(u.ycor()+u.dy)
    if u.ycor() > 280:
        u.dy *= -1
    if u.ycor() < -280:
        u.dy *= -1
        
    u.setx(u.xcor()+u.dx)
    if u.xcor() > 380:
        u.dx *= -1
    if u.xcor() < -380:
        u.dx *= -1
                