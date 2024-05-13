def numeroT(numero):
    if numero == 2:
        return True
    elif numero < 5:
        return False
    else:
        return numeroT(numero - 3) or numeroT(numero // 2)


alternativas = [6, 7, 19, 12]

for numero in alternativas:
    if numeroT(numero):
        print(numero, "pertence ao conjunto T\n")
    else:
        print(numero, "não pertence ao cnojunto T\n")
