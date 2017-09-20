def calculaValorVoo (destino,turno):
    destino=str.lower(destino)
    turno=str.lower(turno)
    if turno == "diurno":
        if destino == "natal":
            valortotal = 80
        elif destino == "recife":
            valortotal = 100
        else:
            valortotal = "Destino Inválido"
    elif turno == "noturno":
        if destino == "fortaleza":
            valortotal= 180
        elif destino == "recife":
            valortotal = 90
        else:
            valortotal = "Destino Inválido"
    else:
        valortotal= "Horário Inválido"
    return valortotal

def validaDadosVoo (destino,turno):
    destino=str.lower(destino)
    turno=str.lower(turno)
    if turno == "diurno":
        if destino == "natal" or destino == "recife":
            return True
        else:
            return False
    elif turno == "noturno":
        if destino == "fortaleza" or destino == "recife":
            return True
        else:
            return False
    else:
        return False
        
