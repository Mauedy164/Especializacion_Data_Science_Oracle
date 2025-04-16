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