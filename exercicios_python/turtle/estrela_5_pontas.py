import turtle

t = turtle.Turtle()
x = 150
num_lados = 5
ang_interno = (180 * (num_lados - 2)) / num_lados
ang_ponta = 180 - (2 * ang_interno)
ang_estrela = 180 - ang_ponta

for i in range(5):
    t.forward(x)
    t.left(ang_estrela)

turtle.done()