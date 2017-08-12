                                     ##Algoritmo - 12

a=(float(input("Digite a primeira nota = ")))
b=(float(input("Digite a segunda nota = ")))
c=(float(input("Digite a terceira nota = ")))

res=((a+b+c)/3)

if (res < 6):
    print("Sua nota é %s e Você está REPROVADO!" %(res))
else:
    print("Sua nota é %s e Você está APROVADO!" %(res))
