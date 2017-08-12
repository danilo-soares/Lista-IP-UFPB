                                        #Algoritmo - 15
a=(int(input("Digite o valor = ")))

cem=(int)(a/100)
cinquenta=(int)((a%100)/50)
dez=(int)(((a%100)%50)/10)
cinco=(int)((((a%100)%50)%10)/5)
um=((((a%100)%50)%10)%5)

print("O valor de %s pode ser retirado com as seguintes notas %s de cem, %s de cinquenta, %s de dez, %s de cinco, %s de um" % (a,cem,cinquenta,dez,cinco,um))
