quantidade=8
lista=[]
for i in range(quantidade):
    numero=int(input("Digite um Número : "))
    if numero % 3 == 0:
        lista.append(numero)

for i in lista:
    print(i,end=" ")
