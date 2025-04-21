from math import sqrt

numeros = [2, 8,9, 15, 23, 91, 112, 256]
raices_enteras = []

for i in range(0, len(numeros)):
    if sqrt(numeros[i]) == int(sqrt(numeros[i])):
        raices_enteras.append(numeros[i])

print(f'Los numeros que sus raices cuadradas dan un número entero son: {raices_enteras}')