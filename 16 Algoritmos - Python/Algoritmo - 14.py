                                   ##Algoritmo - 14
a=(int(input("Digite sua idade = ")))

while(a >= 5):
    if(a >= 5 and a <= 7):
        print("Infantil A")
        break
    elif(a >= 8 and a <= 10):
        print("Infantil B")
        break
    elif(a >= 11 and a <= 13):
        print("Juvenil A")
        break
    elif(a >= 14 and a <= 17):
        print("Juvenil B")
        break
    elif(a >= 18):
        print("Adulto")
        break
