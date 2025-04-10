for n in range(1, 16):
    calificacion = int(input('Ingresa una calificación del 0 al 5: '))
    while calificacion<0 or calificacion>5:
        calificacion = int(input('Datos no válido, debes ingresar un valor entre 0 y 5: '))
    print(f'Calificación {n}. {calificacion}')