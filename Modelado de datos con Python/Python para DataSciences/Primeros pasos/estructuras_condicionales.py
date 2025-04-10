##Entrenando la programación##

###################################################################################################
'''
1 - Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el número más grande.
'''

num_1 = float(input('Ingresa el primer valor: '))
num_2 = float(input('Ingresa el segundo valor: '))

if num_1 > num_2:
    print(f'El número mayor es {num_1}')
else:
    print(f'El número mayor es {num_2}')

####################################################################################################

'''2 - Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa e informe si hubo un crecimiento (porcentaje positivo) o una disminución (porcentaje negativo).'''

crecimiento = float(input('Dime el porcentaje de crecimiento de producción: '))

if crecimiento > 0:
    print('El crecimiento fue positivo')
elif crecimiento == 0:
    print('La empresa se mantuvo igual')
else:
    print('El crecimiento fue negativo')

################################################################################################
'''3 - Escribe un programa que determine si una letra proporcionada por la persona usuaria es una vocal o una consonante.'''

letra = input('Ingresa una letra: ')
letra = letra.lower()

vocal = ('a', 'e', 'i', 'o', 'u')

cantidad = len(letra)

if cantidad > 1:
    print('Sólo debes poner una letra, intenta de nuevo')
else:
    if letra in vocal:
        print('Tu letra es una vocal')
    else:
        print('Tu letra es una consonante')

##############################################################################################

'''4 - Escribe un programa que lea valores promedio de precios de un modelo de automóvil durante 3 años consecutivos y muestre el valor más alto y más bajo entre esos tres años.'''

año_1 = float(input('Dame le valor del primer año: '))
año_2 = float(input('Dame le valor del segundo año: '))
año_3 = float(input('Dame le valor del tercer año: '))

print(f'El valor máximo fue {max(año_1, año_2, año_3)} y el valor mínimo fue {min(año_1, año_2, año_3)}')

################################################################################################

'''5 - Escribe un programa que pregunte sobre el precio de tres productos e indique cuál es el producto más barato para comprar.'''

precio_1 = float(input('Escribe el precio del primer producto: '))
precio_2 = float(input('Escribe el precio del segundo producto: '))
precio_3 = float(input('Escribe el precio del tercer producto: '))

print(f'El producto más barato es el que cuesta {min(precio_1,precio_2,precio_3)}')

###########################################################################################
'''6 - Escribe un programa que lea tres números y los muestre en orden descendente.'''

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))

if (num1 >= num2) and (num1 >= num3):
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif (num2 >= num1) and (num2 >= num3):
    print(num2)
    if num1 >= num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else:
    print(num3)
    if num1 >= num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)

##############################################################################################
'''7 -Escribe un programa que pregunte en qué turno estudia la persona usuaria ("mañana", "tarde" o "noche") y muestre el mensaje "¡Buenos Días!", "¡Buenas Tardes!", "¡Buenas Noches!" o "Valor Inválido!", según el caso.'''

turno = input('¿En qué horario estudias? (mañana, tarde o noche): ')
turno = turno.lower().strip()

if turno == 'mañana':
    print('¡Buenos Días!')
elif turno == 'tarde':
    print('¡Buenas Tardes!')
elif turno == 'noche':
    print('¡Buenas Noches!')
else:
    print('¡Valor Inválido!')


###################################################################################################
'''8 - Escribe un programa que solicite un número entero a la persona usuaria y determine si es par o impar. Pista: Puedes usar el operador módulo (%).'''

numero = float(input('Escribe un número: '))

if numero % 2 == 0:
    print('Tu numero es par')
elif numero % 2 != 0:
    print('Tu numero es impar')
else:
    print('Número invalido')

#############################################################################################
'''9 - Escribe un programa que pida un número a la persona usuaria y le informe si es entero o decimal.'''

numero = float(input('Ingresa un número: '))
numero_entero= int(numero)
print(numero - numero_entero)

if numero - numero_entero > 0:
    print('Tu numero es decimal')
else:
    print('tu numero es entero') 

######Momento de los proyectos##########

'''10 - Un programa debe ser escrito para leer dos números y luego preguntar a la persona usuaria qué operación desea realizar. El resultado de la operación debe incluir información sobre el número, si es par o impar, positivo o negativo, e entero o decimal.'''

print('Bienvenido a la calculadora de dos números')
num1 = float(input('Por favor, ingresa el primer valor: '))
num2 = float(input('Por favor, ingresa el segundo valor: '))

operacion = input('¿Qué operación deseas realizar? (multiplicacion, division, suma, resta): ')
operacion.lower().strip().replace('ó', 'o')

if operacion == 'multiplicacion' or operacion == '*':
    resultado = num1 * num2
    resultado_entero = int(resultado)
    print(f'El resultado de la multipliación es: {resultado}')
    if resultado % 2 == 0:
        print('Es un número par')
    else:
        print('Es un número impar')
    if resultado > 0:
        print('Es un número positivo')
    else: 
        print('Es un número negativo')
    if (resultado - resultado_entero) > 0:
        print('Es un número decimal')
    else: 
        print('Es un número entero')
elif operacion == 'division' or operacion == '/':
    resultado = num1 / num2
    resultado_entero = int(resultado)
    print(f'El resultado de la división es: {resultado}')
    if resultado % 2 == 0:
        print('Es un número par')
    else:
        print('Es un número impar')
    if resultado > 0:
        print('Es un número positivo')
    else: 
        print('Es un número negativo')
    if (resultado - resultado_entero) > 0:
        print('Es un número decimal')
    else: 
        print('Es un número entero')
elif operacion == 'suma' or operacion == '+':
    resultado = num1 + num2
    resultado_entero = int(resultado)
    print(f'El resultado de la suma es: {resultado}')
    if resultado % 2 == 0:
        print('Es un número par')
    else:
        print('Es un número impar')
    if resultado > 0:
        print('Es un número positivo')
    else: 
        print('Es un número negativo')
    if (resultado - resultado_entero) > 0:
        print('Es un número decimal')
    else: 
        print('Es un número entero')
elif operacion == 'resta' or operacion == '-':
    resultado = num1 - num2
    resultado_entero = int(resultado)
    print(f'El resultado de la resta es: {resultado}')
    if resultado % 2 == 0:
        print('Es un número par')
    else:
        print('Es un número impar')
    if resultado > 0:
        print('Es un número positivo')
    else: 
        print('Es un número negativo')
    if (resultado - resultado_entero) > 0:
        print('Es un número decimal')
    else: 
        print('Es un número entero')
else:
    print('Operación no valida')

##################################################################

'''11 - Escribe un programa que pida a la persona usuaria tres números que representan los lados de un triángulo. El programa debe informar si los valores pueden utilizarse para formar un triángulo y, en caso afirmativo, si es equilátero, isósceles o escaleno. Ten en cuenta algunas sugerencias:

Tres lados forman un triángulo cuando la suma de cualesquiera dos lados es mayor que el tercero;
Triángulo Equilátero: tres lados iguales;
Triángulo Isósceles: dos lados iguales;
Triángulo Escaleno: tres lados diferentes.'''

lado1 = float(input('Ingresa la medida en cm del primer lado: '))
lado2 = float(input('Ingresa la medida en cm del segundo lado: '))
lado3 = float(input('Ingresa la medida en cm del tercer lado: '))

if  ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado3 + lado2) > lado1):
    triangulo = True
else:
    triangulo = False

print(triangulo)

if triangulo:
    if lado1 == lado2 == lado3:
        print('Es un triángulo equilatero')
    elif lado1 == lado2 or lado2== lado3 or lado1== lado3:
        print('Es un triángulo isóseles')
    elif lado1 != lado2 and lado1 != lado3 and lado2!= lado3:
        print('Es un triángulo escaleno')
else:
    print('Datos inválidos, no es posible formar un triángulo')
#################################################################################################

'''12 - Un establecimiento está vendiendo combustibles con descuentos variables. Para el etanol, si la cantidad comprada es de hasta 15 litros, el descuento será del 2% por litro. En caso contrario, será del 4% por litro. Para el diésel, si la cantidad comprada es de hasta 15 litros, el descuento será del 3% por litro. En caso contrario, será del 5% por litro. El precio por litro de diésel es de R$ 2,00 y el precio por litro de etanol es de R$ 1,70. Escribe un programa que lea la cantidad de litros vendidos y el tipo de combustible (E para etanol y D para diésel) y calcule el valor a pagar por el cliente. Ten en cuenta algunas sugerencias:

El valor del descuento será el producto del precio por litro, la cantidad de litros y el valor del descuento.
El valor a pagar por un cliente será el resultado de la multiplicación del precio por litro por la cantidad de litros menos el valor del descuento resultante del cálculo.'''

precio_d = 2.00
precio_e = 1.7

descuento_alto_e = 0.04
descuento_bajo_e = 0.02

descuento_alto_d = 0.05
descuento_bajo_d = 0.03

venta_e = float(input('¿Cuántos litros de etanol va a comprar? En caso de que no lleve ninguno, marque 0: '))
venta_d = float(input('¿Cuántos litros de diésel va a comprar? En caso de que no lleve ninguno, marque 0: '))

if venta_e <= 15:
    costo_e = (venta_e * precio_e) * (1-descuento_bajo_e)
    print(venta_e*precio_e)
    print('Aplica descuento de 2%')
    print(f'Costo después de descuento {costo_e}')
else:
    costo_e = (venta_e * precio_e) * (1-descuento_alto_e)
    print(venta_e*precio_e)
    print('Aplica descuento de 4%')
    print(f'Costo después de descuento {costo_e}')
if venta_d <= 15:
    costo_d = (venta_d * precio_d) * (1-descuento_bajo_d)
    print(venta_d*precio_d)
    print('Aplica descuento de 3%')
    print(f'Costo después de descuento {costo_d}')
else:
    costo_d = (venta_d * precio_d) * (1-descuento_alto_d)
    print(venta_d*precio_d)
    print('Aplica descuento de 5%')
    print(f'Costo después de descuento {costo_d}')

costo_final = costo_d + costo_e 
print(f'El costo final es de ${costo_final}')

##########################################################################################################

'''13 - En una empresa de venta de bienes raíces, debes crear un código que analice los datos de ventas anuales para ayudar a la dirección en la toma de decisiones. El código debe recopilar los datos de cantidad de ventas durante los años 2022 y 2023 y calcular la variación porcentual. A partir del valor de la variación, se deben proporcionar las siguientes sugerencias:

Para una variación superior al 20%: bonificación para el equipo de ventas.
Para una variación entre el 2% y el 20%: pequeña bonificación para el equipo de ventas.
Para una variación entre el 2% y el -10%: planificación de políticas de incentivo a las ventas.
Para bonificaciones inferiores al -10%: recorte de gastos.'''

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