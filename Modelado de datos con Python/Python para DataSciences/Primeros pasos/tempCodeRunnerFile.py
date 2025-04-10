ventas_2022 = int(input('Ingrese el número de ventas del año 2022: '))
ventas_2023 = int(input('Ingrese el número de ventas del año 2023: '))

diferencia = ((ventas_2023-ventas_2022)/ventas_2022)*100
print(f'La variación fue de: {diferencia}%')

if diferencia >= 20:
    print('bonificación para el equipo de ventas')
elif 2 <= diferencia <= 20:
    print('pequeña bonificación para el equipo de ventas')
elif 2 > diferencia >= -10:
    print('planificación de políticas de incentivo a las ventas')
else:
    print('Recorte de gastos')