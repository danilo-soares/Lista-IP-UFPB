def calculaComissao (quantidade):
    comissao= (quantidade * 80) * (0.07)
    return comissao

def calculaBonus (quantidade):
    if quantidade > 50:
        valortotal=70
    else:
        valortotal=0
    return valortotal
    
    

    
