                                    ##Algoritmo - 11
valor=(float(input("Digite o valor do veículo = ")))
distribuidor= 28
imposto= 45

res=((imposto/100.0 * valor) + (distribuidor/100.0 * valor) + valor)
##Pode ser usado qualquer dos dois métodos, mais acho melhor o primeiro pois se for preciso alteração no valor dos impostos so alterar valor da variável.
##res=(valor*1.73)
print("O valor final do veículo é %s " %(res))

