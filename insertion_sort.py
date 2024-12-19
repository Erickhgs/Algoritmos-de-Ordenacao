def ordenar_arquivo(entrada, saida):
    with open(entrada, 'r') as entrada:
        numeros = list(map(int, entrada.read().split()))

    for i in range(1, len(numeros)):
        pivo = numeros[i]
        j = i - 1
        while j >= 0 and numeros[j] > pivo:
            numeros[j + 1] = numeros[j]
            j -= 1
        numeros[j + 1] = pivo

    with open(saida, 'w') as saida:
        saida.write('\n'.join(map(str, numeros)))

ordenar_arquivo('num.100000.4.in', 'inserctionsort.100000.4.in')
