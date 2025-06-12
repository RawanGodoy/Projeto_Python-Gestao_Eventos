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
        horario_inicio = evento["hora_inicio"]
        horario_fim = evento["hora_fim"]
        local = evento["local"]
        print(f'ID: {id} | Nome: {nome} | Data: {data} | Horário de início : {horario_inicio} | Horário de fim : {horario_fim} | Local : {local}')
#Atualizar
def atualizar():
    base = carregar()
    try:
        id_escolhido = int(input("Digite o ID do evento que deseja atualizar: "))
        for evento in base:
            if evento['id'] == id_escolhido:
                print(f"\nEvento atual: {evento['evento']} | Data atual: {evento['data']}")
                
                novo_nome = input("Novo nome do evento (Digite (N) para manter o nome): ").strip()
                if novo_nome != "n" and novo_nome != "N":
                    evento['evento'] = novo_nome
                
                mudar_data = input("Deseja alterar a data? (S/N): ").strip()
                if mudar_data == 's' or mudar_data == "S":
                    nova_data = solicitar_data()
                    evento['data'] = nova_data

                opcao = input("Deseja alterar o horário inicial? Digite (N) para manter o horário inicial: ")
                if opcao != 'N' and opcao != 'n':
                    nova_hora = solicitar_horario()
                    evento['hora_inicio'] = nova_hora
                
                opcao2 = input("Deseja alterar o horário final? Digite (N) para manter o horário final: ")
                if opcao2 != 'N' and opcao2 != 'n':
                    nova_hora2 = solicitar_horario()
                    evento['hora_fim'] = nova_hora2

                opcao3 = input("Deseja alterar o local do evento? Digite (N) para manter o local: ")
                if opcao3 != 'N' and opcao3 != 'n':
                    novo_local = input("Qual o local do evento? ")
                    evento['local'] = novo_local

                
                print(f"\n    Nome do evento atualizado: {evento['evento']} | Data atualizada: {evento['data']}\n| Horário inicial atualizado: {evento['hora_inicio']} | Horário final atualizado: {evento['hora_fim']} | Local atualizado: {evento['local']} \n")
                salvar(base)
                return
        
        print("Evento com este ID não foi encontrado.")
    except ValueError:
        print("ID inválido. Tente novamente.")
#Delete
def deletar():
    base = carregar()
    
    if not base:
        print("Não há registros para deletar. Volte para o inicio.")
        return

    listar()
    
    ids_input = input("Digite os IDs dos eventos a serem deletados (caso queira deletar mais de um ID separare por vírgula): ")
    
    try:
        ids_a_deletar = set(int(i.strip()) for i in ids_input.split(",") if i.strip().isdigit())

        if not ids_a_deletar:
            print("Nenhum ID válido fornecido.")
            return

        base_nova = [r for r in base if r['id'] not in ids_a_deletar]
        deletados = len(base) - len(base_nova)

        if deletados == 0:
            print("Nenhum dos IDs fornecidos foi encontrado.")
        else:
            salvar(base_nova)
            print(f"{deletados} registros deletados com sucesso.")
            
    except ValueError:
        print("Erro: certifique-se de digitar apenas números inteiros separados por vírgula.")

#Pesquisa
def pesquisar():
    base = carregar()
    
    if not base:
        print("Não há registros para pesquisar.")
        return

    try:
        id_busca = int(input("Digite o ID do evento que deseja buscar: "))
        for r in base:
            if r['id'] == id_busca:
                print("\n=== Evento Encontrado ===")
                print(f"ID: {r['id']} | Evento: {r['evento']} | Data: {r['data']} | Início: {r['hora_inicio']} | Término: {r['hora_fim']} | Local: {r['local']}")
                return
        print("ID não encontrado.")
    except ValueError:
        print("ID inválido. Digite um número inteiro.")
    
# #Menu
# def menu():
#     actions = {
#         '1': criar,
#         '2': listar,
#         '3': atualizar,
#         '4': deletar,
#         '5': pesquisar,
#         '6': exit
#     }
#     while True:
#         print('''
# \n==== MENU CRUD JSON ====
#         1. Criar
#         2. Listar
#         3. Atualizar
#         4. Deletar
#         5. Pesquisa específica
#         6. Sair''')
#         escolha = input('Escolha uma opção: ')
#         opcao = actions.get(escolha)
#         if opcao:
#             opcao()
#         else:
#             print('Opção inválida, tente novamente.')
#INICIAR MENU   
if __name__ == "__main__":
    # menu()
    pesquisar()
    deletar()
    criar()
    atualizar()
    listar()