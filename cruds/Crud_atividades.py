import json
from colorama import Fore as fr

arquivo_atividades = "dados/atividades.json"
arquivo_eventos = "dados/eventos.json"


def salvar(base):
    with open(arquivo_atividades,'w',encoding = 'utf-8') as f:
        json.dump(base, f, indent = 4, ensure_ascii = False)
        
def carregar():
    try:
        with open(arquivo_atividades,"r") as f:
            registros = json.load(f)
            return registros
    except FileNotFoundError:
        return []

def criar():
    atividades = carregar()
    try:
        with open(arquivo_eventos, "r", encoding="utf-8") as f:
            eventos = json.load(f)
    except FileNotFoundError:
        print(fr.RED+"ARQUIVO DE EVENTOS NÃO ENCONTRADO EM '" + arquivo_eventos + "'. CRIE UM EVENTO PRIMEIRO."+fr.CYAN)
        return

    while True:
        try:
            id_evento_str = input("DIGITE O ID DO EVENTO PARA VINCULAR A ATIVIDADE: ")
            id_evento = int(id_evento_str)
            
            if any(evento['id'] == id_evento for evento in eventos):
                break
            else:
                print(fr.RED+"ERRO: NENHUM EVENTO ENCONTRADO COM ESTE ID. TENTE NOVAMENTE."+fr.CYAN)
        except ValueError:
            print(fr.RED+"ID INVÁLIDO. POR FAVOR, DIGITE UM NÚMERO."+fr.CYAN)

    
    for atividade_existente in atividades:
        if atividade_existente['id_evento'] == id_evento:
            print(fr.RED+f"\n ERRO: O EVENTO COM ID {id_evento} JÁ POSSUI UMA ATIVIDADE VINCULADA.")
            print("UM EVENTO SÓ PODE TER UMA ATIVIDADE.")
            print(" PARA MODIFICAR A ATIVIDADE EXISTENTE, POR FAVOR, VOLTE AO MENU E ESCOLHA A OPÇÃO '3. ATUALIZAR'."+fr.CYAN)
            return 

    while True:
        tipo_atividade = input("DIGITE O TIPO DA ATIVIDADE (EX: PALESTRA, OFICINA): ").strip()
        if tipo_atividade.isalpha():
            break
        print(fr.RED+"DIGITE APENAS LETRAS..."+fr.CYAN)
    
    while True:
        descricao = input("DESCREVA A ATIVIDADE: ").strip()
        if len(descricao) >= 10:
            break
        print(fr.RED+"A DESCRIÇÃO DEVE CONTER NO MINIMO 10 CARACTERES..."+fr.CYAN)

    proximo_id = max((a.get('id_atividade', 0) for a in atividades), default=0) + 1
    nova_atividade = {
        'id_atividade': proximo_id,
        'id_evento': id_evento,
        'tipo': tipo_atividade,
        'descricao': descricao
    }

    atividades.append(nova_atividade)
    salvar(atividades)
    
    print(fr.GREEN+"\n ATIVIDADE CADASTRADA E VINCULADA AO EVENTO COM SUCESSO!")
    print("--- DADOS DA ATIVIDADE CADASTRADA ---")
    print(f"ID ÚNICO DA ATIVIDADE: {nova_atividade['id_atividade']}")
    print(f"VINCULADA AO EVENTO DE ID: {nova_atividade['id_evento']}")
    print(f"TIPO: {nova_atividade['tipo']}")
    print(f"DESCRIÇÃO: {nova_atividade['descricao']}")
    print("-------------------------------------"+fr.CYAN)

def atualizar():
    atividades = carregar()
    if not atividades:
        print(fr.RED+"\nNÃO HÁ ATIVIDADES CADASTRADAS PARA ATUALIZAR."+fr.CYAN)
        return

    try:
        id_atividade = int(input("DIGITE O ID DA ATIVIDADE QUE DESEJA ATUALIZAR: "))
    except ValueError:
        print(fr.RED+"ID INVÁLIDO. POR FAVOR, INSIRA UM NÚMERO INTEIRO."+fr.CYAN)
        return

    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            print(fr.GREEN+f"\nATIVIDADE ENCONTRADA: ID {atividade['id_atividade']}, TIPO: {atividade['tipo']}, DESCRIÇÃO: {atividade['descricao']}"+fr.CYAN)
            while True:
                novo_tipo = input("DIGITE O NOVO TIPO DA ATIVIDADE (PRESSIONE ENTER PARA MANTER O ATUAL): ").strip() or atividade['tipo']
                if novo_tipo.isalpha():
                    break
                print(fr.RED+"DIGITE APENAS LETRAS..."+fr.CYAN)
            
            while True:
                nova_descricao = input("DIGITE A NOVA DESCRIÇÃO DA ATIVIDADE (PRESSIONE ENTER PARA MANTER A ATUAL): ").strip() or atividade['descricao']
                if len(nova_descricao) >= 10:
                    break
                print(fr.RED+"A DESCRIÇÃO DEVE CONTER NO MINIMO 10 CARACTERES..."+fr.CYAN)

            if novo_tipo:
                atividade['tipo'] = novo_tipo
            if nova_descricao:
                atividade['descricao'] = nova_descricao

            salvar(atividades)
            print(fr.GREEN+"\nAtividade atualizada com sucesso!"+fr.CYAN)
            return

    print(fr.RED+f"\nNENHUMA ATIVIDADE ENCONTRADA COM O ID {id_atividade}."+fr.CYAN)

def listar():
    atividades = carregar()
    if not atividades:
        print(fr.RED+"\nNENHUMA ATIVIDADE CADASTRADA PARA VISUALIZAR."+fr.CYAN)
        return
        
    print(fr.GREEN+"\n--- LISTA DE TODAS AS ATIVIDADES CADASTRADAS ---")
    atividades_sorted = sorted(atividades, key=lambda x: x['id_evento'])
    
    for atividade in atividades_sorted:
        print(f"ID DO EVENTO: {atividade['id_evento']} | ID DA ATIVIDADE: {atividade['id_atividade']} | TIPO: {atividade['tipo']} | DESCRIÇÃO: {atividade['descricao']}")
    print("-------------------------------------------------"+fr.CYAN)

def deletar():
    atividades = carregar()
    if not atividades:
        print(fr.RED+"\nNENHUMA ATIVIDADE CADASTRADA PARA EXCLUIR.")
        input("PRESSIONE ENTER PARA VOLTAR AO MENU."+fr.CYAN)
        return
    try:
        id_excluir = int(input("DIGITE O ID DA ATIVIDADE QUE DESEJA EXCLUIR: "))
    except ValueError:
        print(fr.RED+"ID INVÁLIDO. POR FAVOR, INSIRA UM NÚMERO INTEIRO."+fr.CYAN)
        return
    
    original_len = len(atividades)
    atividades = [a for a in atividades if a.get('id_atividade') != id_excluir]

    if len(atividades) < original_len:
        salvar(atividades)
        print(fr.GREEN+"\nATIVIDADE EXCLUÍDA COM SUCESSO!"+fr.CYAN)
    else:
        print(fr.RED+"ATIVIDADE COM O ID INFORMADO NÃO ENCONTRADA."+fr.CYAN)

def pesquisar():
    base = carregar()
    try:
        id_atividade = int(input("DIGITE O ID DA ATIVIDADE QUE DESEJA VISUALIZAR: "))
        encontrou = False
        for atv in base:
            if id_atividade == atv['id_atividade']:
                print(fr.GREEN+f"""
    ID          | {atv['id_atividade']}
    ID EVENTO   | {atv['id_evento']}
    TIPO        | {atv['tipo']}
    DESCRIÇÃO   | {atv['descricao']}"""+fr.CYAN)   
                encontrou = True
        if not encontrou:
            print(fr.RED+"O ID DIGITADO NÃO FOI ENCONTRADO."+fr.CYAN)
    except ValueError:
        print(fr.RED+"ID NÃO VÁLIDO."+fr.CYAN)
    

if __name__ == "__main__":
    criar()
    listar()
    atualizar()
    deletar()
    pesquisar()