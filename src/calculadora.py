from operacoes import operacao_aritmetica

def main():
    while True:
        try:
            n1 = float(input('Digite um número: '))
            n2 = float(input("Digite outro número: "))
            operador = input("Digite um dos operadores ao lado (+, -, *, /): ").strip()

            resultado = operacao_aritmetica(n1, n2, operador)
            print(f'{n1} {operador} {n2} = {resultado} ')

        except ValueError as e:
            print(f'Erro: {e} ')

        sair = input("Deseja sair? [s]im: ").strip().lower()
        if sair in ('s', 'sim'):
            print('Saindo da calculadora. ')
            break

main()

        