def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

# Pedir ao usuário uma lista de números
numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [float(num) for num in numeros]

# Calculando a média
media = calcular_media(numeros)
print("A média dos números é:", media)
