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