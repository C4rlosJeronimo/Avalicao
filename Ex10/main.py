#9 leituras

def populacao(numero):
    if numero == 1:
        return 50000
    else:
        return populacao(numero - 1) * 3

print(populacao(9))