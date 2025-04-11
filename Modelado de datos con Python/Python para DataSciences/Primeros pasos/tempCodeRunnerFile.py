candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0

voto_blanco = 0
voto_nulo= 0
try:
    voto = int(input('Ingresa el número de tu candidato (1. Lalo, 2. Juan, 3. Monse, 4. Guille, 5. Nulo, 6. Blanco: )'))
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