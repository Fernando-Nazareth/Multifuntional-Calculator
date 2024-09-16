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
