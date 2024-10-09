def criar_matriz():
    matriz = []
    print("insira os elementos da matriz 3x3:")

    for i in range(3):
        linha = []
        for j in range(3):
            try:
                valor = float(input(f"Digite o elemento [{i+1}][{j+1}]: "))
                linha.append(valor)
            except ValueError:
                print("Erro Paizao. Tenta de novo.")
                return None
        matriz.append(linha)

    return matriz

matriz = criar_matriz()

if matriz:
    print("\nMatriz inserida:")
    for linha in matriz:
        print(linha)
else:
    print("A matriz não pôde ser criada devido a uma entrada inválida.")

