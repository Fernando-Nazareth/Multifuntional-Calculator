def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).
    """
    try:
        imc = peso / (altura ** 2)
        return f"Seu IMC é: {imc:.2f}"
    except ZeroDivisionError:
        return "Altura não pode ser zero."
    except Exception as e:
        return f"Ocorreu um erro: {e}"


def calcular_media(numeros):
    """
    Calcula a média de uma lista de números.
    """
    try:
        media = sum(numeros) / len(numeros)
        return f"A média é: {media:.2f}"
    except ZeroDivisionError:
        return "A lista de números não pode estar vazia."
    except Exception as e:
        return f"Ocorreu um erro: {e}"


def conversao_basica(a, operador, b):
    """
    Realiza operações matemáticas básicas: soma, subtração, multiplicação, divisão.
    """
    try:
        if operador == '+':
            return a + b
        elif operador == '-':
            return a - b
        elif operador == '*':
            return a * b
        elif operador == '/':
            return a / b
        else:
            return "Operador inválido."
    except ZeroDivisionError:
        return "Erro: divisão por zero."
    except Exception as e:
        return f"Ocorreu um erro: {e}"


def converter_temperatura(valor, de, para):
    """
    Converte temperaturas entre Celsius, Fahrenheit e Kelvin.
    """
    try:
        if de == 'C':
            if para == 'F':
                return (valor * 9/5) + 32
            elif para == 'K':
                return valor + 273.15
        elif de == 'F':
            if para == 'C':
                return (valor - 32) * 5/9
            elif para == 'K':
                return (valor - 32) * 5/9 + 273.15
        elif de == 'K':
            if para == 'C':
                return valor - 273.15
            elif para == 'F':
                return (valor - 273.15) * 9/5 + 32
        return "Unidade inválida."
    except Exception as e:
        return f"Ocorreu um erro: {e}"


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

    elif escolha == '0':
        print("Saindo...")

    else:
        print("Escolha inválida.")


if __name__ == "__main__":
    while True:
        menu()

