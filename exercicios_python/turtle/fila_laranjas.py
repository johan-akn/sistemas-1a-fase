import turtle

t = turtle.Turtle()

x = 50
y = 10

t.color("orange")

t.begin_fill()

for i in range(4):
    t.dot(x, "orange")
    t.fd(x)
    x += y
    
    
t.end_fill()

turtle.done()