# P(numero) = {a, se numero = 1}
#             {r x P(numero - 1), se numero > 1}


def geometria(a, r, numero):
    if numero == 1:
        return a
    else:
        return r * geometria(a, r, numero - 1)


print(geometria(2, 3, 4))
