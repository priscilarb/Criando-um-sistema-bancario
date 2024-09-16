menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=> '''

saldo= 0
limite= 2000
extrato= ""
numero_saques= 0
LIMITE_SAQUES= 3

while True:

    opcao= input(menu)

    if opcao == 'd':
        valor = float(input('Digite o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('Valor inválido!')

    elif opcao == 's':
        valor = float(input('Digite o valor do saque: '))

        excede_saldo = valor > saldo
        excede_limite = valor > limite
        excede_saques = numero_saques >= LIMITE_SAQUES

        if excede_saldo:
            print('Saldo insuficiente.')

        elif excede_limite:
            print('Excede limite diário.')

        elif excede_saques:
            print('Número máximo de saques excedido.')

        elif valor > 0:
            saldo -= valor
            print('Operação realizada com sucesso.')
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Valor inválido.')

    elif opcao == 'e':
        print('\n==========EXTRATO==========')
        print('Não foram realizadas movimentações!' if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}')
        print('===========================')

    elif opcao == 'x':
        break

    else:
        print('Operação inválida, por favor selecione a opção desejada.')




