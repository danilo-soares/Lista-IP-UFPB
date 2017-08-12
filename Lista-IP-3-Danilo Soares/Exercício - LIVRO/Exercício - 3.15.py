qntcigarros = int(input("Quantos cigarros fumados por dia = "))
anosfumando = int(input("Quantos anos fumando = : "))

total = (anosfumando * 365)*qntcigarros
diasperdidos = (total * 10) /60*24

print (" Você já perdeu {:.2f} dias :( !" .format(diasperdidos) )
