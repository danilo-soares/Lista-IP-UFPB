                                    ##Algoritmo - 10

a=(int(input("Digite os segundos = ")))

horas=(int)(a / 3600)
minutos= (int)((a % 3600)/60)
segundos= ((a % 3600) % 60)

print("%s horas, %s minutos, %s segundos." %(horas,minutos,segundos))
