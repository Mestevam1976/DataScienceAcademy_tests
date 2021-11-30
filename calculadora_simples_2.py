# CALCULADORA SIMPLES - v2 EM PYTHON #
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

    opcao = input('Digite sua opção (1/2/3/4): \n')

    if opcao == '1':
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        soma = n1 + n2
        operador = ' + '
        resultado = soma

    elif opcao == '2':
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        subtracao = n1 - n2
        operador = ' - '
        resultado = subtracao
    
    elif opcao == '3':
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        multiplicacao = n1 * n2
        operador = ' * '
        resultado = multiplicacao
    
    elif opcao == '4':
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        divisao = n1 / n2
        operador = ' / '
        resultado = divisao

    else:
        print('Favor digitar somente 1, 2, 3 ou 4! ')
        continua = True
    
    print(n1, operador, n2, ' = ', resultado)
    calcula_novamente = input('''
Deseja fazer outro cálculo?
Digite S para continuar ou tecle qualquer coisa para sair. ''')

    if calcula_novamente == 'S'.lower():
        continua = True
    else:
        continua = False
    

