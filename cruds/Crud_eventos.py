#BIBLIOTECAS
import json
from datetime import datetime
from colorama import Fore as fr
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
        data = input("DIGITE A DATA NO FORMATO DD/MM/AA: ")
        try:
            # Tenta converter para datetime
            data_valida = datetime.strptime(data, "%d/%m/%y")
            print("Data válida:", data_valida.strftime("%d/%m/%y"))
            return data_valida.strftime("%d/%m/%y")
        except ValueError:
            print(fr.RED+"DATA INVÁLIDA, TENTE NOVAMENTE."+fr.BLUE)
def solicitar_horario():
    while True:
        horario = input("(FORMATO HH:MM): ")
        try:
            horario_valido = datetime.strptime(horario, "%H:%M")
            print(fr.GREEN+"Horário válido:", horario_valido.strftime("%H:%M")+fr.BLUE)
            return horario_valido.strftime("%H:%M")
        except ValueError:
            print(fr.RED+"HORÁRIO INVÁLIDO, TENTE NOVAMENTE."+fr.BLUE)
            
#Criar registros
def criar():
    base = carregar()
    proximo_id = max((r['id'] for r in base), default = 0) + 1
    evento = input('DIGITE O NOME DO EVENTO: ').strip()
    print(fr.GREEN+"CADASTRADO COM SUCESSO!"+fr.BLUE)
    data = solicitar_data()
    print(fr.GREEN+"CADASTRADO COM SUCESSO!"+fr.BLUE)
    print("DIGITE O HORÁRIO DE INÍCIO DO EVENTO: ")
    horario_inicio = solicitar_horario()
    print(fr.GREEN+"CADASTRADO COM SUCESSO!"+fr.BLUE)
    print("DIGITE O HORÁRIO DE TÉRMINO DO EVENTO: ")
    horario_fim = solicitar_horario()
    print(fr.GREEN+"CADASTRADO COM SUCESSO!"+fr.BLUE)
    while True:
        local = input("DIGITE O LOCAL DO EVENTO: ").title().replace(" ","")
        if not local.isalpha():
            print(fr.RED+"O LOCAL DO EVENTO NÃO PODE CONTER NÚMEROS."+fr.BLUE)
        else:
            print(fr.GREEN+"CADASTRADO COM SUCESSO!"+fr.BLUE)
            break
    registro = {'id': proximo_id, 'evento': evento,'data': data,'hora_inicio':horario_inicio,'hora_fim':horario_fim,'local':local}
    base.append(registro) 
    salvar(base)
    print(f'Registro criado: {registro}')
#Listar
def listar():
    base = carregar()
    
    if not base:
        print(fr.RED+"NENHUM EVENTO ENCONTRADO"+fr.BLUE)
        return

    print(fr.GREEN+"EVENTOS CADASTRADOS:\n")
    for evento in base:
        id = evento["id"]
        nome = evento["evento"]
        data = evento["data"]
        horario_inicio = evento["hora_inicio"]
        horario_fim = evento["hora_fim"]
        local = evento["local"]
        print(fr.GREEN+f"""
                ---------------------------
                ID     | {id}
                NOME   | {nome}
                DATA   | {data}
                INÍCIO | {horario_inicio}
                FIM    | {horario_fim}
                LOCAL  | {local}"""+fr.BLUE)
#Atualizar
def atualizar():
    base = carregar()
    encontrou = False
    try:
        id_escolhido = int(input("DIGITE O ID DO EVENTO QUE DESEJA ATUALIZAR: "))
        for evento in base:
            if evento['id'] == id_escolhido:
                print(fr.GREEN+f"""
                == DADOS ATUAIS DO EVENTO ==
                NOME   | {evento['evento']}
                DATA   | {evento['data']}
                INÍCIO | {evento['hora_inicio']}
                FIM    | {evento['hora_fim']}
                LOCAL  | {evento['local']}"""+fr.BLUE)
                encontrou = True
                
                mudar_nome = input('Deseja mudar o nome? (S/N): ').strip().upper()
                while True:
                    if mudar_nome == 'S':
                        novo_nome = input("Novo nome do evento: ").strip() or evento['evento']
                        evento['evento'] = novo_nome
                        break
                    elif mudar_nome == 'N':
                        break
                    else:
                        print(fr.RED+"Opção inválida."+fr.BLUE)
                        mudar_nome = input('Deseja mudar o nome? (S/N): ').strip().upper()       
                mudar_data = input("Deseja alterar a data? (S/N): ").strip().upper()
                while True:
                    if mudar_data == "S":
                        nova_data = solicitar_data()
                        evento['data'] = nova_data
                        break
                    elif mudar_data == "N":
                        break
                    else:
                        print(fr.RED+"Opção inválida."+fr.BLUE)
                        mudar_data = input("Deseja alterar a data? (S/N): ").strip().upper()

                mudar_hora1 = input("Deseja alterar o horário inicial? (S/N): ").strip().upper()
                while True:
                    if mudar_hora1 == 'S':
                        nova_hora = solicitar_horario()
                        evento['hora_inicio'] = nova_hora
                        break
                    elif mudar_hora1 == 'N':
                        break
                    else:
                        print(fr.RED+"Opção inválida."+fr.BLUE)
                        mudar_hora1 = input("Deseja alterar o horário inicial? (S/N): ").strip().upper()
                    
                mudar_hora2 = input("Deseja alterar o horário final? (S/N) ").strip().upper()
                while True:
                    if mudar_hora2 == 'S':
                        nova_hora = solicitar_horario()
                        evento['hora_inicio'] = nova_hora
                        break
                    elif mudar_hora2 == 'N':
                        break
                    else:
                        print(fr.RED+"Opção inválida."+fr.BLUE)
                        mudar_hora2 = input("Deseja alterar o horário inicial? (S/N): ").strip().upper()

                mudar_local = input("Deseja alterar o local do evento? (S/N) ").strip().upper()
                while True:
                    if mudar_local == 'S':
                        novo_local = input("Qual o local do evento? ")
                        evento['local'] = novo_local
                        break
                    elif mudar_local == 'N':
                        break
                    else:
                        print(fr.RED+"Opção inválida."+fr.BLUE)
                        mudar_local =  input("Deseja alterar o local do evento? (S/N): ").strip().upper()
                salvar(base)
                print(fr.GREEN+f"""
                == EVENTO ATUALIZADO ==
                NOME   | {evento['evento']}
                DATA   | {evento['data']}
                INÍCIO | {evento['hora_inicio']}
                FIM    | {evento['hora_fim']}
                LOCAL  | {evento['local']}"""+fr.BLUE)
                return
        if not encontrou:
            print(fr.RED+"EVENTO NÃO ENCONTRADO."+fr.BLUE)
    except ValueError:
        print(fr.RED+"ID INVÁLIDO. TENTE NOVAMENTE."+fr.BLUE)
#Delete
def deletar():
    base = carregar()
    
    if not base:
        print(fr.RED+"NÃO HÁ REGISTROS PARA DELETAR. VOLTANDO PARA O INÍCIO."+fr.BLUE)
        return

    listar()
    
    ids_input = input("DIGITE O ID DE EVENTO QUE DESEJA DELETAR (caso queira deletar mais de um ID separare por vírgula): ")
    
    try:
        ids_a_deletar = set(int(i.strip()) for i in ids_input.split(",") if i.strip().isdigit())

        if not ids_a_deletar:
            print(fr.RED+"NENHUM ID VÁLIDO FORNECIDO."+fr.BLUE)
            return

        base_nova = [r for r in base if r['id'] not in ids_a_deletar]
        deletados = len(base) - len(base_nova)

        if deletados == 0:
            print(fr.RED+"NENHUM DOS IDS FORNECIDOS FORAM ENCONTRADOS."+fr.BLUE)
        else:
            salvar(base_nova)
            print(fr.GREEN+f"{deletados} REGISTRO(S) DELETADO(S) COM SUCESSO."+fr.BLUE)
            
    except ValueError:
        print(fr.RED+"ERRO: CERTIFIQUE-SE DE DIGITAR APENAS NÚMEROS INTEIROS SEPARADOS POR VÍRGULA."+fr.BLUE)

#Pesquisa
def pesquisar():
    base = carregar()
    
    if not base:
        print(fr.RED+"NÃO HÁ REGISTROS PARA PESQUISAR."+fr.BLUE)
        return

    try:
        id_busca = int(input("DIGITE O ID DO EVENTO QUE DESEJA BUSCAR: "))
        for r in base:
            if r['id'] == id_busca:
                print(fr.GREEN+f"""
                == EVENTO ENCONTRADO ==
                ID     | {r['id']}
                NOME   | {r['evento']}
                DATA   | {r['data']}
                INÍCIO | {r['hora_inicio']}
                FIM    | {r['hora_fim']}
                LOCAL  | {r['local']}"""+fr.BLUE)
                return
        print(fr.RED+"ID NÃO ENCONTRADO."+fr.BLUE)
    except ValueError:
        print(fr.RED+"ID INVÁLIDO. TENTE NOVAMENTE."+fr.BLUE)

if __name__ == "__main__":
    pesquisar()
    deletar()
    criar()
    atualizar()
    listar()