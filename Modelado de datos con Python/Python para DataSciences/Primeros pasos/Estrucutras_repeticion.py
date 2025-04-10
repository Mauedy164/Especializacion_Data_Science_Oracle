'''1 - Escribe un programa que solicite dos números enteros e imprima todos los números enteros entre ellos.'''
print('Bienvenido al contador, deberás ingresar dos valores y te diré todos los números enteros que se encuentran entre ellos')
num1 = int(input('Ingresa el valor más bajo: '))
num2 = int(input('Ingresa el valor más alto: '))

for n in range(num1, num2+1):
    print(n)


'''2 - Escribe un programa para calcular cuántos días tomará que la colonia de una bacteria A supere o iguale a la colonia de una bacteria B, basado en tasas de crecimiento del 3% y 1.5%, respectivamente. Supón que la colonia A comienza con 4 elementos y B con 10.'''
print('Bienvenido')
colonia_A = 4
colonia_B = 10
dia=0

while colonia_A <= colonia_B:
    colonia_A+= (colonia_A*0.03)
    colonia_B+= (colonia_B*0.015)
    print(f'La colonia A = {colonia_A} UFC')
    print(f'La colonia B = {colonia_B} UFC')
    dia+=1
    print(dia)

'''3 - Para procesar una cantidad de 15 datos de evaluaciones de usuarios de un servicio de la empresa, necesitamos verificar si las calificaciones son válidas. Por lo tanto, escribe un programa que recibirá calificaciones del 0 al 5 y verificará si son valores válidos. Si se ingresa una calificación superior a 5 o inferior a 0, se repetirá hasta que el usuario ingrese un valor válido.'''



for n in range(1, 16):
    calificacion = int(input('Ingresa una calificación del 0 al 5: '))
    while calificacion<0 or calificacion>5:
        calificacion = int(input('Datos no válido, debes ingresar un valor entre 0 y 5: '))
    print(f'Calificación {n}. {calificacion}')

'''5 - Escribe un programa que calcule el factorial de un número entero proporcionado por el usuario. Recuerda que el factorial de un número entero es el producto de ese número por todos sus antecesores hasta llegar al número 1. Por ejemplo, el factorial de 5 es 5 x 4 x 3 x 2 x 1 = 120.'''

num = int(input('Ingresa el número para calcular su factorial: '))

while num > 0:
    factorial = num * num-1
    num