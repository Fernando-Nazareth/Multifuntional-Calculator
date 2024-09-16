from imc import calcular_imc
from media import calcular_media
from calculadora import conversao_basica
from conversoes import converter_temperatura, converter_distancia, converter_peso

def menu():
    print("Bem-vindo à Calculadora Multifuncional!")
    print("1. Calculadora Normal")
    print("2. Calcular IMC")
    print("3. Calcular Média")
    print("4. Conversões")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        try:
            a = float(input("Digite o primeiro número: "))
            operador = input("Escolha a operação (+, -, *, /): ")
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {conversao_basica(a, operador, b)}")
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")

    elif escolha == '2':
        peso = float(input("Digite o peso (kg): "))
        altura = float(input("Digite a altura (m): "))
        print(calcular_imc(peso, altura))

    elif escolha == '3':
        n = int(input("Quantos números você quer calcular a média? "))
        numeros = [float(input(f"Digite o número {i+1}: ")) for i in range(n)]
        print(calcular_media(numeros))

    elif escolha == '4':
        print("1. Converter Temperatura")
        print("2. Converter Distância")
        print("3. Converter Peso")
        sub_escolha = input("Escolha uma conversão: ")

        if sub_escolha == '1':
            valor = float(input("Digite o valor da temperatura: "))
            de = input("De qual unidade (C/F/K): ").upper()
            para = input("Para qual unidade (C/F/K): ").upper()
            print(f"Resultado: {converter_temperatura(valor, de, para):.2f}")

        elif sub_escolha == '2':
            valor = float(input("Digite o valor da distância: "))
            de = input("De qual unidade (M/KM/MI): ").upper()
            para = input("Para qual unidade (M/KM/MI): ").upper()
            print(f"Resultado: {converter_distancia(valor, de, para):.2f}")

        elif sub_escolha == '3':
            valor = float(input("Digite o valor do peso: "))
            de = input("De qual unidade (G/KG/LB): ").upper()
            para = input("Para qual unidade (G/KG/LB): ").upper()
            print(f"Resultado: {converter_peso(valor, de, para):.2f}")

    elif escolha == '0':
        print("Saindo...")

    else:
        print("Escolha inválida.")


if __name__ == "__main__":
    while True:
        menu()
