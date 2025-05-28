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
def solicitar_horario():
    while True:
        horario = input("Digite o horário no formato HH:MM (24h): ")
        try:
            horario_valido = datetime.strptime(horario, "%H:%M")
            print("Horário válido:", horario_valido.strftime("%H:%M"))
            return horario_valido.strftime("%H:%M")
        except ValueError:
            print("Horário inválido. Tente novamente.")
            
#Criar registros
def criar():
    base = carregar()
    proximo_id = max((r['id'] for r in base), default = 0) + 1
    evento = input('Digite o nome do evento: ').strip(' ')
    data = solicitar_data()
    print("Digite o horário de início do evento:")
    horario_inicio = solicitar_horario()
    print("Digite o horário de término:")
    horario_fim = solicitar_horario()
    local = input("Qual o local do evento? ")
    registro = {'id': proximo_id, 'evento': evento,'data': data,'hora_inicio':horario_inicio,'hora_fim':horario_fim,'local':local}
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
    base = carregar()
    try:
        id_escolhido = int(input("Digite o ID do evento que deseja atualizar: "))
        for evento in base:
            if evento['id'] == id_escolhido:
                print(f"\nEvento atual: {evento['evento']} | Data atual: {evento['data']}")
                
                novo_nome = input("Novo nome do evento (Digite (n) para manter o nome): ").strip()
                if novo_nome != "n" or novo_nome != "N":
                    evento['evento'] = novo_nome
                
                mudar_data = input("Deseja alterar a data? (s/n): ").strip()
                if mudar_data == 's' or mudar_data == "S":
                    nova_data = solicitar_data()
                    evento['data'] = nova_data
                
                print(f"\nNome do evento atualizado: {evento['evento']} | Data atualizada: {evento['data']} \n")
                salvar(base)
                return
        
        print("Evento com este ID não foi encontrado.")
    except ValueError:
        print("ID inválido. Tente novamente.")

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