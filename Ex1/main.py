#Exa
def algoritmoS(numero):
    if numero < 2:
        return 10
    else:
        return algoritmoS(numero - 1) + 10


print(algoritmoS(2))


#Exb
def algoritmoA(numero):
    if numero < 2:
        return 2
    else:
        return algoritmoA(numero - 1)**-1


print(algoritmoA(6))


#Exc
def algoritmoB(numero):
    if numero < 2:
        return 1
    else:
        return algoritmoB(numero - 1) + numero**2


print(algoritmoB(6))


#Exd
def algoritmoP(numero):
    if numero < 2:
        return 1
    else:
        return numero**2 * algoritmoP(numero - 1) + numero - 1


print(algoritmoP(3))


#Exe
def algoritmoD(numero):
    if numero <= 1:
        return 3
    elif numero == 2:
        return 5
    else:
        return (numero - 1) * algoritmoD(numero - 1) + (
            numero - 2) * algoritmoD(numero - 2)


print(algoritmoD(4))


#Exf
def algoritmoW(numero):
    if numero == 1:
        return 2
    elif numero == 2:
        return 5
    else:
        return algoritmoW(numero - 1) * algoritmoW(numero - 2)


print(algoritmoW(5))


#Exg
def algoritmoT(numero):
    if numero == 1:
        return 1
    elif numero == 2:
        return 2
    elif numero == 3:
        return 3
    else:
        return algoritmoT(numero -
                          1) + 2 * algoritmoT(numero -
                                              2) + 3 * algoritmoT(numero - 3)


print(algoritmoT(4))
