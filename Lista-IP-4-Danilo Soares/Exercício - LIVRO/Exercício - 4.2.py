velocidade=(float(input("Digite a velocidade do veículo = ")))

if (velocidade > 80):
    valor= (velocidade - 80)
    valorfinal= (valor * 5)
    print("Você foi multado, o valor da multa é R$ {} !" .format(valorfinal))
else:
    print("Você não foi multado !")
