# CALCULADORA SIMPLES EM PYTHON #
continua = True

while continua == True:

    print("\n******************* Python Calculator *******************")

    print('''
    Selecione o número da opção desejada:

    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão

    ''')

    opcao = input('Digite sua opção (1/2/3/4): ')
    int_opcao = int(opcao)

    if int_opcao == 1:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        soma = n1 + n2
        print(n1, ' + ', n2, ' = ', soma)
        
    elif int_opcao == 2:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        subtracao = n1 - n2
        print(n1, ' - ', n2, ' = ', subtracao)

    elif int_opcao == 3:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        multiplicacao = n1 * n2
        print(n1, ' * ', n2, ' = ', multiplicacao)

    elif int_opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        divisao = n1 / n2
        print(n1, ' / ', n2, ' = ', divisao)

    else:
        print('Digite somente as opções de 1, 2, 3 ou 4!')
        continua = True
        
    segue = input('Deseja realizar mais algum cálculo? Digite S para continuar ou qualquer coisa para sair. ')
    if segue == 'S' or segue == 's':
        continua = True
    else:
        continua = False





