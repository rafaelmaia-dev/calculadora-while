def criar_soma(n1):
    def soma2(n2):
        return n1 + n2
    return soma2

numero1 = criar_soma(int(input('Digite o primeiro número: ')))
resultado = numero1(int(input('Digite o segundo número: ')))
print(resultado)





        

