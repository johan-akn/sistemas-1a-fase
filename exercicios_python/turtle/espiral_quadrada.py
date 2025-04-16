import turtle

tu = turtle.Turtle()

x = 5

for i in range (5, 135, x):
    tu.forward(i)
    tu.right(90)

turtle.done()