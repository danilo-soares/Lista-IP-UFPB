numeroa=(int(input("Digite um número = ")))
numerob=(int(input("Digite um número = ")))
operacao=(str.lower(input("Digite qual a operação desejada = ")))

if (operacao == "soma"):
    valor = (numeroa + numerob)
    
elif (operacao == "subtração"):
    valor = (numeroa - numerob)
    
elif (operacao == "multiplicação"):
    valor = (numeroa * numerob)
    
elif (operacao == "divisão"):
    valor = (numeroa / numerob)
    
else:
    print("Você digitou ({}). Falta o Acento " .format(operacao))

print("O resultado da sua operação é {}" .format(valor))

