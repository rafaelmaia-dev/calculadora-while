def operacao_aritmetica(n1: float, n2: float, operador: str) -> float:

    """
    Realiza operação aritmética entre dois números.
    
    Args:
        n1: Primeiro operando
        n2: Segundo operando
        operador: Um de '+', '-', '*', '/'
    
    Returns:
        Resultado da operação como float
    
    Raises:
        ValueError: Para operador inválido ou divisão por zero

    """
   
    if operador == '+':
        return n1 + n2
    elif operador == '-':
        return n1 - n2
    elif operador == '*':
        return n1 * n2
    elif operador == '/':
        if n2 == 0:
            raise ValueError('Divisão por zero não é permitida. ')
        return n1 / n2
    else:
        raise ValueError(f'Operador inválido: "{operador}". Use +, -, *, ou /. ')
    
