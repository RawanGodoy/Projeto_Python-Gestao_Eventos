#Crud focado nas atividades dos eventos
import json
import os

#arquivo Json das atividades
arquivo_atividades = "dados/atividades.json"
arquivo_eventos = "dados/eventos.json"

#salvar a base
def salvar(base):
    diretorio = os.path.dirname(arquivo_atividades)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    with open(arquivo_atividades,'w',encoding = 'utf-8') as f:
        json.dump(base, f, indent = 4, ensure_ascii = False)
        
#carregar base
def carregar():
    try:
        with open(arquivo_atividades,"r") as f:
            registros = json.load(f)
            return registros
    except FileNotFoundError:
        return []
    
#codigo

# cadastro
def criar():
    atividades = carregar()
    
    try:
        with open(arquivo_eventos, "r", encoding="utf-8") as f:
            eventos = json.load(f)
    except FileNotFoundError:
        print("Arquivo de eventos não encontrado em '" + arquivo_eventos + "'. Crie um evento primeiro.")
        return

    # obter e validar o ID do evento
    while True:
        try:
            id_evento_str = input("Digite o ID do evento para vincular a atividade: ")
            id_evento = int(id_evento_str)
            
            if any(evento['id'] == id_evento for evento in eventos):
                break # Evento existe, podemos prosseguir para a próxima validação
            else:
                print("Erro: Nenhum evento encontrado com este ID. Tente novamente.")
        except ValueError:
            print("ID inválido. Por favor, digite um número.")

    
    for atividade_existente in atividades:
        if atividade_existente['id_evento'] == id_evento:
            print(f"\n ERRO: O evento com ID {id_evento} já possui uma atividade vinculada.")
            print("   Um evento só pode ter uma atividade.")
            print(" Para modificar a atividade existente, por favor, volte ao menu e escolha a opção '3. Atualizar'.")
            return 
        #interrompe o cadastro imediatamente
    

    #aqui fala se passou na validação, pede os detalhes da nova atividade
    tipo_atividade = input("Digite o tipo da atividade (Ex: Palestra, Oficina): ").strip()
    descricao = input("Descreva a atividade: ").strip()

    #cria e salva a nova atividade
    proximo_id = max((a.get('id_atividade', 0) for a in atividades), default=0) + 1
    nova_atividade = {
        'id_atividade': proximo_id,
        'id_evento': id_evento,
        'tipo': tipo_atividade,
        'descricao': descricao
    }

    atividades.append(nova_atividade)
    salvar(atividades)
    
    print("\n Atividade cadastrada e vinculada ao evento com sucesso!")
    print("--- Dados da Atividade Cadastrada ---")
    print(f"ID ÚNICO DA ATIVIDADE: {nova_atividade['id_atividade']}")
    print(f"VINCULADA AO EVENTO DE ID: {nova_atividade['id_evento']}")
    print(f"Tipo: {nova_atividade['tipo']}")
    print(f"Descrição: {nova_atividade['descricao']}")
    print("-------------------------------------")


# atualizar
def atualizar():
    atividades = carregar()
    if not atividades:
        print("\nNão há atividades cadastradas para atualizar.")
        return

    try:
        id_atividade = int(input("Digite o ID da atividade que deseja atualizar: "))
    except ValueError:
        print("ID inválido. Por favor, insira um número inteiro.")
        return

    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            print(f"\nAtividade encontrada: ID {atividade['id_atividade']}, Tipo: {atividade['tipo']}, Descrição: {atividade['descricao']}")

            novo_tipo = input("Digite o novo tipo da atividade (pressione Enter para manter o atual): ").strip()
            nova_descricao = input("Digite a nova descrição da atividade (pressione Enter para manter a atual): ").strip()

            if novo_tipo:
                atividade['tipo'] = novo_tipo
            if nova_descricao:
                atividade['descricao'] = nova_descricao

            salvar(atividades)
            print("\nAtividade atualizada com sucesso!")
            return

    print(f"\nNenhuma atividade encontrada com o ID {id_atividade}.")


# visualizar
def listar():
    atividades = carregar()
    if not atividades:
        print("\nNenhuma atividade cadastrada para visualizar.")
        return
        
    print("\n--- LISTA DE TODAS AS ATIVIDADES CADASTRADAS ---")
    atividades_sorted = sorted(atividades, key=lambda x: x['id_evento'])
    
    for atividade in atividades_sorted:
        print(f"ID do Evento: {atividade['id_evento']} | ID da Atividade: {atividade['id_atividade']} | Tipo: {atividade['tipo']} | Descrição: {atividade['descricao']}")
    print("-------------------------------------------------")


# excluir
def deletar():
    print("\nFunção de exclusão ainda não implementada.")
    pass
# pesquisar
def pesquisar():
    print("\nFunção de pesquisa ainda não implementada.")
    pass

#menu
# def menu():
#     actions = {
#         '1': criar,
#         '2': listar,
#         '3': atualizar,
#         '4': deletar,
#         '5': pesquisar,
#     }
#     while True:
#         print('''
# \n=======  MENU DE ATIVIDADES =======
#         1. Cadastrar nova atividade
#         2. Visualizar todas as atividades
#         3. Atualizar uma atividade
#         4. Excluir uma atividade
#         5. Pesquisar atividade específica
#         6. Sair
# --------------------------------------''')
#         escolha = input('Escolha uma opção: ').strip()
        
#         if escolha == '6':
#             print("Finalizando!!")
#             break
        
#         funcao = actions.get(escolha)
        
#         if funcao:
#             funcao()
#         else:
#             print('Opção inválida, tente novamente.')

if __name__ == "__main__":
    # menu()
    criar()
    listar()
    atualizar()
    deletar()
    pesquisar()
    