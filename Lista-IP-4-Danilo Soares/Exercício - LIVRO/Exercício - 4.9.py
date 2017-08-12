valorcasa= (float(input("Digite o valor da casa = ")))
salario= (float(input("Digite seu salário = ")))
quantpagar= (float(input("Digite quantos anos vai pagar = ")))

tempo= (quantpagar * 12)
prestacao= (valorcasa//tempo)
limiteprestacao= (salario * 0.30)


if(prestacao <= limiteprestacao):
    print("O valor da sua prestação vai ser de {}, durante {} mese(s)" .format(prestacao,tempo))
else:
    print("Não é possível liberar empréstimo pois sua prestacao seria de {} excedendo o limite de 30% do seu salário" .format(prestacao))

