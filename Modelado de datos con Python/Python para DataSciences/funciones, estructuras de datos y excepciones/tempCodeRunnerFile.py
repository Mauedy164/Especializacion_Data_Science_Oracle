empleados = [('CMX', 16), ('OAX', 8), ('PUE', 9), ('PUE', 6), ('CMX', 10), ('PUE', 4), ('OAX',9),  ('OAX', 7), ('OAX', 12), ('CMX', 7), ('CMX', 11), ('PUE',8), ('OAX',8), ('CMX',9), ('VER', 13), ('PUE', 5),  ('VER', 9), ('CMX', 12), ('PUE', 10), ('CMX', 7), ('OAX', 14), ('CMX', 10), ('PUE', 12)]


#Diccionario en el que las claves son los nombres de los estados únicos y los valores son las listas con el número de empleados referentes al estado.

# Almacenando los estados sin repetición de valor
estados_unicos = list(set([tupla[0] for tupla in empleados]))

# Creando una lista de listas con valores de empleados de cada estado
lista_de_listas = []
for estado in estados_unicos:
    lista = [tupla[1] for tupla in empleados if tupla[0] == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

# Creando un diccionario con datos agrupados de empleados por estado
agrupamiento_por_estado = {estados_unicos[i]: lista_de_listas[i] for i in range(len(estados_unicos))}
print(agrupamiento_por_estado)

# Creando un diccionario con la suma de empleados por estado
suma_por_estado = {estados_unicos[i]: sum(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(suma_por_estado)