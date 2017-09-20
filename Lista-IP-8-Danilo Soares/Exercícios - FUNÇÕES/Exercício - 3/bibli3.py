def calculaCondominio (nome,dias):
    nome=str.lower(nome)
    if nome == "duna":
        valor= (300 * 0.02)
        valortotal= (valor*dias)+300
    elif nome == "chateau":
        valor= (450 * 0.04)
        valortotal= (valor*dias)+450
    elif nome == "petit":
        valor= (220 * 0.03)
        valortotal= (valor*dias)+220
    else:
        return "Nome Inválido"

    return valortotal

def calculaEstacionamento (tipo,horas,minutos):
    tipo=str.lower(tipo)
    tempo=round((horas + (minutos/60)+0.49))-5
    if tipo == "moto":
        if horas < 5:
            valortotal= 1.5
        else:
            valortotal= 1.5 + (tempo*1)
    else:

        if horas < 5:
            valortotal= 3
        else:
            valortotal= 3 + (tempo*2)
    return valortotal

