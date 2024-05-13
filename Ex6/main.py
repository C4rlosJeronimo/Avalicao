def caracter(letra):
    if letra == 'a' or letra == 'b' or letra == 'c':
        return True
    if len(letra) > 1 and (letra.endswith('a') or letra.endswith('b')
                           or letra.startswith('c') or letra.startswith('b') or
                           (letra.endswith('c') and letra[-2] != ')') or
                           (letra.startswith('a') and letra[1] != '(')):
        return False
    return caracter(letra[2:-2])


alternativas = ['a(b)c', 'a(a(b)c)c', 'a(abc)c', 'a(a(a(a)c)c)c', 'a(aacc)c']

for letra in alternativas:
    if caracter(letra):
        print(f"{letra} pertence ao conjunto W\n")
    else:
        print(f"{letra} não pertence ao conjunto W\n")
