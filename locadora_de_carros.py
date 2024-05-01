import os

carros = [
    ('Chevrolet Tracker', 120),
    ('Chevrolet Onix', 90),
    ('Chevrolet Spin', 150),
    ('Hyundai HB20', 85),
    ('Hyundai Tucson', 120),
    ('Fiat Uno', 60),
    ('Fiat Mobi', 70),
    ('Fiat Pulse', 130)
    ]

carros_alugados = []

def mostrar_portfolio(lista_carros):
    for i, car in enumerate(lista_carros):
        print('[{}] {} - R$ {}/dia.'.format(i, car[0], car[1]))
    print('-' * 50)

mostrar_portfolio(carros)

while True:
    os.system("cls")
    print('-' * 50)
    print('Bem vindo à locadora de carros!')
    print('-' * 50)
    print('O que deseja fazer?')
    print('0 - Mostrar portfólio | 1 - Alugar um carro | 2 - Devolver um carro')
    acao = int(input())

    os.system("cls")
    if acao == 0:
        print('Portfólio de carros disponíveis:')
        mostrar_portfolio(carros)
    elif acao == 1:
        mostrar_portfolio(carros)
        print('Escolha o código do carro:')
        cod = int(input())
        print('Deseja alugar por quantos dias?')
        dias_aluguel = int(input())
        os.system("cls")

        print('Você escolheu o carro {} por {} dias.'.format(carros[cod][0], dias_aluguel))
        print('-' * 50)
        print('O aluguel total é de R$ {}. Deseja confirmar?'.format(dias_aluguel * carros[cod][1]))
        print('0 - Sim | 1 - Não')
        conf = int(input())

        if conf == 0:
            print('Parabéns! Você alugou o {} por {} dias.'. format(carros[cod][0], dias_aluguel))
            carros_alugados.append(carros.pop(cod))

    elif acao == 2:
        if len(carros_alugados) == 0:
            print('Não há carros para devolver.')
        else:
            print('Segue lista de carros alugados. Qual você deseja devolver?')
            mostrar_portfolio(carros_alugados)
            print('')
            print('Escolha o código do carro que deseja devolver:')
            cod = int(input())
            print('Obrigado por devolver o carro {}.'.format(carros[cod][0]))
            carros.append(carros_alugados.pop(cod))

    print('')
    print('-' * 50)
    print('Deseja continuar? 0 : Continuar | 1 : Sair')
    if int(input()) == 1:
        break