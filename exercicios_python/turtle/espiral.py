import turtle

t = turtle.Turtle()
t.speed(0)

x = 5

for z in range(180):
    for i in range(4):
         t.forward(x)
         t.right(90)
    t.right(10)
    x += 1
    
turtle.done()