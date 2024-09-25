letra = input('Digite uma letra: ').lower()

match letra:
    case 'a'|'e'|'i'|'o'|'u':
        print('Vogal')
        n = int(input('Digite um numero: '))
        if n > 0:
            print('Maior que zero')
        else:
            print('Menor ou igual a zero')
    case _:
        print('Consoante')
