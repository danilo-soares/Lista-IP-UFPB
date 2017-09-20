quantidade=4
lista=[]
soma=[]
for i in range(quantidade):
    lista.append(int(input("Digite um número = ")))
print(lista)

for i in range(len(lista)-1):
    
    soma.append(lista[i]+lista[i+1])

soma.append(lista[-1])

print(soma)
