quantidade=(int(input("Digite a quantidade de pessoas = ")))

onibus= 42
van= 20


if(quantidade <= 41 ):

    if(quantidade <= 20):
        lotvan= 1
        lotonibus= 0
    else:
        lotvan= 2
        lotonibus= 0

elif(quantidade > 41):
    if(quantidade <= 52):
        lotonibus= quantidade // onibus
        lotvan= 1
    elif(quantidade):
        lotonibus= quantidade // onibus
        lotvan=round((quantidade % onibus)/ van)
        
print("Nessa excurssão vão {} pessoa(s), então vão ser {} ônibus e {} van(s)" .format(quantidade,lotonibus,lotvan))

