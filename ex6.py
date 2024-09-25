

print('Cardápio do restaurante')
print('1 - Picanha')
print('2 - Lasanha')
print('3 - Strogonoff')
print('4 - Bife Acebolado')
print('5 - Pão com Ovo')
opc = int(input('Digite a opção do prato desejado: '))

match opc:
    case 1:
        print('O prato escolhido foi Picanha')
        preco = 25.00
        confirm = input('Você deseja pagar os 10% do garçom? ').lower()
        if confirm == 'sim' or confirm == 's' or confirm == 'yes':
            pt = preco + ((10*preco)/100)
            print(f'O valor total a ser pago é R${pt:.2f}')
        else:
            print(f'O valor total a ser pago é R${preco}')
    case 2:
        print('O prato escolhido foi Lasanha')
        preco = 20.00
        confirm = input('Você deseja pagar os 10% do garçom? ').lower()
        if confirm == 'sim' or confirm == 's' or confirm == 'yes':
            pt = preco + ((10 * preco) / 100)
            print(f'O valor total a ser pago é R${pt:.2f}')
        else:
            print(f'O valor total a ser pago é R${preco}')
    case 3:
        print('O prato escolhido foi Strogonoff')
        preco = 20.00
        confirm = input('Você deseja pagar os 10% do garçom? ').lower()
        if confirm == 'sim' or confirm == 's' or confirm == 'yes':
            pt = preco + ((10 * preco) / 100)
            print(f'O valor total a ser pago é R${pt:.2f}')
        else:
            print(f'O valor total a ser pago é R${preco}')
    case 4:
        print('O prato escolhido foi Bife Acebolado')
        preco = 15.00
        confirm = input('Você deseja pagar os 10% do garçom? ').lower()
        if confirm == 'sim' or confirm == 's' or confirm == 'yes':
            pt = preco + ((10 * preco) / 100)
            print(f'O valor total a ser pago é R${pt:.2f}')
        else:
            print(f'O valor total a ser pago é R${preco}')
    case 5:
        print('O prato escolhido foi Pão com Ovo')
        preco = 5.00
        confirm = input('Você deseja pagar os 10% do garçom? ').lower()
        if confirm == 'sim' or confirm == 's' or confirm == 'yes':
            pt = preco + ((10 * preco) / 100)
            print(f'O valor total a ser pago é R${pt:.2f}')
        else:
            print(f'O valor total a ser pago é R${preco}')
    case _:
        print('Opção inválida')


