import abada
cont=0
comissarios=[]

for i in range(10):
    quantidade=int(input("Quantidades de Abadas Vendidos -> "))
    comissarios.append(quantidade)
    cont += quantidade
    valor=abada.calculaComissao(quantidade)
    total=abada.calculaBonus(quantidade)
    print("Comissão -> {:.2f}" .format(valor))
    print("Bônus -> {}" .format(total))
    print(20*"*")
print("Total de Abadas -> {}" .format(cont))
print(20*"*")
numero=1

for i in comissarios:
    print("O {}º comissário vendeu -> {} Abadas" .format(numero,i))
    numero+=1
    
