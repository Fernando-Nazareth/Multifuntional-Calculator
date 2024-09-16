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
