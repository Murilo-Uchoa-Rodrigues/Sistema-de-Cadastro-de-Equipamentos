# Este programa consiste em um Sistema de Cadastro de Equipamentos.
#
# O sistema permite cadastrar equipamentos, listar os equipamentos
# cadastrados e calcular o valor total dos equipamentos.
#
# Como base para o sistema, foram utilizados equipamentos elétricos,
# como CLP, inversor de frequência, motor e sensor.

equipamentos = []#Lista onde será armazenado os equipamentos cadastrados EX: [(Nome: nome_equipamento), (Categoria: categoria), (Preço: preco)]

def cadastrar_equipamentos():#Aqui é aonde deverá ser feito todo o cadastro dos equipamantos, informando: Nome, Categoria e Preço do equipamento
    nome_equipamento = input('Nome do equipamento? ').upper()
    while len(nome_equipamento) == 0:
        print('Erro: o nome do eqipamento não pode estar vazio. ')
        nome_equipamento = input('Nome do equipamento?')
    print('\n'
    ''
    'Categorias:\n'
    'CLP\n'
    'Inversor\n'
    'Motor\n'
    'Sensor\n ')
    categoria = input('Categoria?: ').upper()

    # Cria um laço de repetição para garantir que o usuário informe apenas valores aceitos pelo sistema.
    while categoria not in ('CLP', 'INVERSOR', 'MOTOR', 'SENSOR'):
        print('Erro: categoria inválida. ')
        categoria = input('Categoria?: ').upper()
    preco = float(input('Informe o valor do produto: R$ '))
    while preco <= 0:
        print('Valor inválido! O preço deve ser maior que zero.')
        preco = float(input('Informe o valor do produto: R$ '))

    equipamento_cadastrado = nome_equipamento, categoria, preco
    equipamentos.append(equipamento_cadastrado)
    print('Equipamento cadastrado com sucesso! \n' \
    '')
    

# Exibe os equipamentos cadastrados ou informa caso não exista nenhum equipamento.
def mostrar_equipamentos():
    if equipamentos:
        for indice, equipamentos_cadastrado in enumerate(equipamentos):
            print(indice, f'Nome: {equipamentos_cadastrado[0]}',
                          f'Categoria: {equipamentos_cadastrado[1]}',
                          f'Preço: {equipamentos_cadastrado[2]}')

    else:
        print('Nenhum equipamento cadastrado.')
    

# Calcula e exibe o valor total de todos os equipamentos cadastrados.
def calcular_total():
    total = 0
    for equipamento in equipamentos:
        total += equipamento[2]
    print(f'Valo total dos equipamentos: R$ {total}')


# Exibe o menu principal, valida a opção escolhida e executa a função correspondente.
def escolha_opcao():
    print('SISTEMA DE EQUIPAMENTOS')
    while True:
        try:
            opcao = int(input('Escolha uma opção: \n 1. Cadastrar equipamento\n 2. Listar equipamentos\n 3. Calcular valor total\n 4. Sair\n '))
            if opcao == 1 :
                    cadastrar_equipamentos()
            elif opcao == 2:
                    mostrar_equipamentos()
            elif opcao == 3:
                    calcular_total()
                    pass
            elif opcao == 4:
                    print('Programa encerrado.')
                    break
            else:
                    print('Opção inválida.\n' \
                    'Tente novamente.')
                    
        except ValueError:
             print('Entrada inválida!\n' \
            'Digite apenas números.')
             

chamar = escolha_opcao()