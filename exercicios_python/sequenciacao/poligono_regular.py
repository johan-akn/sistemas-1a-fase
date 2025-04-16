import turtle

tt = turtle.Turtle()

num_lados = 12
tam_lado = 50

# angulo externo = 360 / n
ang_externo = 360 / num_lados

for poligono in range(num_lados):
    tt.fd(tam_lado)
    tt.left(ang_externo)

turtle.done()