                                ##Algortimo - 8
a=int(input("Digite a quantidade de dias = "))

anos = (int)(a / 365)
meses = (int)((a % 365) /30)
dias = (int)((a % 365) % 30)


print("São %s ano(s), %s mese(s) e %s dia(s)." %(anos,meses,dias))
