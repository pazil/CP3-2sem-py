def encontrar_maximo(numeros):
    if len(numeros) == 0:
        return None
    return max(numeros)

# Pedir ao usuário uma lista de números
numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [float(num) for num in numeros]

maximo = encontrar_maximo(numeros)
print("O maior número é:", maximo)
