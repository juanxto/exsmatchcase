print('Opção 1 - Soma')
print('Opção 2 - Subtração')
print('Opção 3 - Multiplicação')
print('Opção 4 - Divisão')

opc = int(input('Digite uma opção: '))
a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))

match opc:
    case 1:
        n = a + b
        print(f'O resultado da soma entre esses números é {n}')
    case 2:
        n = a - b
        print(f'O resultado da suubtração entre esses números é {n}')
    case 3:
        n = a * b
        print(f'O resultado da multiplicação entre esses números é {n}')
    case 4:
        n = a / b
        print(f'O resultado da divisão entre esses numeros é {n}')
    case _:
        print('Opção invalida')