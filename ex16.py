def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Pedir ao usuário a temperatura em Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Convertendo para Fahrenheit
fahrenheit = celsius_para_fahrenheit(celsius)
print(f"A temperatura em Fahrenheit é: {fahrenheit}")
