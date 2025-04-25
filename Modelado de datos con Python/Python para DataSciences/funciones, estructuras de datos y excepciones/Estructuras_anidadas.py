'''1 - Crea un código para imprimir la suma de los elementos de cada una de las listas contenidas en la siguiente lista:

lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]

'''

lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]

suma = [sum(numero) for numero in lista_de_listas]
print(suma)


'''2 - Crea un código para generar una lista que almacene el tercer elemento de cada tupla contenida en la siguiente lista de tuplas:

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

'''
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]


edad = [lista_de_tuplas[i][2] for i in range(len(lista_de_tuplas))]

print(edad)

'''3 - A partir de la lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crea un código para generar una lista de tuplas en la que cada tupla tenga el primer elemento como la posición del nombre en la lista original y el segundo elemento siendo el propio nombre.'''

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

segunda_lista = [ (nombres, lista[nombres]) for  nombres in range(len(lista))]
print(segunda_lista)


'''4 - Crea una lista usando la comprensión de listas (list comprehension) que almacene solo el valor numérico de cada tupla en caso de que el primer elemento sea 'Apartamento', a partir de la siguiente lista de tuplas:

alquiler = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

'''

alquiler = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

alquiler_apartamento = [alquiler[i][1] for i in range(len(alquiler)) if alquiler[i][0] == 'Apartamento' ]
print(alquiler_apartamento)



'''5 - Crea un diccionario usando la comprensión de diccionarios (dict comprehension) en el que las claves estén en la lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] y los valores estén en gasto = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].'''

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
gasto = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

lista = {meses[i] : gasto[i] for i in range(len(meses))}

print(lista)

'''6 - Una tienda tiene una base de datos con la información de venta de cada representante y de cada año y necesita filtrar solo los datos del año 2022 con ventas mayores a 6000. La tienda proporcionó una muestra con solo las columnas de los años y los valores de venta para que puedas ayudar a realizar la filtración de los datos a través de un código:

ventas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

'''

ventas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]


ventas_2022 = [(ventas[i][0], ventas[i][1]) for i in range(len(ventas)) if (ventas[i][0] == '2022' and ventas[i][1] >=6000 )]

print(ventas_2022)


'''7 - Una clínica analiza datos de pacientes y almacena el valor numérico de la glucosa en una base de datos y le gustaría etiquetar los datos de la siguiente manera:

Glucosa igual o inferior a 70: 'Hipoglicemia'
Glucosa entre 70 y 99: 'Normal'
Glucosa entre 100 y 125: 'Alterada'
Glucosa superior a 125: 'Diabetes'
La clínica proporcionó parte de los valores y tu tarea es crear una lista de tuplas usando la comprensión de listas que contenga la etiqueta y el valor de la glucemia en cada tupla.

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

'''

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

rangos = [(valor, 'Hipoglicemia' if valor < 70 else 'Normal' if valor < 99 else 'Alterada' if valor < 125 else 'Diabetes') for valor in glicemia]

print(rangos)


'''8 - Un comercio electrónico tiene información de id de venta, cantidad vendida y precio del producto divididos en las siguientes listas:

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cantidad = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
precio = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

La plataforma necesita estructurar estos datos en una tabla que contenga el valor total de la venta, que se obtiene multiplicando la cantidad por el precio unitario. Además, la tabla debe contener un encabezado indicando las columnas: 'id', 'cantidad', 'precio' y 'total'.

Crea una lista de tuplas en la que cada tupla tenga id, cantidad, precio y valor total, siendo la primera tupla el encabezado de la tabla.'''

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cantidad = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
precio = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

tabla = [('id', 'cantidad', 'precio', 'total')]
tabla += [( (id[i], cantidad[i], precio[i], (cantidad[i]*precio[i]))) for i in range(len(id))]

print(tabla)


'''9.- TODOMODA tiene sucursales distribuidas en los estados de la región. En una de las tablas de registro de las sucursales, hay una columna que contiene la información de a qué estado pertenece: estados =['CMX', 'OAX', 'PUE', 'PUE', 'CMX', 'PUE', 'OAX', 'OAX', 'OAX', 'CMX', 'CMX', 'PUE', 'OAX', 'CMX', 'VER', 'PUE', 'VER', 'CMX', 'PUE', 'CMX', 'OAX', 'CMX', 'PUE'].

La empresa siempre está abriendo nuevas sucursales, por lo que la tabla está constantemente recibiendo nuevos registros y al gerente le gustaría tener la información actualizada de la cantidad de sucursales en cada estado.

A partir de la columna con la información de los estados, crea un diccionario utilizando la comprensión de diccionarios (dict comprehension) con la clave siendo el nombre de un estado y el valor siendo la cantidad de veces que aparece el estado en la lista.

Mi sugerencia es que puedes hacer un paso intermedio para generar una lista de listas en la que cada una de las listas tenga el nombre de solo un estado con valores repetidos.

'''
estados =['CMX', 'OAX', 'PUE', 'PUE', 'CMX', 'PUE', 'OAX', 'OAX', 'OAX', 'CMX', 'CMX', 'PUE', 'OAX', 'CMX', 'VER', 'PUE', 'VER', 'CMX', 'PUE', 'CMX', 'OAX', 'CMX', 'PUE']

conteo = {estado: estados.count(estado) for estado in estados}

print(conteo)



'''10.- En esa misma tabla de registro de sucursales, hay una columna con la información de la cantidad de personas empleadas y el gerente quisiera tener un agrupamiento de la suma de esas personas para cada estado. Las informaciones contenidas en la tabla son:

 empleados = [('CMX', 16), ('OAX', 8), ('PUE', 9), ('PUE', 6), ('CMX', 10), ('PUE', 4), ('OAX',9),  ('OAX', 7), ('OAX', 12), ('CMX', 7), ('CMX', 11), ('PUE',8), ('OAX',8), ('CMX',9), ('VER', 13), ('PUE', 5),  ('VER', 9), ('CMX', 12), ('PUE', 10), ('CMX', 7), ('OAX', 14), ('CMX', 10), ('PUE', 12)]

A partir de la lista de tuplas, crea un diccionario en el que las claves son los nombres de los estados únicos y los valores son las listas con el número de empleados referentes al estado. También crea un diccionario en el que las claves son los nombres de los estados y los valores son la suma de empleados por estado.'''

empleados = [('CMX', 16), ('OAX', 8), ('PUE', 9), ('PUE', 6), ('CMX', 10), ('PUE', 4), ('OAX',9),  ('OAX', 7), ('OAX', 12), ('CMX', 7), ('CMX', 11), ('PUE',8), ('OAX',8), ('CMX',9), ('VER', 13), ('PUE', 5),  ('VER', 9), ('CMX', 12), ('PUE', 10), ('CMX', 7), ('OAX', 14), ('CMX', 10), ('PUE', 12)]


estados_unicos = list(set([tupla[0] for tupla in empleados]))


lista_de_listas = []
for estado in estados_unicos:
    lista = [tupla[1] for tupla in empleados if tupla[0] == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)


agrupamiento_por_estado = {estados_unicos[i]: lista_de_listas[i] for i in range(len(estados_unicos))}
print(agrupamiento_por_estado)


suma_por_estado = {estados_unicos[i]: sum(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(suma_por_estado)