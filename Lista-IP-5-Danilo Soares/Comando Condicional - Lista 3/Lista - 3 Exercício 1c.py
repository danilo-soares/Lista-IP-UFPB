#O programa deve receber como entrada três números inteiros e exibir
#qual o maior deles. (Dica: desconsidere a possibilidade de números iguais
#na entrada)

# Ao meu ver não é necessaŕio 3 if, um if, um elif e um else já resolvem o problema
#pois com tres if causa redundância

a=int(input("Digite um número = "))
b=int(input("Digite um número = "))
c=int(input("Digite um número = "))

if (a>b) and (a>c):
    print(a)
elif (b>a) and (b>c):
    print(b)
else:
    print(c)
