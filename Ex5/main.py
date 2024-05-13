def caracter(letra):
    if letra == 'a' or letra == 'b':
        return True
    if letra.endswith('a') and letra[-2] != 'a':
        return False
    return caracter(letra[:-1]) and letra[-1] == 'b'


alternativas = ['a', 'ab', 'aba', 'aaab', 'bbbbb']

for letra in alternativas:
    if caracter(letra):
        print(f"{letra} pertence ao conjunto S\n")
    else:
        print(f"{letra} não pertence ao conjunto S\n")
