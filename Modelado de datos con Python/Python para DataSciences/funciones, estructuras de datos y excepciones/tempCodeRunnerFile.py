glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
rangos = ['Hipoglicemia','Normal','Alterada','Diabetes']

rangos_glicemia = [(rangos[i], glicemia[i]) for i in range(len(glicemia))]

print(rangos_glicemia)