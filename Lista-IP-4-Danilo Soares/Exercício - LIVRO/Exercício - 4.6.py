distancia=(float(input("Digite a distância que o usuário deseja percorrer = ")))

if(distancia <= 200):
    valorfinal= (distancia * 0.50)
    
elif(distancia > 200):
    valorfinal= (distancia * 0.45)

print("O valor da passagem é de {}" .format(valorfinal))
