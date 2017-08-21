# Programa para ler 20 números e
# exibir a soma dos pares.
cont = 20
soma=0
while (cont > 0):
    numero = int(input())
    if (numero % 2 == 0):
        soma += numero 
    cont -= 1
print(soma)

#O programa anterior não executava por alguns fatores, um deles é que a condição
#do while esta invertida então ele entraria em um loop infinito, outro problema
#é que ele não estava somando so atribuando o valor de numero a soma 
