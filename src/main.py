"""Calculadora com while"""

while True:
    try:
        primeiro_numero = input('Digite o primeiro número: ')
        segundo_numero = input('Digite o segundo número: ')
        operador = input('Digite o operador (+, -, *, /): ').strip()  # .strip() remove espaços extras

        num_1_float = float(primeiro_numero)
        num_2_float = float(segundo_numero)

        if operador == '+':
            resultado = num_1_float + num_2_float
            print(f'{num_1_float} + {num_2_float} = {resultado}.')
    
        elif operador == '-':
            resultado = num_1_float - num_2_float
            print(f'{num_1_float} - {num_2_float} = {resultado}.')
    
        elif operador == '/':
            if num_2_float == 0:
                print('Divisão com o segundo número sendo zero não é permitido.')
            else:
                resultado = num_1_float / num_2_float
                print(f'{num_1_float} / {num_2_float} = {resultado}.')

        elif operador == '*':
            resultado = num_1_float * num_2_float
            print(f'{num_1_float} * {num_2_float} = {resultado}.')

        else:
            print('Operador inválido! Use +, -, / ou *.')

    except ValueError:
        print('Valor digitado inválido!')
        continue # Volta ao início do loop sem perguntar para sair

    sair = input('Você deseja sair? [s]im: ').lower().startswith('s')
    if sair:  
        print('Saindo da calculadora.')
        break
