numero=(int(input("Digite o número = ")))

if (numero % 2 != 0 ):
    print(" {} é impar" .format(numero))
else:
    print(" {} não é impar" .format(numero))
if(numero % 3 == 0):
    print(" {} é múltiplo de 3" .format(numero))
else:
    print(" {} não é múltiplo de 3" .format(numero))
if( 102 % numero == 0):
    print(" {} é divisor de 102" .format(numero))
else:
    print(" {} não é divisor de 102" .format(numero))
        
