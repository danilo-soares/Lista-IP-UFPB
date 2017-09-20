import bibli3
veiculo=input("Veículo -> ")
horas=int(input("Horas -> "))
minutos=int(input("Minutos -> "))

valor= bibli3.calculaEstacionamento (veiculo,horas,minutos)

print("Valor -> {:.2f}" .format(valor))
