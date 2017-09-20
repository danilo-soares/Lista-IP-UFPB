titulo=(input("Título das Revistas = "))
cont=0
valor=0

while titulo != "FIM" or titulo != "fim":
    titulo=str(input("Título das Revistas = "))

    if editora == "globo":
        cont+=1

    if revistas > 100:
        valor += preco
        media= valor/100
