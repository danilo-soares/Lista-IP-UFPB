								##Exercício - 3.9
dias=(int(input("Digite quantos dias = ")))
horas=(int(input("Digite quantas horas = ")))
minutos=(int(input("Digite quantos minutos = ")))
segundos=(int(input("Digite quantos segundos = ")))

dias=(dias * 84600)
horas=(horas * 3600)
minutos=(minutos * 60)

res= (dias+horas+minutos+segundos)

print(" São {} segundos !" .format(res))
