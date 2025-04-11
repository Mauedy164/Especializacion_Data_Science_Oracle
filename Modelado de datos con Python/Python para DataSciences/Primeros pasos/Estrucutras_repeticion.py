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
factorial = 1 

for n in range(1, num+1):
    factorial *= n 
print(f'El factorial de {num} es {factorial}')

'''6 - Escribe un programa que genere la tabla de multiplicar de un número entero del 1 al 10, según la elección del usuario. Como ejemplo, para el número 2, la tabla de multiplicar debe mostrarse en el siguiente formato:

Tabla de multiplicar del 2:
2 x 1 = 2
2 x 2 = 4
[...]
2 x 10 = 20

'''
print('Bienvenido a tablas de multiplicación')


tabla = int(input('Escribe un número entero entre el 1 y el 10 para conocer su tabla de multiplicación: '))
while (1> tabla or tabla > 10):
    tabla = int(input('El número está fuera del rango de 1 y 10, intenta de nuevo: '))    

for n in range(1, 11):
    multiplicacion = tabla * n
    print(f'{tabla} x {n} = {multiplicacion}')


'''7 - Los números primos tienen diversas aplicaciones en Ciencia de Datos, como en criptografía y seguridad. Un número primo es aquel que es divisible solo por sí mismo y por 1. Por lo tanto, crea un programa que solicite un número entero y determine si es un número primo o no.'''

num = int(input('Ingresa un número: '))
contador = 0


for n in range(1 , num+1):
    if contador > 2:
        print('No es un número primo')
        break
    elif (num % n) == 0:
        contador +=1
    else: 
        continue
if contador <= 2:
    print('Es un número primo')


'''8 - Vamos a comprender la distribución de edades de los pensionistas de una empresa de seguros. Escribe un programa que lea las edades de una cantidad no informada de clientes y muestre la distribución en los intervalos [0-25], [26-50], [51-75] y [76-100]. La entrada de datos se detendrá al ingresar un número negativo.'''


rango_1 = 0
rango_2 = 0
rango_3 = 0
rango_4 = 0

while True:
    try:
        edad = int(input('Ingresa la edad (Da un número negativo para detener el flujo): '))
        if edad < 0:
            break
        if 0<= edad <= 25:
            rango_1 +=1
        elif 26<= edad <= 50:
            rango_2 +=1
        elif 51<= edad <= 75:
            rango_3 +=1
        elif 76<= edad <= 100:
            rango_4 +=1
        elif edad >= 100:
            print('No se admiten personas mayores de 100 años')
    except ValueError:
        print('Ingresa un número entero')

print(f'Rango [0-25] = {rango_1} personas')
print(f'Rango [26-50] = {rango_2} personas')
print(f'Rango [51-75] = {rango_3} personas')
print(f'Rango [76-100] = {rango_4} personas')

'''9 - En una elección para la gerencia de una empresa con 20 empleados, hay cuatro candidatos. Escribe un programa que calcule al ganador de la elección. La votación se realizó de la siguiente manera:

Cada empleado votó por uno de los cuatro candidatos (representados por los números 1, 2, 3 y 4).

También se contaron los votos nulos (representados por el número 5) y los votos en blanco (representados por el número 6).

Al final de la votación, el programa debe mostrar el número total de votos para cada candidato, los votos nulos y los votos en blanco. Además, debe calcular y mostrar el porcentaje de votos nulos con respecto al total de votos y el porcentaje de votos en blanco con respecto al total de votos.

Si necesitas ayuda, las soluciones a las actividades están disponibles en la sección Opinión del instructor'''

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0

voto_blanco = 0
voto_nulo= 0
try:
    voto = int(input('Ingresa el número de tu candidato (1. Lalo, 2. Juan, 3. Monse, 4. Guille, 5. Nulo, 6. Blanco): '))
    for n in range (1, 5):
        try: 
            while 1<= voto >= 6:
                voto = int(input('Ingresa el número de tu candidato (1. Lalo, 2. Juan, 3. Monse, 4. Guille, 5. Nulo, 6. Blanco: )'))
            if voto == 1:
                candidato_1 += 1
            elif voto == 2:
                candidato_2 +=1
            elif voto == 3:
                candidato_3 +=1
            elif voto == 4:
                candidato_4 +=1
            elif voto == 5:
                voto_nulo +=1
            elif voto == 6:
                voto_blanco +=1
        except:
            print('Dato invalido. Ingresa un valor del 1-6')
except:
    print
porcentaje_nulo = (voto_nulo/20)*100
porcentaje_blanco= (voto_blanco/20)*100
print(f'El candidato 1. Lalo tuvo {candidato_1} votos')
print(f'El candidato 2. Juan tuvo {candidato_2} votos')
print(f'El candidato 3. Monse tuvo {candidato_3} votos')
print(f'El candidato 4. Guille tuvo {candidato_4} votos')
print(f'Exisiteron {voto_nulo} votos nulos, siendo estos el {porcentaje_nulo}% de los votos totales')
print(f'Exisiteron {voto_blanco} votos blancos, siendo estos el {porcentaje_blanco}% de los votos totales')
    