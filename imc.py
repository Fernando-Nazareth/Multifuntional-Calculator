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
