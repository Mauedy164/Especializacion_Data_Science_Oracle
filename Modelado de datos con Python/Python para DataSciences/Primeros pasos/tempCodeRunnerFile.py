lista_ventas = {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

ventas = lista_ventas.values()
total_ventas = sum(lista_ventas.values())
mas_vendido = max(ventas)
print(f'El producto más vendido fue {mas_vendido}')
print(f'El total de ventas fue de {total_ventas} ventas')