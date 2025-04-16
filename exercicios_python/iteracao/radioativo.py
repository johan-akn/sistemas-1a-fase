massa = float(input())
tempo = 50

while massa >= 0.5:
    massa /= 2
    tempo += tempo
    
print(tempo)