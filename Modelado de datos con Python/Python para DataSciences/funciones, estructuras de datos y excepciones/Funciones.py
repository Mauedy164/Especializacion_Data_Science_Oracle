'''1 - Escribe un código que lee la lista siguiente y realiza:

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
# 1. Leer el tamaño de la lista
# 2. Leer el valor máximo y mínimo
# 3. Calcular la suma de los valores de la lista
# 4. Mostrar un mensaje al final: La lista tiene `tamano` números, donde el mayor 
# es `mayor` y el menor es `menor`. La suma de los valores es `suma`.

'''

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

# 1. Leer el tamaño de la lista
tamaño = (len(lista))

# 2. Leer el valor máximo y mínimo
maximo = (max(lista))
minimo = (min(lista))

# 3. Calcular la suma de los valores de la lista
suma = (sum(lista))
# 4. Mostrar un mensaje al final: La lista tiene `tamano` números, donde el mayor es `mayor` y el menor es `menor`. La suma de los valores es `suma`.

print(f'La lista tiene {tamaño} números, donde el mayor es {maximo} y el menor es {minimo}. La suma de los valores es {suma}')

'''2 - Escribe una función que genere la tabla de multiplicar de un número entero del 1 al 10, según la elección del usuario. Como ejemplo, para el número 7, la tabla de multiplicar se debe mostrar en el siguiente formato:

# Tabla del  7:
# 7 x 0 = 0
# 7 x 1 = 7
# [...]
# 7 x 10 = 70

'''

def multiplicacion(numero):
    print(f'Tabla del {numero}')
    for n in range(1,11):
        print(f'{numero} x {n} = {numero*n}')

numero = int(input('Ingresa un número: '))
multiplicacion(numero)

'''3 - Crea una función que lea la siguiente lista y devuelva una nueva lista con los múltiplos de 3:
[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

'''
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
multiplos_tres = []

def multiplos():
    for i in range(0, len(lista)):
        if lista[i] % 3 ==0:
            multiplos_tres.append(lista[i])
    return(multiplos_tres)
multiplos()
print(multiplos_tres)


'''4 - Crea una lista de los cuadrados de los números de la siguiente lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Recuerda utilizar las funciones lambda y map() para calcular el cuadrado de cada elemento de la lista.'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cuadrados = list(map(lambda x: pow(x,2), lista))

print(cuadrados)

###### Aplicando a proyectos #########

'''5 - Has sido contratado como científico(a) de datos de una asociación de skate. Para analizar las notas recibidas por los skaters en algunas competiciones a lo largo del año, necesitas crear un código que calcule la puntuación de los atletas. Para ello, tu código debe recibir 5 notas ingresadas por los jueces.'''

calificaciones = []
resultado = 0

for calificacion in range(1,6):
    calificacion = float(input(f'Ingresa la calificación {calificacion}: '))
    while calificacion>10:
        calificacion = float(input(f'Ingresa una calificación menor o igual a 10: '))
    calificaciones.append(calificacion)

def promedio():
    resultado = sum(calificaciones)/len(calificaciones)
    print(f'El promedio del skeater fue de {resultado}')
promedio()

'''6 - Para cumplir con una demanda de una institución educativa para el análisis del rendimiento de sus estudiantes, necesitas crear una función que reciba una lista de 4 notas y devuelva:

# mayor nota
# menor nota
# media
# situación (Aprobado(a) o Reprobado(a))
# Uso de la función
# Mostrar: El estudiante obtuvo una media de `media`, con la mayor nota de `mayor` puntos y la menor nota de `menor` puntos y fue `situacion`.)

'''

notas = [5,8,6,10]

def rendimiento():
    mayor_nota = max(notas)
    menor_nota = min(notas)
    media_notas = (sum(notas)/len(notas))
    if media_notas >= 6:
        situacion = 'Aprobado'
    else:
        situacion = 'Reprobado'
    return mayor_nota, menor_nota, media_notas, situacion

resultado = rendimiento()
print(f'La calificación menor del alumno fue de {resultado[1]}, la calificacion mayor fue {resultado[0]}, obteniendo una media de {resultado[2]} y la situación del alumno fue {resultado[3]}')

'''7 - Has recibido una demanda para tratar 2 listas con los nombres y apellidos de cada estudiante concatenándolos para presentar sus nombres completos en la forma Nombre Apellido. Las listas son:

nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

# Normalizar nombres y apellidos y crear una nueva lista con los nombres completos
# Puedes apoyarte en la función map()
'''

nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]
nombres_completos = []

correccion_nombres = list(map(lambda x: x.capitalize(), nombres))
correccion_apellidos = list(map(lambda x: x.capitalize(), apellidos))

for i in range(0, len(correccion_nombres)):
    union = correccion_nombres[i] + ' ' + correccion_apellidos[i]
    nombres_completos.append(union)

print(nombres_completos)

'''8 - Como científico de datos en un equipo de fútbol, necesitas implementar nuevas formas de recopilación de datos sobre el rendimiento de los jugadores y del equipo en su conjunto. Tu primera acción es crear una forma de calcular la puntuación del equipo en el campeonato nacional a partir de los datos de goles marcados y recibidos en cada juego.

Escribe una función llamada calcula_puntos() que recibe como parámetros dos listas de números enteros, representando los goles marcados y recibidos por el equipo en cada partido del campeonato. La función debe devolver la puntuación del equipo y el rendimiento en porcentaje, teniendo en cuenta que la victoria vale 3 puntos, el empate 1 punto y la derrota 0 puntos.

Nota: si la cantidad de goles marcados en un partido es mayor que los recibidos, el equipo ganó. En caso de ser igual, el equipo empató, y si es menor, el equipo perdió. Para calcular el rendimiento, debemos hacer la razón entre la puntuación del equipo y la puntuación máxima que podría recibir.

Para la prueba, utiliza las siguientes listas de goles marcados y recibidos:

goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]
# Texto probablemente mostrado:
# La puntuación del equipo fue `puntos` y su rendimiento fue `desempeno`%"

'''
goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]

puntos_obtenidos = 0

def calcula_puntos():
    global puntos_obtenidos
    for i in range(0,len(goles_marcados)):
        diferencia = goles_marcados[i] - goles_recibidos[i]
        if diferencia > 0:
            puntos_obtenidos += 3
        elif diferencia == 0:
            puntos_obtenidos += 1
        else:
            puntos_obtenidos += 0

    puntos_totales = len(goles_marcados)*3
    rendimiento = (puntos_obtenidos / puntos_totales) * 100
    print(puntos_obtenidos)
    return puntos_obtenidos, rendimiento

resultado = calcula_puntos()
print(f'Los puntos obtenidos fueron {resultado[0]}, teniendo un rendimiento de {resultado[1]: .2f}%')


'''9 - Te han desafiado a crear un código que calcule los gastos de un viaje a una de las cuatro ciudades desde Recife, siendo ellas: Salvador, Fortaleza, Natal y Aracaju.

El costo diario del hotel es de 150 reales en todas ellas y el consumo de gasolina en el viaje en coche es de 14 km/l, siendo que el precio de la gasolina es de 5 reales por litro. Los gastos con paseos y alimentación a realizar en cada una de ellas por día serían [200, 400, 250, 300], respectivamente.

Sabiendo que las distancias entre Recife y cada una de las ciudades son aproximadamente [850, 800, 300, 550] km, crea tres funciones: la primera función calcula los gastos de hotel (gasto_hotel), la segunda calcula los gastos de gasolina (gasto_gasolina) y la tercera los gastos de paseo y alimentación (gasto_paseo).

Para probar, simula un viaje de 3 días a Salvador desde Recife. Considera el viaje de ida y vuelta en coche.

# Texto probablemente mostrado:
# Con base en los gastos definidos, un viaje de [dias] días a [ciudad] desde Recife costaría [gastos] reales.

'''

gastos_paseo = [200, 400, 250, 300]
hospedaje = 150
rendimiento = 14
costo_gasolina = 5
distancia = [850, 800, 300, 550]
ciudades = ['Salvador', 'Fortaleza', 'Natal',  'Aracaju']

ciudad = input('¿A qué ciudad quieres ir? (Salvador, Fortaleza, Natal y Aracaju): ')

ciudad = ciudad.capitalize()

while ciudad not in ciudades:
    print('Opción no válida, por favor escribe alguna de las opciones')
    ciudad = input('¿A qué ciudad quieres ir? (Salvador, Fortaleza, Natal y Aracaju): ')

    ciudad = ciudad.capitalize()

dias = int(input('¿Cuántos días serán? '))

print(ciudad)
#Gasto hotel
def gasto_hotel():
    hotel = dias * hospedaje
    print(f'Pago hotel es de {hotel}')
    return hotel

#Gasto gasolina
def gasto_gasolina():
    indice = ciudades.index(ciudad)
    trayecto = distancia[indice] * 2
    pago_gasolina = (trayecto / rendimiento) * costo_gasolina
    print(f'La distancia es {trayecto} y costará {pago_gasolina}')
    return pago_gasolina

#Gasto paseo (paseo y alimentacion)
def gasto_paseo():
    indice = ciudades.index(ciudad)
    pago_paseo = gastos_paseo[indice] * dias
    print(f'El paseo costará {pago_paseo}')
    return pago_paseo

gasolina = gasto_gasolina()
paseo = gasto_paseo()
hotel = gasto_hotel()
print(f'Con base en los gastos definidos, un viaje de {dias} días a {ciudad} desde Recife costaría {hotel + paseo + gasolina: .2f} reales.')

