nota=[]
cont=0

for i in range(5):
    notas=float(input("Digite as Notas = "))
    if notas > 8:
        cont+=1
nota.append(cont)

for i in nota:
    print(i,end="")
        

