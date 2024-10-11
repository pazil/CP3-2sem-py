def encontrar_maior_numero(num1, num2, num3):
    """
    Retorna o maior número entre os três fornecidos.

    :param num1: Primeiro número.
    :param num2: Segundo número.
    :param num3: Terceiro número.
    :return: O maior número entre os três.
    """
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

def solicitar_numeros():
    """
    Solicita três números ao usuário e exibe o maior número.

    Continua solicitando até que os três números sejam válidos.
    """
    while True:
        try:
            # Solicitar três números ao usuário
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            num3 = float(input("Digite o terceiro número: "))

            # Encontrar o maior número
            maior = encontrar_maior_numero(num1, num2, num3)

            # Exibir o maior número
            print(f"O maior número é: {maior}")
            break  # Sair do loop se a entrada for válida

        except ValueError:
            print("Erro: Por favor, insira apenas números válidos.")

# Executar a função solicitar_numeros se o script for executado diretamente
if __name__ == "__main__":
    solicitar_numeros()
