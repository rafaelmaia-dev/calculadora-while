"""Calculadora com while"""

while True:
    try:
        primeiro_numero = float(input('Digite o primeiro número: '))
        segundo_numero = float(input('Digite o segundo número: '))
        operador = input('Digite o operador (+, -, *, /): ').strip()  # .strip() remove espaços extras

        if operador == '+':
            resultado = primeiro_numero + segundo_numero
            print(f'{primeiro_numero} + {segundo_numero} = {resultado}.' )
    
        elif operador == '-':
            resultado = primeiro_numero - segundo_numero
            print(f'{primeiro_numero} - {segundo_numero} = {resultado}. ')
    
        elif operador == '/':
            if segundo_numero == 0:
                print('Divisão com o segundo número sendo zero não é permitido. ')
            else:
                resultado = primeiro_numero / segundo_numero
                print(f'{primeiro_numero} / {segundo_numero} = {resultado}. ')

        elif operador == '*':
            resultado = primeiro_numero * segundo_numero
            print(f'{primeiro_numero} * {segundo_numero} = {resultado}. ')

        else:
            print('Operador inválido! Use +, -, / ou *.')

    except ValueError:
        print('Valor digitado inválido! ')
        continue # Volta ao início do loop sem perguntar para sair

    sair = input('Você deseja sair? [s]im: ').lower().startswith('s')
    if sair:  
        print('Saindo da calculadora. ')
        break
