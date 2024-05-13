def numeroM(numero):
    if numero == 2 or numero == 3:
        return True
    elif numero < 2 or (numero % 2 != 0 and numero % 3 != 0):
        return False
    for i in range(2, numero):
        if numero % i == 0 and numeroM(i) and numeroM(numero // i):
            return True
    return False


alternativas = [6, 9, 16, 21, 26, 54, 72, 218]

for numero in alternativas:
    if numeroM(numero):
        print(numero, "pertence ao conjunto M\n")
    else:
        print(numero, "não pertence ao conjunto M\n")
