#BIBLIOTECAS
import json
from datetime import datetime

#arquivo Json
arquivo = "dados/eventos.json"
#SALVAR A BASE (INPUT)
def salvar(base):
    with open(arquivo,'w',encoding = 'utf-8') as f:
        json.dump(base, f, indent = 4, ensure_ascii = False)
        
#CARREGAR A BASE (OUTPUT)
def carregar():
    try:
        with open(arquivo,"r") as f:
            registros = json.load(f)
            return registros
    except FileNotFoundError:
        return []
    
#Solicitação de data no formato correto
def solicitar_data():
    while True:
        data = input("Digite a data no formato dd/mm/aa: ")
        try:
            # Tenta converter para datetime
            data_valida = datetime.strptime(data, "%d/%m/%y")
            print("Data válida:", data_valida.strftime("%d/%m/%y"))
            return data_valida.strftime("%d/%m/%y")
        except ValueError:
            print("Data inválida. Tente novamente.")
            
#Criar registros
def criar():
    base = carregar()
    proximo_id = max((r['id'] for r in base), default = 0) + 1
    evento = input('Digite o nome do evento: ').strip(' ')
    data = solicitar_data()
    registro = {'id': proximo_id, 'evento': evento,'data': data}
    base.append(registro) 
    salvar(base)
    print(f'Registro criado: {registro}')
#Listar
def listar():
    base = carregar()
    
    if not base:
        print('Nenhum evento encontrado.')
        return

    print('\n Eventos Cadastrados ')
    for evento in base:
        id = evento["id"]
        nome = evento["evento"]
        data = evento["data"]
        print(f'ID: {id} | Nome: {nome} | Data: {data}')
#Atualizar
def atualizar():
    print("Atualizar")
#Delete
def deletar():
    base = carregar()
    try:
        id_delete = int(input("Digite o ID do evento a ser deletado: "))
        base_nova = [r for r in base if r['id'] != id_delete]
        if len(base_nova) == len(base):
            print("ID não encontrado.")
        else:
            salvar(base_nova)
            print("Registro deletado com sucesso.")
    except ValueError:
        print("ID inválido. Tente novamente.")
#Pesquisa
def pesquisar():
    print("pesquisar")
    
#Menu
def menu():
    actions = {
        '1': criar,
        '2': listar,
        '3': atualizar,
        '4': deletar,
        '5': pesquisar,
        '6': exit
    }
    while True:
        print('''
\n==== MENU CRUD JSON ====
        1. Criar
        2. Listar
        3. Atualizar
        4. Deletar
        5. Pesquisa específica
        6. Sair''')
        escolha = input('Escolha uma opção: ')
        opcao = actions.get(escolha)
        if opcao:
            opcao()
        else:
            print('Opção inválida, tente novamente.')
#INICIAR MENU
menu()