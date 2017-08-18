setor=(str.lower(input("Qual setor = ")))
tipoingre=(str.lower(input("Tipo de Ingresso = ")))

plateiavip= 350.0
cadeira= 200.0
arquibancada= 100.0

if(tipoingre == "inteira"):

    if(setor == "arquibancada"):
        valorfinal= ((arquibancada * 0.05) + arquibancada)

    elif(setor == "plateia vip"):
        valorfinal= ((plateiavip * 0.05) + plateiavip)

    elif(setor == "cadeira"):
        valorfinal= ((cadeira * 0.05) + cadeira)

    else:
        print("Setor Inválido")

elif(tipoingre == "meia"):

    if(setor == "arquibancada"):
        valor= ((arquibancada * 0.05) + arquibancada)
        valorfinal= (valor - (arquibancada * 0.50))

    elif(setor == "plateia vip"):
        print("Tipo de ingresso inválido")

    elif(setor == "cadeira"):
        valor= ((cadeira * 0.05) + cadeira)
        valorfinal= (valor - (cadeira * 0.50))
    else:
        print("Setor Inválido")

print("R$ {}" .format(valorfinal))

    
