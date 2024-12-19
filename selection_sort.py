def ordenar_arquivo(entrada, saida):
    with open(entrada, 'r') as entrada:
        numeros = list(map(int, entrada.read().split()))

    n = len(numeros)
    for i in range(n-1):
        menor_ind = i
        for j in range(i+1, n):
            if numeros[j] < numeros[menor_ind]:
                menor_ind = j
        (numeros[i], numeros[menor_ind]) = (numeros[menor_ind], numeros[i])

    with open(saida, 'w') as saida:
        saida.write('\n'.join(map(str, numeros)))

ordenar_arquivo('num.100000.4.in', 'selectionsort.100000.4.in')