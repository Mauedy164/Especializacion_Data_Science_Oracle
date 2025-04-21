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

#Pasa los values de ventas de cada producto en lista
lista_num_ventas = list(ventas)
print(lista_num_ventas)

#Extrae en lista las keys y lo convierte en lista
productos = list(lista_ventas.keys())

#Buscar el indice del producto mas vendido
mas_vendido_indice = lista_num_ventas.index(mas_vendido)


print(f'El producto más vendido fue {productos[mas_vendido_indice]}')
print(f'El total de ventas fue de {total_ventas} ventas')


'''12 - Se realizó una encuesta de mercado para decidir cuál diseño de marca infantil es más atractivo para los niños. Los votos de la encuesta se pueden ver a continuación:

Tabla de votos de la marca
Diseño 1 - 1334 votos
Diseño 2 - 982 votos
Diseño 3 - 1751 votos
Diseño 4 - 210 votos
Diseño 5 - 1811 votos

Adapta los datos proporcionados a una estructura de diccionario. A partir de ello, informa el diseño ganador y el porcentaje de votos recibidos.
'''

votos_disenos = {
    "Diseño 1": 1334,
    "Diseño 2": 982,
    "Diseño 3": 1751,
    "Diseño 4": 210,
    "Diseño 5": 1811
}

#Hacer diccionario en tupla
diseños_tupla = votos_disenos.items()

#buscar el voto más alto
ganador = max(diseños_tupla, key= lambda x : x[1])

#porcentaje de votos
#Extraer los valores

votos_totales = sum(votos_disenos.values())
porcentaje = (ganador[1]/votos_totales)*100

print(f'El diseño ganador fue el {ganador[0]} con un {porcentaje: .2f}% de los votos totales')


'''13 - Los empleados de un departamento de tu empresa recibirán una bonificación del 10% de su salario debido a un excelente rendimiento del equipo. El departamento de finanzas ha solicitado tu ayuda para verificar las consecuencias financieras de esta bonificación en los recursos. Se te ha enviado una lista con los salarios que recibirán la bonificación: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. La bonificación de cada empleado no puede ser inferior a 200. En el código, convierte cada uno de los salarios en claves de un diccionario y la bonificación de cada salario en el valor correspondiente. Luego, informa el gasto total en bonificaciones, cuántos empleados recibieron la bonificación mínima y cuál fue el valor más alto de la bonificación proporcionada.'''

salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
bonificaciones = []
diccionario_bonificaciones = {}

for i in range(len(salarios)):
  salario = salarios[i]
  if salario*.1>=200:
    porcentaje = salario*.1
    bonificaciones.append(porcentaje)
  else:
    bonificaciones.append(200)

for i in range(len(salarios)):
  diccionario_bonificaciones[salarios[i]]= bonificaciones[i]


#informa el gasto total en bonificaciones
total_bonificaciones = sum(bonificaciones)
print(f'El gasto total de bonificaciones fue de ${total_bonificaciones}')

#cuántos empleados recibieron la bonificación mínima 
num_bonificacion_minima = 0
for i in range(len(bonificaciones)):
  if bonificaciones[i] <= 200:
    num_bonificacion_minima += 1
print(f'El número de empleados que recibieron la bonifcación mínima fueron {num_bonificacion_minima} empleados')

# y cuál fue el valor más alto de la bonificación proporcionada.

print(f'La bonificación más alta fue de ${max(bonificaciones): .2f}')


print(bonificaciones)

print(diccionario_bonificaciones)

'''14 - Un equipo de científicos de datos está estudiando la diversidad biológica en un bosque. El equipo recopiló información sobre el número de especies de plantas y animales en cada área del bosque y almacenó estos datos en un diccionario. En él, la clave describe el área de los datos y los valores en las listas corresponden a las especies de plantas y animales en esas áreas, respectivamente.

{'Área Norte': [2819, 7236], 'Área este': [1440, 9492], 'Área Sur': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}

Escribe un código para calcular el promedio de especies por área e identificar el área con la mayor diversidad biológica. Sugerencia: utiliza las funciones incorporadas sum() y len().

'''

diversidad_area = {'Área Norte': [2819, 7236], 'Área Este': [1440, 9492], 'Área Sur': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}

biodiversidad_max= 0
area_max = ''

for area, valores in diversidad_area.items():    
    promedio = sum(valores)/len(valores)
    if promedio > biodiversidad_max:
      biodiversidad_max = promedio
      area_max = area
    
print(f'El área con mayor biodiversidad de especies es el {area_max} con un promedio de {biodiversidad_max} especies ')


'''15 - El departamento de Recursos Humanos de tu empresa te pidió ayuda para analizar las edades de los colaboradores de 4 sectores de la empresa. Para ello, te proporcionaron los siguientes datos:

{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

Dado que cada sector tiene 10 colaboradores, construye un código que calcule la media de edad de cada sector, la edad media general entre todos los sectores y cuántas personas están por encima de la edad media general.
 
'''
edades_por_sector = {
 'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}



lista_edades_generales = []
tamaño_empresa= 0
lista_encima_promedio = []

# Promedio por cada sector

for sector, edad in edades_por_sector.items():
  lista_edad = list(edad)
  promedio = sum(lista_edad)/len(lista_edad)
  print(f'La media de edad del {sector} es de {promedio} años')
  tamaño_sector = len(lista_edad)
  tamaño_empresa += tamaño_sector

# Promedio de todos los sectores
for sector, edad in edades_por_sector.items():
  lista_edad = list(edad)
  suma = sum(lista_edad)
  lista_edades_generales.append(suma)


promedio_general = sum(lista_edades_generales)/tamaño_empresa
print(f'El promedio general es de {promedio_general}')

#Quienes están por encima del promedio

for sector, edad in edades_por_sector.items():
  valores_edad = list(edad)
  for edad in range(0, len(valores_edad)):
    edad_previa = valores_edad[edad]
    if edad_previa > promedio_general:
      lista_encima_promedio.append(edad_previa)
print(f'Las edades que están por encima son {lista_encima_promedio}, siendo estas una cantidad de {len(lista_encima_promedio)} personas')
