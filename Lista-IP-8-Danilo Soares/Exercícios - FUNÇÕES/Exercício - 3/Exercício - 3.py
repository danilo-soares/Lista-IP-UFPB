import abada

quantidade=int(input("Quantidade de Abadas Vendidos -> "))

valor= abada.calculaComissao(quantidade)
total=abada.calculaBonus(quantidade)

print("Comissão -> {:.2f}" .format(valor))
print("Bônus -> {}" .format(total))
