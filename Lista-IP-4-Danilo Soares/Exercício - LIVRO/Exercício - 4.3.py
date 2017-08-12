numeroa=(int(input("Digite um número = ")))
numerob=(int(input("Digite um número = ")))
numeroc=(int(input("Digite um número = ")))


if (numeroa > numerob) and (numeroa > numeroc):
    maior= numeroa

elif (numerob > numeroa) and (numerob > numeroc):
    maior= numerob

elif (numeroc > numeroa) and (numeroc > numerob):
    maior= numeroc

if (numeroa < numerob) and (numeroa < numeroc):
    menor= numeroa

elif (numerob < numeroa) and (numerob < numeroc):
    menor= numerob

elif (numeroc < numeroa) and (numeroc < numerob):
    menor= numeroc

print("O maior é {}, e o menor é {}" .format(maior,menor))
