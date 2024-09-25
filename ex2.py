print('Qual o seu estado civil: ')
print('S - Solteiro')
print('C - Casado')
print('V - Viúvo')
print('D - Divorciado')
estadoc = input('Digite uma opção: ').lower()

match estadoc:
    case 's':
        print('Seu estado civil é solteiro')
    case 'c':
        print('Seu estado civil é casado')
    case 'v':
        print('Seu estado civil é viúvo')
    case 'd':
        print('Seu estado civil é divorciado')
    case _:
        print('Opção inválida')