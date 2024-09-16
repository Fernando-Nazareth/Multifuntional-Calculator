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
