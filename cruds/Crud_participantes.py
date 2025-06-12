import json, os
os.system('cls||clear')

arquivogeral = 'dados/participantes.json'
arquivoid = 'dados/eventos.json'


#Criei a função de salvar o arquivo no json
def salvar(basearquivo):
    with open(arquivogeral, 'w', encoding='utf-8') as adicionar:
        json.dump(basearquivo,adicionar,indent=4,ensure_ascii=False)

#Defini a função para ler o arquivo
def leitura():
    with open(arquivogeral,'r') as elementos:
        try: 
            leitura = json.load(elementos)
            return leitura
        except FileNotFoundError:
            return[]

#Defino a função de leitura do json do outro crud, o crud de eventos, irei precisar acessar o json para buscar o ID que o usuário pesquisar
def leitura2():
    with open(arquivoid,'r') as elementos:
        try: 
            leitura2 = json.load(elementos)
            return leitura2
        except FileNotFoundError:
            return[]

#Criei a função para cadastrar o arquivo
def criar():
    base = leitura()
    carregamento = leitura2()
    while True:
        nome = input("Digite o nome do participante: ")
        if not nome.isdigit():
            break
        print("Nome inválido, o nome inserido não pode conter números")

    print("(Nome cadastrado...)")

    while True:
        idade = input("Digite a idade do participante: ")
        if idade.isdigit():
            idade = int(idade)
            print("(Idade cadastrada...)")
            break
        print("(ERROR!) Digite a idade em forma de número...")
    
    while True:
        cidademorada = input("Digite a cidade de morada do participante: ")
        if not cidademorada.isdigit():
            print("(Cidade cadastrada...)")
            break
        print("(ERROR!) Os dados inseridos são inválidos, digite em forma de texto...")
    
    while True:
        cpf = input("Qual o cpf do participante? ")
        if cpf.isdigit():
            print("(Cpf cadastrado...)")
            cpf = int(cpf)
            break
        print("O dado inserido está inválido, tente novamente...")
    
    while True:
        genero = input("Qual seu gênero? Use (M/F)").lower()

        if genero == "m":
             genero = "Masculino"
             break
        if genero == "f":
                genero = "Feminino"
                break
 
        print("Resposta inválida, use apenas (M) ou (F)... ")


    #Defino a variavel de controle para o meu while

    while True:
        encontrou = False

        idevento = int(input("Qual o id do evento que deseja participar? "))

        for elementos in carregamento:
            if elementos['id'] == idevento:
                os.system('cls||clear')
                print(f"O participante ({nome}) reservou o evento ({elementos['evento']}), de id ({idevento}), que será no local ({elementos['local']})")
                encontrou = True
                break
        if encontrou:
            break
        else:
            print("Evento não encontrado") 
         
    dados = {'idevento' : idevento,'nome' : nome, 'idade' : idade, 'cidade' : cidademorada, 'cpf' : cpf, 'genero' : genero}
    base.append(dados)
    salvar(base)
    
    print('''
         <CADASTRO REALIZADO COM SUCESSO>
''')



#Atualização dos dados do participante 
def atualizar():
    print()
   #Atualiza os dados de um participante existente com base no seu CPF, permitindo que vários campos sejam atualizados.
    base = leitura()
    if not base:
        print("Nenhum participante cadastrado para atualizar.")
        input("Pressione Enter para continuar...")
        return

    cpf_busca = input("Digite o CPF do participante que deseja atualizar: ").strip()
    encontrado = False

    for i, participante in enumerate(base):
        if participante.get('cpf') == cpf_busca:
            encontrado = True
            print(f"\nParticipante encontrado: {participante['nome']} (CPF: {participante['cpf']})")
            
            
            made_changes = False

            while True:
                print("\nQual informação você deseja atualizar? (Digite '0' para sair)")
                print("1. Nome")
                print("2. Idade")
                print("3. Cidade")
                print("4. Gênero")
                print("5. ID do Evento")
                
                opcao_atualizacao = input("Digite o número da opção (ou '0' para finalizar): ").strip()

                if opcao_atualizacao == '0':
                    print("Finalizando atualização.")
                    break 
                elif opcao_atualizacao == '1':
                    novo_nome = input("Digite o novo nome: ").strip()
                    if base[i]['nome'] != novo_nome: 
                        base[i]['nome'] = novo_nome
                        print("Nome atualizado.")
                        salvar(base) 
                        print("\n<ALTERAÇÃO PENDENTE SALVA>\n")
                        made_changes = True
                    else:
                        print("Nome não alterado, valor é o mesmo.")
                elif opcao_atualizacao == '2':
                    while True:
                        nova_idade_str = input("Digite a nova idade: ").strip()
                        if nova_idade_str.isdigit():
                            nova_idade = int(nova_idade_str)
                            if base[i]['idade'] != nova_idade: 
                                base[i]['idade'] = nova_idade
                                print("Idade atualizada.")
                                salvar(base) 
                                print("\n<ALTERAÇÃO PENDENTE SALVA>\n")
                                made_changes = True
                            else:
                                print("Idade não alterada, valor é o mesmo.")
                            break
                        else:
                            print("Idade inválida. Por favor, digite um número.")
                elif opcao_atualizacao == '3':
                    nova_cidade = input("Digite a nova cidade: ").strip()
                    if base[i]['cidade'] != nova_cidade: 
                        base[i]['cidade'] = nova_cidade
                        print("Cidade atualizada.")
                        salvar(base) 
                        print("\n<ALTERAÇÃO PENDENTE SALVA>\n")
                        made_changes = True
                    else:
                        print("Cidade não alterada, valor é o mesmo.")
                elif opcao_atualizacao == '4':
                    novo_genero = ""
                    while novo_genero not in ["Masculino", "Feminino"]:
                        genero_input = input("Digite o novo gênero (M/F): ").strip().lower()
                        if genero_input == "m":
                            novo_genero = "Masculino"
                        elif genero_input == "f":
                            novo_genero = "Feminino"
                        else:
                            print("Opção de gênero inválida. Por favor, use 'M' ou 'F'.")
                    if base[i]['genero'] != novo_genero: 
                        base[i]['genero'] = novo_genero
                        print("Gênero atualizado.")
                        salvar(base) 
                        print("\n<ALTERAÇÃO PENDENTE SALVA>\n")
                        made_changes = True
                    else:
                        print("Gênero não alterado, valor é o mesmo.")
                elif opcao_atualizacao == '5':
                    carregamento_eventos = leitura2()
                    novo_idevento = -1
                    encontrou_novo_evento = False
                    while not encontrou_novo_evento:
                        try:
                            novo_idevento = int(input("Digite o novo ID do evento: ").strip())
                            for evento in carregamento_eventos:
                                if evento.get('id') == novo_idevento:
                                    if base[i]['idevento'] != novo_idevento: 
                                        base[i]['idevento'] = novo_idevento
                                        print(f"O participante ({participante['nome']}) agora está associado ao evento ({evento['evento']}).")
                                        salvar(base) 
                                        print("\n<ALTERAÇÃO PENDENTE SALVA>\n")
                                        made_changes = True
                                    else:
                                        print("ID do Evento não alterado, valor é o mesmo.")
                                    encontrou_novo_evento = True
                                    break
                            if not encontrou_novo_evento:
                                print("Evento não encontrado. Por favor, digite um ID de evento válido.")
                        except ValueError:
                            print("ID de evento inválido. Por favor, digite um número.")
                else:
                    print("Opção inválida.")
            
            
            if made_changes:
                print("\n<PARTICIPANTE ATUALIZADO COM SUCESSO>\n")
            else:
                print("\n<NENHUMA ATUALIZAÇÃO REALIZADA>\n")
            break 
    
    if not encontrado:
        print("Participante com o CPF informado não encontrado.")
    
    input("Pressione Enter para continuar...")



#Visualização dos participantes
def listar():
    i = 0
    base = leitura()


    for elementos in base:

        i+=1

        id_participante = elementos['idevento']
        nome = elementos['nome']
        idade = elementos['idade']
        cidade = elementos['cidade']
        cpf = elementos['cpf']
        genero = elementos['genero']
        print()
        print(f"""
              ID EVENTO DO PARTICIPANTE | {id_participante}
              NOME      | {nome}
              IDADE     | {idade}
              CIDADE    | {cidade}
              CPF       | {cpf}
              GÊNERO    | {genero}""")


#Exclusão dos participantes
def deletar():
    base = leitura()
    if not base:
        print("Nenhum participante cadastrado com esse CPF. ")
        input("Para voltar ao menu, pressione a tecla Enter.")
        return

    cpf_excluir = input("Digite o CPF do participante que deseja excluir: ").strip()
    
    initial_length = len(base)
    base = [participante for participante in base if participante.get('cpf') != cpf_excluir]

    if len(base) < initial_length:
        salvar(base)
        print("\nParticipante excluido com sucesso! \n")
    else:
        print("Participante com o CPF informado não encontrado.")
    
    input("Para voltar ao menu, pressione a tecla Enter.")

#Pesquisar participante
def pesquisar():
    base = leitura()
    
    if not base:
        print("Não existem participantes para pesquisar.")
        return

    print('''
--- PESQUISAR PARTICIPANTE ---
1. Por CPF
2. Por Nome
3. Por ID do Evento
    ''')

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cpf = input("Digite o CPF do participante: ")
        encontrou = False
        for participante in base:
            if participante['cpf'] == cpf:
                print("\nParticipante encontrado:")
                print("Nome:", participante['nome'])
                print("Idade:", participante['idade'])
                print("Cidade:", participante['cidade'])
                print("Gênero:", participante['genero'])
                print("ID do Evento:", participante['idevento'])
                encontrou = True
        if not encontrou:
            print("Nenhum participante com esse CPF.")

    elif opcao == '2':
        nome = input("Digite o nome do participante: ")
        encontrou = False
        for participante in base:
            if nome == participante['nome']:
                print("\nParticipante encontrado:")
                print("Nome:", participante['nome'])
                print("Idade:", participante['idade'])
                print("Cidade:", participante['cidade'])
                print("Gênero:", participante['genero'])
                print("CPF:", participante['cpf'])
                print("ID do Evento:", participante['idevento'])
                encontrou = True
        if not encontrou:
            print("Nenhum participante com esse nome.")

    elif opcao == '3':
        try:
            idevento = int(input("Digite o ID do evento: "))
            encontrou = False
            for participante in base:
                if participante['idevento'] == idevento:
                    print("\nParticipante do evento encontrado:")
                    print("Nome:", participante['nome'])
                    print("CPF:", participante['cpf'])
                    print("Cidade:", participante['cidade'])
                    encontrou = True
            if not encontrou:
                print("Nenhum participante encontrado para esse evento.")
        except:
            print("ID inválido. Digite um número inteiro.")

    else:
        print("Opção inválida.")

#Menu de escolhas 
# def menu():
#     op = {
#         '1': criar,
#         '2': atualizar,
#         '3': listar,
#         '4': deletar,
#         '5': pesquisar,
#         '6': exit
#     }

#     while True:
#         print('''
#         ---MENU INICIAL---
#         1. CADASTRAMENTO
#         2. ATUALIZAÇÃO
#         3. VISUALIZAÇÃO DE PARTICIPANTES
#         4. EXCLUSÃO DE PARTICIPANTES
#         5. PESQUISAR PARTICIPANTE
#         6. SAIR DO PROGRAMA
#         ''')
        
#         numero = input("Qual a opção desejada? ").strip()
#         desejo = op.get(numero)
        
#         if desejo:
#             desejo()
#         else:
#             print("Opção inválida, tente novamente...")


if __name__ == "__main__":
    # menu()
    criar()
    listar()
    atualizar()
    deletar()
    pesquisar()
    