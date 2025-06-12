#Importação dos arquivos dos cruds anteriores, já que estamos usando modularizaçao no projeto
import cruds.Crud_eventos as eventos
import cruds.Crud_participantes as participantes
import cruds.Crud_atividades as atividades

# função que inicia a função de determinado crud
# lambda é uma função simples, que não precisa ser declarada
# assim esses comando só iniciarão quando chamados
def menu_crud(nome, mod):
    #dicionário com as funções padronizadas de cada crud
    #quando chamada, inicia o comando do script selecionado
    funcao_crud ={
        '1' : lambda : mod.criar(),
        '2' : lambda : mod.listar(),
        '3' : lambda : mod.atualizar(),
        '4' : lambda : mod.deletar(),
        '5' : lambda : mod.pesquisar()
    }
    while True:
        print(f"""
      {'-'*10} MENU {nome} {'-'*10}
    1 | CRIAR
    2 | LISTAR
    3 | ATUALIZAR
    4 | DELETAR
    5 | PESQUISAR
    0 | VOLTAR""")
        
        #escolhe a função
        escolha_funcao = input("Opção: ")
        #caso seja o comando de retorno
        if escolha_funcao == '0':
            print("Retornando...")
            break
        #se não é o de retorno, continua e recebe a opção
        #armazena a função de acordo com a escolha do usuário
        opcao_funcao = funcao_crud.get(escolha_funcao)
        #se a função foi encontrada, executa, se não, dá como inválida
        if opcao_funcao:
            opcao_funcao()
        else:
            print("Opção inválida, tente novamente!")
        
#menu principal
def menu_principal():
    #opções de crud, mesma coisa do lambda
    crud = {
        '1': lambda: menu_crud("EVENTOS", eventos),
        '2' : lambda: menu_crud("PARTICIPANTES", participantes),
        '3' : lambda: menu_crud("ATIVIDADES",atividades),
        '0' : exit
    }
    while True:
        print(f"""
    {'-'*10} MENU GESTÃO DE EVENTOS {'-'*10}
    1 | GERENCIAR EVENTOS
    2 | GERENCIAR PARTICIPANTES
    3 | GERENCIAR ATIVIDADES DOS EVENTOS
    0 | SAIR""")
        
        #escolha do crud
        escolha_crud = input('Escolha uma opção: ')
        #condição de saída
        if escolha_crud == '0':
            print("Encerrando programa...")
        #recebe, pesquisa a opção e armazena
        opcao_crud = crud.get(escolha_crud)
        #executa se achou, se não, retorna inválido
        if opcao_crud:
            opcao_crud() 
        else:
            print('Opção inválida, tente novamente.')

        
        
        

if __name__ == "__main__":
    menu_principal()
