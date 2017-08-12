#O programa deve receber como entrada a altura de uma pessoa e exibir uma
#mensagem informando se ela é de estatura baixa, mediana ou alta.

# O código tem um erro por que ele colocou o if eo else dentro de um else
#quando na verdade só era necessaŕio colocar um elif.

altura=float(input("Digite sua Altura = "))

if(altura <= 1.40):
    print("Estatura Baixa")
elif(altura < 1.65):
    print("Estatura Mediana")
else:
    print("Estatura Alta")
