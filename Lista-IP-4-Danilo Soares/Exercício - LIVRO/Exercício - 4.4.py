salario=(float(input("Digite o salário = ")))

if(salario > 1250):
    valorfinal= ((salario * 0.10) + salario)

elif(salario <= 1250):
    valorfinal= ((salario * 0.15) + salario)

print("Seu salário com aumento é R$ {}" .format(valorfinal))
