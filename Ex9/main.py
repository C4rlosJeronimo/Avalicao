#P(numero) = {1, se o numero = 1}
#            {P(numero - 1) + numero, se numero > 1}

def geometria(numero):
    if numero == 1:
        return 1
    else:
        return geometria(numero - 1) + numero

print(geometria(5))
