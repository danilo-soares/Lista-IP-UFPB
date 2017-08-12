                                ##Algoritmo - 16
a=(float(input("Digite a hora de início = ")))
b=(float(input("Digite a hora do término = ")))

if(a > 12.00 and a < 24.00 ):
    c = ((a - 24.00)*-1)
    res= (c + b)
    
    print("O jogo durou %s hora(s) !" %(res))
else:
    res = (b - a)
    print("O jogo durou %s hora(s) !" %(res))


