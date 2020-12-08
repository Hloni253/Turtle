import turtle
wn = turtle.Screen()
wn.bgcolor("black")
player = turtle.Turtle()
player.color("purple")
player.speed(0)
j = -1
for i in range(200):
    player.fd(i)
    player.circle(i)
    player.left(i)
enemy = turtle.Turtle()
enemy.color("red")
enemy.speed(0)
for k in range(200):
    enemy.fd(k)
    enemy.circle(k)
    enemy.left(k)
enemy.undo()