'''1 - Crea un programa que tenga la siguiente lista con los gastos de una empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Con estos valores, crea un programa que calcule el promedio de gastos. Sugerencia: usa las funciones integradas sum() y len().'''

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

promedio = sum(gastos)/len(gastos)
print(promedio)

'''2 - Con los mismos datos de la pregunta anterior, determina cuántas compras se realizaron por encima de 3000 reales y calcula el porcentaje con respecto al total de compras.'''
mayores =[]
for mayor in gastos:
  if mayor > 3000:
    mayores.append(mayor)

porcentaje = (len(mayores)/len(gastos))*100
print(f'Las compras mayores fueron: {mayores} y esto representa un {porcentaje}% del total de compras')

'''3 - Crea un código que recoja en una lista 5 números enteros aleatorios e imprima la lista. Ejemplo: [1, 4, 7, 2, 4].'''

import random
num_aleatorios = []
for numero in range(1,6):
  aleatorio = int(random.random()*10)
  num_aleatorios.append(aleatorio)


print(num_aleatorios)

'''4 - Recoge nuevamente 5 números enteros e imprime la lista en orden inverso al enviado.'''

import random
num_aleatorios = []
for numero in range(1,6):
  aleatorio = int(random.random()*10)
  num_aleatorios.append(aleatorio)


print(num_aleatorios)
num_aleatorios.reverse()
print(num_aleatorios)

'''5 - Crea un programa que, al ingresar un número cualquiera, genere una lista que contenga todos los números primos entre 1 y el número ingresado.'''

numero = int(input('Ingresa un número entero: '))

lista_primos = []

for num in range(2, numero):

  primo = True

  for prueba_divisibles in range(2, num):
    if num % prueba_divisibles == 0:

      primo = False
      break

  if primo:
    lista_primos.append(num)

print(f'Lista de números primos: {lista_primos}')

'''6 - Escribe un programa que pida una fecha, especificando el día, mes y año, y determine si es válida para su análisis.'''

# Recopilamos la fecha
dia = int(input('Ingrese el día: '))
mes = int(input('Ingrese el mes: '))
año = int(input('Ingrese el año: '))

# Análisis de febrero
if mes == 2:
  # Verificamos si es o no un año bisiesto
  if año % 4 == 0 and (año % 400 == 0 or año % 100 != 0):
    dias_febrero = 29
  else:
    dias_febrero = 28
  # Verificamos si el día ingresado coincide con el máximo de días de febrero
  if dia >= 1 and dia <= dias_febrero:
    print('Fecha válida')
  else:
    print('Fecha inválida')
# Verificamos meses que terminan en 31 días
elif mes in [1, 3, 5, 7, 8, 10, 12]:
  if dia >= 1 and dia <= 31:
    print('Fecha válida')
  else:
    print('Fecha inválida')
# Verificamos meses que terminan en 30 días
elif mes in [4, 6, 9, 11]:
  if dia >= 1 and dia <= 30:
    print('Fecha válida')
  else:
    print('Fecha inválida')
# Si el mes no está entre 1 y 12
else:
  print('Fecha inválida')


  #########################################################################################################
  ########               PROYECTOS        ##############################################################

  '''7 - Para un estudio sobre la multiplicación de bacterias en una colonia, se recopiló el número de bacterias multiplicadas por día y se puede observar a continuación: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Con estos valores, crea un código que genere una lista que contenga el porcentaje de crecimiento de bacterias por día, comparando el número de bacterias en cada día con el número de bacterias del día anterior. Sugerencia: para calcular el porcentaje de crecimiento, utiliza la siguiente ecuación: 100 * (muestra_actual - muestra_anterior) / muestra_anterior.'''

  bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

for i in range(1, len(bacterias)):
  diferencia = ((bacterias[i] - bacterias[i-1])/bacterias[i-1])*100
  print(f'En el día {i} hubo un crecimiento de {diferencia} respecto al día anterior')


  '''8 - Para una selección de productos alimenticios, debemos separar el conjunto de IDs proporcionados por números enteros, sabiendo que los productos con ID par son dulces y los que tienen ID impar son amargos. Crea un código que recoja 10 IDs. Luego, calcula y muestra la cantidad de productos dulces y amargos.'''


producto_dulce =[]
producto_amargo = []
lista_productos = []

for producto in range(1, 11):
  producto = int(input('Ingresa el id del producto: '))
  lista_productos.append(producto)
  if producto % 2 ==0:
    producto_dulce.append(producto)
  else:
    producto_amargo.append(producto)
print(f'La cantidad de productos dulces son: {len(producto_dulce)}')
print(f'La cantidad de productos amargos son: {len(producto_amargo)}')
print(f'La cantidad total de productos es: {len(lista_productos)}')


'''9 - Desarrolla un programa que informe la puntuación de un estudiante de acuerdo con sus respuestas. Debe pedir la respuesta del estudiante para cada pregunta y verificar si la respuesta coincide con el resultado. Cada pregunta vale un punto y hay opciones A, B, C o D.'''

'''
Resultado del examen:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B
'''

resultados = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
respuestas = []
calificacion =0

for n in range(1,11):
  respuesta = str(input(f'Ingresa tu respuesta a la pregunta {n}: ')).upper()
  respuestas.append(respuesta)
for i in range(len(resultados)):
  if respuestas[i] == resultados[i]:
    calificacion +=1
print(f'La calificación es {calificacion}')

'''10 - Un instituto de meteorología desea realizar un estudio de la temperatura media de cada mes del año. Para ello, debes crear un código que recoja y almacene esas temperaturas medias en una lista. Luego, calcula el promedio anual de las temperaturas y muestra todas las temperaturas por encima del promedio anual y en qué mes ocurrieron, mostrando los meses por su nombre (Enero, Febrero, etc.).'''

meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]
temperaturas = []
temperaturas_altas = []
meses_altos = []
for i in range(0,12):
  temperatura = float(input(f'Ingresa la temperatura del mes de {meses[i]} en grados Celsius: '))
  temperaturas.append(temperatura)
promedio = sum(temperaturas)/len(temperaturas)

for i in range(1, len(temperaturas)):
  if temperaturas[i] > promedio:
    temperaturas_altas.append(temperaturas[i])
    mes = temperaturas.index(temperaturas[i])
    meses_altos.append(meses[mes])


print(f'La temperatura promedio fue de {promedio}')
print(f'Las temperaturas que estuvieron por encima del promedio fueron {temperaturas_altas}')
print(f'Las cuales ocurrieron en los meses de {meses_altos} respectivamente')

'''11 - Una empresa de comercio electrónico está interesada en analizar las ventas de sus productos. Los datos de ventas se han almacenado en un diccionario:

{'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

Escribe un código que calcule el total de ventas y el producto más vendido.
'''

lista_ventas = {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

ventas = lista_ventas.values()
total_ventas = sum(lista_ventas.values())
mas_vendido = max(ventas)
ventas.
print(f'El producto más vendido fue {mas_vendido}')
print(f'El total de ventas fue de {total_ventas} ventas')
