DOCUMENTO="documento"
PACOTE="pacote"
CUSTO_DOC=2
CUSTO_PAC=3
PEQUENA="pequena"
MEDIA="media"
GRANDE="grande"
CUSTO_PEQUENA=4
CUSTO_MEDIA=7
CUSTO_GRANDE=10
NORMAL="normal"
SEDEX="sedex"
SEDEX10="sedex10"
CUSTO_NORMAL= 0
CUSTO_SEDEX= 5
CUSTO_SEDEX10= 8

def validaTipoItem (tipo):
    tipo = str.lower(tipo)
    
    if tipo == PACOTE or tipo == DOCUMENTO:
        return True
    else:
        return False

def validaPeso (peso):

    if peso >= 0:
        return True
    else:
        return False

def convertePeso (peso):
    gramas= peso * 1000
    return gramas

def calculoCustoItem (tipo,peso):
    tipo=str.lower(tipo)
    kilos= peso / 1000
    
    if tipo == PACOTE:
        preco= kilos * 3
    elif tipo == DOCUMENTO:    
        preco= kilos * 2
    return preco

def validaEmbalagem (embalagem):
    embalagem=str.lower(embalagem)
    if embalagem == PEQUENA or embalagem == MEDIA or embalagem == GRANDE:
        return True
    else :
        return False

def calculoCustoEmbalagem (tipoembalagem):
    tipoembalagem=str.lower(tipoembalagem)
    if tipoembalagem == PEQUENA:
        return CUSTO_PEQUENA

    elif tipoembalagem == MEDIA:
        return CUSTO_MEDIA

    elif tipoembalagem == GRANDE:
        return CUSTO_GRANDE
    else:
        return ("Embalagem Inválida")

def validaEntrega (tipoentrega):
    tipoentrega=str.lower(tipoentrega)
    if tipoentrega == NORMAL or tipoentrega == SEDEX or tipodeentrega == SEDEX10:
        return True
    else:
        return False

def calculoCustoEntrega (tipoentrega):
    tipoentrega=str.lower(tipoentrega)
    if tipoentrega == NORMAL:
        return CUSTO_NORMAL

    elif tipoentrega == SEDEX:
        return CUSTO_SEDEX

    elif tipoentrega == SEDEX10:
        return CUSTO_SEDEX10
