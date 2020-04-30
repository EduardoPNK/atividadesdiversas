#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0
def mostrar_matriz():
    print('-'*30)
    for linha in matriz:
        for coluna in linha:
            print('[ {} ]'.format(coluna), end='')
        print()
    print('-'*30)
for i, valor in enumerate(matriz):
    for j , valor in enumerate(matriz[i]):
        matriz[i][j] = int(input(f'Informe algum valor para linha {i} e coluna {j}: '))
        if (matriz[i][j] % 2 ==0):
            soma_pares += matriz[i][j]
        if (j == 2):
            soma_terceira_coluna += matriz[i][j]
        if (i == 1):
            if (maior_valor_segunda_linha < matriz[i][j]):
                maior_valor_segunda_linha = matriz[i][j]
        if i == 2 and j == 2 != None:
            mostrar_matriz()
            print(f'a soma dos pares é {soma_pares}')
            print(f'a soma da terceira coluna é {soma_terceira_coluna}')
            print(f'o maior valor na  segunda linha é {maior_valor_segunda_linha}')
        else:
            mostrar_matriz()
