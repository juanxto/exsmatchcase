n = float(input('Digite um numero: '))
print('Operações disponíveis: ')
print('1 - Dobro')
print('2 - Metade')
print('3 - 10% do número')
opc = int(input('Digite a opção desejada: '))

match opc:
    case 1:
        print(f'O dobro do número digitado é {n*2}')
    case 2:
        print(f'A metade do número é {n/2}')
    case 3:
        print(f'10% do número é {(n * 10)/100}')
    case _:
        print('Opção invalida')