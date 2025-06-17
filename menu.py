import cruds.Crud_eventos as eventos
import cruds.Crud_participantes as participantes
import cruds.Crud_atividades as atividades
from colorama import Fore as fr

def menu_crud(nome, mod,cor):
    
    funcao_crud ={
        '1' : lambda : mod.criar(),
        '2' : lambda : mod.listar(),
        '3' : lambda : mod.atualizar(),
        '4' : lambda : mod.deletar(),
        '5' : lambda : mod.pesquisar()
    }
    while True:
        print(f"""
      {cor}{'-'*10} MENU {nome} {'-'*10}
    1 | CRIAR
    2 | LISTAR
    3 | ATUALIZAR
    4 | DELETAR
    5 | PESQUISAR
    0 | VOLTAR""")
        
        
        escolha_funcao = input("Opção: ")
     
        if escolha_funcao == '0':
            print("Retornando...")
            break
        opcao_funcao = funcao_crud.get(escolha_funcao)
        
        if opcao_funcao:
            opcao_funcao()
        else:
            print(fr.RED + "Opção inválida, tente novamente!"+fr.RESET)
        

def menu_principal():
  
    crud = {
        '1': lambda: menu_crud("EVENTOS", eventos,fr.BLUE),
        '2' : lambda: menu_crud("PARTICIPANTES", participantes,fr.YELLOW),
        '3' : lambda: menu_crud("ATIVIDADES",atividades,fr.CYAN),
        '0' : exit
    }
    while True:
        print(f"""
    {fr.RESET}{'-'*10} MENU GESTÃO DE EVENTOS {'-'*10}
    {fr.BLUE} 1 | GERENCIAR EVENTOS
    {fr.YELLOW} 2 | GERENCIAR PARTICIPANTES
    {fr.CYAN} 3 | GERENCIAR ATIVIDADES DOS EVENTOS
    {fr.MAGENTA} 0 | SAIR"""+fr.RESET)
        

        escolha_crud = input('Escolha uma opção: ')
 
        if escolha_crud == '0':
            print(fr.MAGENTA+"Encerrando programa...")
        opcao_crud = crud.get(escolha_crud)
        if opcao_crud:
            opcao_crud() 
        else:
            print(fr.RED + "Opção inválida, tente novamente."+ fr.RESET)


if __name__ == "__main__":
    menu_principal()