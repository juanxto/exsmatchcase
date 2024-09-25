print('Palestras disponíveis: ')
print('1 - Linux')
print('2 - Banco de Dados')
print('3 - Windows Server')
print('4 - Lógica e Programação')
n = int(input('Digite o numero da palestra que você vai: '))

match n:
    case 1:
        print('Você deve ir para o Auditório 1')
    case 2:
        print('Você deve ir para o Auditório 2')
    case 3:
        print('Você deve ir para o Auditório 3')
    case 4:
        print('Você deve ir para o Auditório Principal')
    case _:
        print('Opção invalida.')