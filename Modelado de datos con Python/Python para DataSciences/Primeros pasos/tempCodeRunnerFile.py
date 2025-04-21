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