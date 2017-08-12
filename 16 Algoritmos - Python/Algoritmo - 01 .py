a=int(input("Insira um numero"))
b=int(input("Insira um numero"))
cont=0
r=a
while(b<=r):
    
    if a == 0 or b ==0 :
        
        print("Nao sera possivel a divisao")
        break

    else:
        
        if(b > r):
            print("O resultado da divisao eh %d e o resto %r"%(cont,r))
            
        else:
            r= r-b
            cont+=1

print("O resultado da divisao eh %d e o resto %r"%(cont,r))

            
    
