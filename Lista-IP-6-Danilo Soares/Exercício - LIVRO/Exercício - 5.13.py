divida= float(input("Digite o valor da dívida = "))
juros= float(input("Digite a quantidade de juros = "))
pgmensal= float(input("Digite o valor a pagar este mês = "))

saldo=divida
mes= 0
jurospg=0

while saldo > 0:
                    
    jurostotal = (saldo * (juros/100))
    porcentagem =jurostotal + saldo

    saldo = porcentagem - pgmensal
    jurospg = jurospg + jurostotal
    mes += 1

    if saldo > 0:
        print("Faltam R$ {:.2f} para quitar sua dívida " .format(saldo))
    else:
        break
   
    pgmensal= float(input("Digite o valor a pagar este mês = "))

pgtotal= divida + jurospg
saldo=saldo*(-1)

if mes > 12:
    anos = mes // 12
    meses = mes % 12
    print ("Seu saldo é de R$ {:.2f}" .format(saldo))
    print ("Foram necessários {} ano(s) e {} mese(s),foram pagos R$ {:.2f}, acréscimo de R$ {:.2f}" .format(anos,meses,pgtotal,jurospg))

else:
    print ("Seu saldo é de R$ {:.2f}" .format(saldo))
    print ("Foram necessários {} meses,foram pagos R$ {:.2f}, acréscimo de R$ {:.2f}" .format(mes,pgtotal,jurospg))

