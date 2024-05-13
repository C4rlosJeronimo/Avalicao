def listarotina(L, j):
    if j == 1:
        return L
    else:
        max_index = L.index(max(L[:j]))
        L[max_index], L[j - 1] = L[j - 1], L[max_index]
        return listarotina(L, j - 1)


ListaExemplo = [3, 7, 4, 2, 6]
resultado = listarotina(ListaExemplo, len(ListaExemplo))
print("Lista final: ", resultado)
