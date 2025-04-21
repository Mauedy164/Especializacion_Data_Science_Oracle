import matplotlib
from matplotlib import pyplot as plt

'''Ejemplo 1: Vamos a probar la biblioteca Matplotlib para un ejemplo sobre el cálculo de los promedios de notas de los estudiantes de una clase.'''

nombres = ['Ana', 'Carlos', 'Sofía', 'Mateo']
calificaciones = [7, 3, 9, 5]

plt.bar( x= nombres, height= calificaciones)
plt.show()

'''Ejemplo 2: Vamos a seleccionar aleatoriamente a un alumno para presentar su trabajo de ciencia de datos usando la biblioteca random.'''

from random import choice


print(choice(nombres))

'''Ejercicios

Escribe un código para importar la biblioteca numpy con el alias np.
'''

import numpy as np

'''Crea un programa que lea la siguiente lista de números y elija uno al azar.
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
'''
import random
from random import choice as ch

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

print(ch(lista))

'''4 - Crea un programa que genere aleatoriamente un número entero menor que 100.'''

import random
from random import randrange
print(randrange(1,100))

'''5 - Crea un programa que solicite a la persona usuaria ingresar dos números enteros y calcule la potencia del primer número elevado al segundo.'''

import math


num_1 = int(input('Ingresa un número: '))
num_2 = int(input('Ingresa un segundo número: '))

print(f'El la potencia es: {math.pow(num_1, num_2)}')


###### Aplicando a proyectos #########

'''6 - Se debe escribir un programa para sortear a un seguidor de una red social para ganar un premio. La lista de participantes está numerada y debemos elegir aleatoriamente un número según la cantidad de participantes. Pide a la persona usuaria que proporcione el número de participantes del sorteo y devuelve el número sorteado.'''



#Solicitar el numero de participantes

cantidad_participantes = int(input('Ingresa el número de participantes: '))

#Devuelve numero sorteado

import random
from random import randrange

ganador = randrange(1,cantidad_participantes+1)

print(f'El ganador es el participante con el número {ganador}')

'''7 - Has recibido una solicitud para generar números de token para acceder a la aplicación de una empresa. El token debe ser par y variar de 1000 a 9998. Escribe un código que solicite el nombre de la persona usuaria y muestre un mensaje junto a este token generado aleatoriamente.'''

#Solicita el nombre

usuario = str(input('Ingresa tu nombre de usuario: '))

#Generar el token que sea par y esté entre 1000 a 9998

from random import randrange

token_aleatorio = randrange(1000,9999)
while token_aleatorio % 2 != 0:
    token_aleatorio = randrange(1000,9999)
print(f'Tu usuario es {usuario} y tu token es {token_aleatorio}')

'''8 - Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su menú llamado "ensalada de frutas sorpresa". En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12 para componer la ensalada de frutas del cliente. Crea el código que realice esta selección aleatoria según la lista dada.

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

'''

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

from random import sample

frutas_aleatorias = sample(frutas, 3)
print(f'Las frutas de la ensalada serán {frutas_aleatorias}')


'''9 - Has recibido un desafío para calcular la raíz cuadrada de una lista de números, identificando cuáles resultan en un número entero. La lista es la siguiente:

numeros = [2, 8,9, 15, 23, 91, 112, 256]

'''
from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]
raices_enteras = []

for i in range(0, len(numeros)):
    if sqrt(numeros[i]) == int(sqrt(numeros[i])):
        raices_enteras.append(numeros[i])

print(f'Los numeros que sus raices cuadradas dan un número entero son: {raices_enteras}')

'''10 - Haz un programa para una tienda que vende césped para jardines. Esta tienda trabaja con jardines circulares y el precio del metro cuadrado de césped es de R$ 25,00. Pide a la persona usuaria el radio del área circular y devuelve el valor en reales de cuánto tendrá que pagar.'''

radio = float(input('Ingresa el radio en metros del cesped que requiere: '))
precio=25

from math import pi, pow

area = pi * pow(radio, 2)

print(f'El precio a pagar es de R${(area*precio): .2f}')