numero=int(input("Digite o número -> "))
soma=0
total=0

while numero != 0:

    soma += numero
    total += 1
    media = soma/total
    numero=int(input("Digite o número -> "))

print("Números Digitados -> {}" .format(total))
print("Soma -> {}" .format(soma))
print("Média -> {:.2f}" .format(media))
