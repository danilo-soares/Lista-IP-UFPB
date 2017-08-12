                                    ##Algoritmo - 10
a=(int(input("Digite os segundos = ")))

horas=(int)(a / 3600)
resto=(a % 3600)

minutos= (int)(resto / 60)
resto= (resto % 60)

segundos= (resto)

print(" {} horas, {} minutos, {} segundos." .format(horas,minutos,segundos))
