def converter_temperatura(celsius, tipo):
    """
    Converte a temperatura de Celsius para Fahrenheit ou Kelvin.
    
    :param celsius: Temperatura em graus Celsius
    :param tipo: Tipo de conversão, "F" para Fahrenheit (padrão) ou "K" para Kelvin
    :return: Temperatura convertida na unidade especificada
    """
    if tipo.upper() == "F":
        # Converter para Fahrenheit
        return (celsius * 9/5) + 32
    elif tipo.upper() == "K":
        # Converter para Kelvin
        return celsius + 273.15
    else:
        # Tipo não reconhecido, retornar Fahrenheit por padrão
        print("Tipo não reconhecido. Convertendo para Fahrenheit por padrão.")
        return (celsius * 9/5) + 32

def solicitar_temperatura():
    """
    Solicita ao usuário a temperatura em Celsius.
    
    :return: Temperatura fornecida pelo usuário.
    """
    while True:
        try:
            # Solicitar a temperatura ao usuário
            temp_celsius = float(input("Digite a temperatura em Celsius: "))
            return temp_celsius  # Retorna a temperatura válida
        except ValueError:
            print("Erro: Por favor, insira um valor numérico válido para a temperatura.")

def solicitar_tipo_conversao():
    """
    Solicita ao usuário o tipo de conversão de temperatura desejado.
    
    :return: Tipo de conversão, "F" para Fahrenheit ou "K" para Kelvin.
    """
    while True:
        try:
            # Solicitar o tipo de conversão ao usuário
            tipo_conversao = input("Digite o tipo de conversão ('F' para Fahrenheit ou 'K' para Kelvin): ")

            # Verificar se o tipo de conversão é válido
            if tipo_conversao.upper() not in ["F", "K"]:
                raise ValueError("Tipo de conversão inválido.")
            return tipo_conversao.upper()  # Retorna o tipo de conversão válido
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira 'F' ou 'K'.")

def main():
    """
    Função principal para realizar a conversão de temperatura.
    """
    # Solicitar a temperatura e o tipo de conversão
    temp_celsius = solicitar_temperatura()
    tipo_conversao = solicitar_tipo_conversao()

    # Realizar a conversão e exibir o resultado
    resultado = converter_temperatura(temp_celsius, tipo_conversao)
    print(f"A temperatura convertida é: {resultado}")

# Executar a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
