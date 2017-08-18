#O programa deve receber como entrada a altura de uma pessoa e exibir uma
#mensagem informando se ela é de estatura baixa, mediana ou alta.

# No Programa original ele utilizou dois if e dois else, quando no lugar do else
#usaria o elif e depois o else.

altura=float(input("Digite sua Altura = "))

if(altura <= 1.40):
    print("Estatura Baixa")
elif(altura < 1.65):
    print("Estatura Mediana")
else:
    print("Estatura Alta")
