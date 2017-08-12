kwconsumida=(float(input("Quantos kWh foram consumidas = ")))
tipodeinstal=(str.lower(input("Qual tipo de instalação = ")))

if(tipodeinstal == "r"):

    if(kwconsumida <= 500):
        res= (kwconsumida * 0.40)
        
    else:
        res= (kwconsumida * 0.65)
        
    print("O valor da sua conta será de R$ {}" .format(res))        

elif(tipodeinstal == "c"):

    if(kwconsumida <= 1000):
        res= (kwconsumida * 0.55)
        
    else:
        res= (kwconsumida * 0.60)
        
    print("O valor da sua conta será de R$ {}" .format(res))

elif(tipodeinstal == "i"):

    if(kwconsumida <= 5000):
        res= (kwconsumida * 0.55)

    else:
        res= (kwconsumida * 0.60)

    print("O valor da sua conta será de R$ {}" .format(res))

else:

    print("Não existi este tipo de instalação")
