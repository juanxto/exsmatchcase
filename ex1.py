

preco = float(input('Digite o valor do produto a ser comprado: R$'))
print('Você é um cliente comum, funcionario ou vip? ')
print('Opção 1 - Cliente comum')
print('Opção 2 - Cliente vip')
print('Opção 3 - Funcionario')
opc = int(input('Digite uma opção: '))

match opc:
    case 1:
        print('Você é um cliente comum')
        print(f'O valor do produto a ser pago é R${preco:.2f}')
    case 2:
        print('Você é um cliente vip, tem 5% de desconto')
        pt = preco - ((5 * preco) / 100)
        print(f'O valor do produto a ser pago é R${pt:.2f}')
    case 3:
        print('Você é um funcionario, tem 10% de desconto')
        pt = preco - ((10 * preco) / 100)
        print(f'O valor do produto a ser pago é R${pt:.2f}')
    case _:
        print('ERRO: Opção invalida')