def classificar_nota(nota):
    """
    Classifica a nota de acordo com a escala de letras.

    :param nota: Nota do aluno, um valor entre 0 e 100.
    :return: A classificação correspondente à nota ("A" a "F").
    """
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"

def solicitar_nota():
    """
    Solicita ao usuário uma nota válida entre 0 e 100.

    :return: Nota fornecida pelo usuário.
    """
    while True:
        try:
            # Solicitar a nota do usuário
            nota = float(input("Digite a nota (0 a 100): "))

            # Verificar se a nota está dentro do intervalo válido
            if 0 <= nota <= 100:
                return nota  # Retorna a nota válida
            else:
                print("A nota deve estar entre 0 e 100. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, insira um valor numérico válido.")

def main():
    """
    Função principal para solicitar a nota e exibir a classificação correspondente.
    """
    # Solicitar a nota do usuário
    nota = solicitar_nota()

    # Obter a classificação da nota
    classificacao = classificar_nota(nota)

    # Exibir a classificação
    print(f"A classificação correspondente à nota {nota} é: {classificacao}")

# Executar a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
