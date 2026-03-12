def operacao_aritmetica(n1, n2, operador):
    
    if operador == '+':
        return n1 + n2
    elif operador == '-':
        return n1 - n2
    elif operador == '*':
        return n1 * n2
    elif operador == '/':
        if n2 == 0:
            print(f'Divisão por zero não é permitida. ')
        else:
            return n1 / n2
    else:
        raise ValueError(f'Operador inválido: "{operador}". Use +, -, *, ou /. ')
    
