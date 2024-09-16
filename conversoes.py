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


def converter_distancia(valor, de, para):
    """
    Converte distância entre metros, quilômetros e milhas.
    """
    try:
        if de == 'M':
            if para == 'KM':
                return valor / 1000
            elif para == 'MI':
                return valor * 0.000621371
        elif de == 'KM':
            if para == 'M':
                return valor * 1000
            elif para == 'MI':
                return valor * 0.621371
        elif de == 'MI':
            if para == 'M':
                return valor / 0.000621371
            elif para == 'KM':
                return valor / 0.621371
        return "Unidade inválida."
    except Exception as e:
        return f"Ocorreu um erro: {e}"


def converter_peso(valor, de, para):
    """
    Converte peso entre gramas, quilogramas e libras.
    """
    try:
        if de == 'G':
            if para == 'KG':
                return valor / 1000
            elif para == 'LB':
                return valor * 0.00220462
        elif de == 'KG':
            if para == 'G':
                return valor * 1000
            elif para == 'LB':
                return valor * 2.20462
        elif de == 'LB':
            if para == 'G':
                return valor / 0.00220462
            elif para == 'KG':
                return valor / 2.20462
        return "Unidade inválida."
    except Exception as e:
        return f"Ocorreu um erro: {e}"
