import numpy as np

def criar_matriz():
    matriz = []
    print("Insira os elementos da matriz 2x2:")

    for i in range(2):
        linha = []
        for j in range(2):
            try:
                valor = float(input(f"Digite o elemento [{i+1}][{j+1}]: "))
                linha.append(valor)
            except ValueError:
                print("Erro Paizão. Tenta de novo.")
                return None
        matriz.append(linha)

    return np.array(matriz)

matriz = criar_matriz()

if matriz is not None:
    print("\nMatriz inserida:")
    print(matriz)
else:
    print("A matriz não pôde ser criada devido a uma entrada inválida.")
