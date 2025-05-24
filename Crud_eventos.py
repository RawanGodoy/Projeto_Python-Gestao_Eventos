#BIBLIOTECAS
import json
import re

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
from datetime import datetime

from datetime import datetime

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
            
#CRIAR REGISTROS
def criar():
    base = carregar()
    proximo_id = max((r['id'] for r in base), default = 0) + 1
    evento = input('Digite o nome do evento: ').strip(' ')
    data = solicitar_data()
    registro = {'id': proximo_id, 'evento': evento,'data': data}
    base.append(registro) 
    salvar(base)
    print(f'Registro criado: {registro}')
    
def deletar():
    print("deletar")
def pesquisar():
    print("pesquisar")
def listar():
    print("Listar")
def atualizar():
    print("Atualizar")
    
    
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