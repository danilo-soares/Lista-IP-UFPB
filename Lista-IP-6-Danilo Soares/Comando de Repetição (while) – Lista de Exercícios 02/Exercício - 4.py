numero=int(input())
cont=0
res=0

while numero != 100:

    if numero > 0 and numero % 2 == 0:
        cont += 1
        res += numero
        valor= res//cont
    else:
        valor=("Não recebidos números válidos")
    numero=int(input())

print(valor)

        


