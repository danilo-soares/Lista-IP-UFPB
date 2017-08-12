                                ##Algortimo - 8
a=float(input("Digite a quantidade de dias = "))

anos = (int)(a / 365)
meses = (int)((a % 365) /30)
dias = (int)((a % 365) % 30)


print("%s anos, %s meses e %s dias." %(anos,meses,dias))
