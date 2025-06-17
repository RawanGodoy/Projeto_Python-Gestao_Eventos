import json, os
os.system('cls||clear')
from colorama import Fore as fr


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
        nome = input("DIGITE O NOME DO PARTICIPANTE: ").title().replace(" ","")
        if nome.isalpha():
            break
        print(fr.RED+"NOME INVÁLIDO, O NOME INSERIDO NÃO DEVE CONTER NÚMEROS"+fr.YELLOW)

    print(fr.GREEN+"(NOME CADASTRADO...)"+fr.YELLOW)

    while True:
        idade = input("DIGITE A IDADE DO PARTICIPANTE: ").strip()
        if idade.isdigit():
            idade = int(idade)
            pass
            if idade > 0:
                print(fr.GREEN+"(IDADE CADASTRADA...)"+fr.YELLOW)
                break
        print(fr.RED+"(ERROR!) DIGITE A IDADE EM FORMA DE NÚMERO E INTEIRO E MAIOR QUE 0..."+fr.YELLOW)
    

    
    while True:
        cidademorada = input(fr.YELLOW+"DIGITE A CIDADE DE MORADA DO PARTICIPANTE: ").title().replace(" ","")
        if cidademorada.isalpha():
            print(fr.GREEN+"(CIDADE CADASTRADA...)"+fr.YELLOW)
            break
        print(fr.RED+"(ERROR!) OS DADOS INSERIDOS SÃO INVÁLIDOS, DIGITE EM FORMA DE TEXTO..."+fr.YELLOW)
    
    while True:
        cpf = input("QUAL O CPF DO PARTICIPANTE? ").strip()
        if cpf.isdigit() and len(cpf) == 11:
            print(fr.GREEN+"(CPF CADASTRADO...)"+fr.YELLOW)
            cpf = int(cpf)
            break
        print(fr.RED+"O DADO INSERIDO ESTÁ INVÁLIDO. O CPF DEVE CONTER EXATAMENTE 11 NÚMEROS. TENTE NOVAMENTE..."+fr.YELLOW)

        
    while True:
        genero = input(fr.YELLOW+"QUAL SEU GÊNERO? USE (M/F)").lower().strip()
        if genero == "m":
             genero = "Masculino"
             break
        if genero == "f":
                genero = "Feminino"
                break
 
        print(fr.RED+"RESPOSTA INVÁLIDA, USE APENAS (M) OU (F)... "+fr.YELLOW)

    while True:
        encontrou = False
        while True:
            idevento = input("QUAL O ID DO EVENTO QUE DESEJA PARTICIPAR? ")
            if idevento.isdigit():
                idevento = int(idevento)
                break
            print(fr.RED+"DIGITE APENAS NÚMEROS..."+fr.YELLOW)


        for elementos in carregamento:
            if elementos['id'] == idevento:
                os.system('cls||clear')
                print(fr.GREEN+f"O PARTICIPANTE ({nome}) RESERVOU O EVENTO ({elementos['evento']}), DE ID ({idevento}), QUE SERÁ NO LOCAL ({elementos['local']})"+fr.YELLOW)
                encontrou = True
                break
        if encontrou:
            break
        else:
            print(fr.RED+"EVENTO NÃO ENCONTRADO"+fr.YELLOW) 
         
    dados = {'idevento' : idevento,'nome' : nome, 'idade' : idade, 'cidade' : cidademorada, 'cpf' : cpf, 'genero' : genero}
    base.append(dados)
    salvar(base)
    
    print(fr.GREEN+'''
         <CADASTRO REALIZADO COM SUCESSO>
'''+fr.YELLOW)
#Atualização dos dados do participante 
def atualizar():
    print()
    base = leitura()
    if not base:
        print(fr.RED+"NENHUM PARTICIPANTE CADASTRADO PARA ATUALIZAR.")
        input("PRESSIONE ENTER PARA CONTINUAR..."+fr.YELLOW)
        return
    #Enviar para gody
    while True:
            cpf_busca = input("DIGITE O CPF DO PARTICIPANTE QUE DESEJA ATUALIZAR: ").strip()
            if cpf_busca.isdigit() and len(cpf_busca) == 11:
                cpf_busca = int(cpf_busca)
                break
            print(fr.RED+"DIGITE UM (CPF) COM 11 NÚMEROS, SEM LETRAS OU PONTUAÇÕES..."+fr.YELLOW)
            
    encontrado = False

    for i, participante in enumerate(base):
        if participante.get('cpf') == cpf_busca:
            encontrado = True
            print(f"\nPARTICIPANTE ENCONTRADO: {participante['nome']} (CPF: {participante['cpf']})")
            
            
            made_changes = False

            while True:
                print("\nQUAL INFORMAÇÃO VOCÊ DESEJA ATUALIZAR? (DIGITE '0' PARA SAIR)")
                print("1. NOME")
                print("2. IDADE")
                print("3. CIDADE")
                print("4. GÊNERO")
                print("5. ID DO EVENTO")
                
                opcao_atualizacao = input("DIGITE O NÚMERO DA OPÇÃO (OU '0' PARA FINALIZAR): ").strip()

                if opcao_atualizacao == '0':
                    print(fr.GREEN+"FINALIZANDO ATUALIZAÇÃO."+fr.YELLOW)
                    break 
                elif opcao_atualizacao == '1':
                    novo_nome = input("DIGITE O NOVO NOME: ").strip()
                    if base[i]['nome'] != novo_nome: 
                        base[i]['nome'] = novo_nome
                        print(fr.GREEN+"NOME ATUALIZADO."+fr.YELLOW)
                        salvar(base) 
                        print(fr.GREEN+"\n<ALTERAÇÃO PENDENTE SALVA>\n"+fr.YELLOW)
                        made_changes = True
                    else:
                        print(fr.GREEN+"NOME NÃO ALTERADO, VALOR É O MESMO."+fr.YELLOW)
                elif opcao_atualizacao == '2':
                    while True:
                        nova_idade_str = input("DIGITE A NOVA IDADE: ").strip()
                        if nova_idade_str.isdigit():
                            nova_idade = int(nova_idade_str)
                            if base[i]['idade'] != nova_idade: 
                                base[i]['idade'] = nova_idade
                                print("IDADE ATUALIZADA.")
                                salvar(base) 
                                print(fr.GREEN+"\n<ALTERAÇÃO PENDENTE SALVA>\n"+fr.YELLOW)
                                made_changes = True
                            else:
                                print(fr.GREEN+"IDADE NÃO ALTERADA, VALOR É O MESMO."+fr.YELLOW)
                            break
                        else:
                            print(fr.RED+"IDADE INVÁLIDA. POR FAVOR, DIGITE UM NÚMERO."+fr.YELLOW)
                elif opcao_atualizacao == '3':
                    nova_cidade = input("DIGITE A NOVA CIDADE: ").strip()
                    if base[i]['cidade'] != nova_cidade: 
                        base[i]['cidade'] = nova_cidade
                        print(fr.GREEN+"CIDADE ATUALIZADA."+fr.YELLOW)
                        salvar(base) 
                        print(fr.GREEN+"\n<ALTERAÇÃO PENDENTE SALVA>\n"+fr.YELLOW)
                        made_changes = True
                    else:
                        print(fr.GREEN+"CIDADE NÃO ALTERADA, VALOR É O MESMO."+fr.YELLOW)
                elif opcao_atualizacao == '4':
                    novo_genero = ""
                    while novo_genero not in ["Masculino", "Feminino"]:
                        genero_input = input("DIGITE O NOVO GÊNERO (M/F): ").strip().lower()
                        if genero_input == "m":
                            novo_genero = "Masculino"
                        elif genero_input == "f":
                            novo_genero = "Feminino"
                        else:
                            print(fr.RED+"OPÇÃO DE GÊNERO INVÁLIDA. POR FAVOR, USE 'M' OU 'F'."+fr.YELLOW)
                    if base[i]['genero'] != novo_genero: 
                        base[i]['genero'] = novo_genero
                        print(fr.GREEN+"GÊNERO ATUALIZADO."+fr.YELLOW)
                        salvar(base) 
                        print(fr.GREEN+"\n<ALTERAÇÃO PENDENTE SALVA>\n"+fr.YELLOW)
                        made_changes = True
                    else:
                        print(fr.GREEN+"GÊNERO NÃO ALTERADO, VALOR É O MESMO."+fr.YELLOW)
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
                                        print(fr.GREEN+"\n<ALTERAÇÃO PENDENTE SALVA>\n"+fr.YELLOW)
                                        made_changes = True
                                    else:
                                        print(fr.GREEN+"ID do Evento não alterado, valor é o mesmo."+fr.YELLOW)
                                    encontrou_novo_evento = True
                                    break
                            if not encontrou_novo_evento:
                                print(fr.RED+"Evento não encontrado. Por favor, digite um ID de evento válido."+fr.YELLOW)
                        except ValueError:
                            print(fr.RED+"ID de evento inválido. Por favor, digite um número."+fr.YELLOW)
                else:
                    print(fr.RED+"Opção inválida.+fr.YELLOW")
            
            
            if made_changes:
                print(fr.GREEN+"\n<PARTICIPANTE ATUALIZADO COM SUCESSO>\n"+fr.YELLOW)
            else:
                print(fr.GREEN+"\n<NENHUMA ATUALIZAÇÃO REALIZADA>\n"+fr.YELLOW)
            break 
    
    if not encontrado:
        print(fr.RED+"Participante com o CPF informado não encontrado."+fr.YELLOW)
    
    input(fr.GREEN+"Pressione Enter para continuar...+fr.YELLOW")



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
        print(fr.GREEN+f"""
              ID EVENTO DO PARTICIPANTE | {id_participante}
              NOME      | {nome}
              IDADE     | {idade}
              CIDADE    | {cidade}
              CPF       | {cpf}
              GÊNERO    | {genero}"""+fr.YELLOW)


#Exclusão dos participantes
def deletar():
    base = leitura()
    if not base:
        print(fr.RED+"NENHUM PARTICIPANTE CADASTRADO COM ESSE CPF. ")
        input("PARA VOLTAR AO MENU, PRESSIONE A TECLA ENTER."+fr.YELLOW)
        return

    cpf_excluir = input("DIGITE O CPF DO PARTICIPANTE QUE DESEJA EXCLUIR: ").strip()
    
    initial_length = len(base)
    base = [participante for participante in base if participante.get('cpf') != cpf_excluir]

    if len(base) < initial_length:
        salvar(base)
        print(fr.GREEN+"\nPARTICIPANTE EXCLUIDO COM SUCESSO! \n"+fr.YELLOW)
    else:
        print(fr.RED+"PARTICIPANTE COM O CPF INFORMADO NÃO ENCONTRADO."+fr.YELLOW)
    
    input(fr.GREEN+"PARA VOLTAR AO MENU, PRESSIONE A TECLA ENTER."+fr.YELLOW)

#Pesquisar participante
def pesquisar():
    base = leitura()
    
    if not base:
        print(fr.RED+"Não existem participantes para pesquisar."+fr.YELLOW)
        return

    print('''
--- PESQUISAR PARTICIPANTE ---
1. Por CPF
2. Por Nome
3. Por ID do Evento
    ''')

    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        while True:
            cpf = input("Digite o CPF do participante: ")
            if cpf.isdigit() and len(cpf) == 11:
                cpf = int(cpf)
                break
            print(fr.RED+"Digite um (CPF) com 11 números, sem letras ou pontuações..."+fr.YELLOW)

        encontrou = False
        for participante in base:
            if participante['cpf'] == cpf:
                print(fr.GREEN+"\nParticipante encontrado:")
                print("Nome:", participante['nome'])
                print("Idade:", participante['idade'])
                print("Cidade:", participante['cidade'])
                print("Gênero:", participante['genero'])
                print("ID do Evento:", participante['idevento']+fr.YELLOW)
                encontrou = True
        if not encontrou:
            print(fr.RED+"Nenhum participante com esse CPF."+fr.YELLOW)

    elif opcao == '2':
        nome = input("Digite o nome do participante: ")
        encontrou = False
        for participante in base:
            if nome == participante['nome']:
                print(fr.GREEN+"\nParticipante encontrado:")
                print("Nome:", participante['nome'])
                print("Idade:", participante['idade'])
                print("Cidade:", participante['cidade'])
                print("Gênero:", participante['genero'])
                print("CPF:", participante['cpf'])
                print("ID do Evento:", participante['idevento']+fr.YELLOW)
                encontrou = True
        if not encontrou:
            print(fr.RED+"Nenhum participante com esse nome."+fr.YELLOW)

    elif opcao == '3':
        try:
            idevento = int(input("Digite o ID do evento: "))
            encontrou = False
            for participante in base:
                if participante['idevento'] == idevento:
                    print(fr.GREEN+"\nParticipante do evento encontrado:")
                    print("Nome:", participante['nome'])
                    print("CPF:", participante['cpf'])
                    print("Cidade:", participante['cidade'])
                    print("Gênero:", participante['genero'])
                    print("CPF:", participante['cpf'])
                    print("ID do Evento:", participante['idevento']+fr.YELLOW)
                    encontrou = True
            if not encontrou:
                print(fr.RED+"Nenhum participante encontrado para esse evento."+fr.YELLOW)
        except:
            print(fr.RED+"ID inválido. Digite um número inteiro."+fr.YELLOW)

    else:
        print(fr.RED+"Opção inválida."+fr.YELLOW)

if __name__ == "__main__":
    criar()
    listar()
    atualizar()
    deletar()
    pesquisar()
    