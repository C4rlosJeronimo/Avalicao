#a)
def funcaoa(numero):
    if numero == 1:
        return 1
    else:
        return funcaoa(numero - 1) * 3


print(funcaoa(4))

# P(numero) = {1, se numero = 1}
#             {P(numero - 1) * 3, se numero > 1}


#b)
def funcaob(numero):
    if numero == 1:
        return 2
    else:
        return funcaob(numero - 1) / 2


print(funcaob(4))

# P(numero) = {2, se numero = 1}
#             {P(numero - 1) / 2, se numero > 2}


#c)
def funcaoc(numero, a, b):
    if numero == 1:
        return a
    elif numero == 2:
        return b
    else:
        return funcaoc(numero - 1, a, b) + funcaoc(numero - 2, a, b)


a = 1
b = 2
print(funcaoc(3))

# P(numero) = {a, se numero = 1}
#             {2, }
#
