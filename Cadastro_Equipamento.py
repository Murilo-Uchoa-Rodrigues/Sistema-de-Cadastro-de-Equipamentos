#Esse programa é um Sistema de Cadastro de Equipamentos.
#O Sistema de Equipamento baseia-se em cadastrar equipamentos, listar equipamentos e cadastrar valor total 
equipamentos = []

def cadastrar_equipamentos():
    nome_equipamento = input('Qual o nome do equipamento? ').upper()
    while len(nome_equipamento) == 0:
        print('Erro: o nome do eqipamento não pode estar vazio. ')
        nome_equipamento = input('Qual o nome do equipamento?')
    print('\n' 
    ''
    'Categorias:\n' 
    'CLP\n' 
    'Inversor\n' 
    'Motor\n' 
    'Sensor\n ')
    categoria = input('Categoria: ').upper()
    while categoria not in ('CLP', 'iNVERSOR', 'MOTOR', 'SENSOR'):
        print('Erro: categoria inválida. ')
        categoria = input('Categoria: ').upper()
    preco = float(input('Informe o valor do produto: R$ '))
    while preco <= 0:
        print('Erro: o preço deve ser maior que zero.')
        preco = float(input('Informe o valor do produto: R$ '))

    equipamento_cadastrado = nome_equipamento, categoria, preco
    equipamentos.append(equipamento_cadastrado)
    print('Equipamento cadastrado com sucesso! \n' \
    '')



#Área de testes, sistema de cadastro de equipamentos
print('SISTEMA DE EQUIPAMENTOS')
opcao = int(input('Escolha uma opção: \n 1. Cadastrar equipamento\n 2. Listar equipamentos\n 3. Calcular valor total\n 4. Sair\n '))
if opcao == 1:
    cadastrar_equipamentos()
else:
    print('Certo')

#Área de testes, sistema mostra equipamentos cadastrados
print('SISTEMA DE EQUIPAMENTOS')
opcao = int(input('Escolha uma opção: \n 1. Cadastrar equipamento\n 2. Listar equipamentos\n 3. Calcular valor total\n 4. Sair\n '))












