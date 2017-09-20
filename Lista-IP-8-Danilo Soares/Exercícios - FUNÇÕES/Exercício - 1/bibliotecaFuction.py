def testaVogal (letra):
    letra= str.lower(letra)
    if letra == "a" or letra == "b" or letra == "c" or letra == "d" or letra == "e":
        return True
    else:
        return False

def calculaMaior (numero,numerob):
    if numero > numerob:
        return numero
    else:
        return numerob

def testaMultiplo4 (numero):
    if numero % 4 == 0:
        return True
    else:
        return False

def testaDivisor (numero,numerob):
    if numero % numerob == 0:
        return True
    else:
        return False
