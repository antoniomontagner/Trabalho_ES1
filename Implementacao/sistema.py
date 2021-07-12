from receita import Bolo
from receita import Comida
from user import User
from user import Admin
from bd import BD
from defs import parametros
from defs import tabela
from defs import nomequant

def menu_cadastro(data):
    user_atual = 0
    while user_atual == 0 :
        comand = input(f"""
Sistema de Cadastro:
    A - Cadastrar usuario
    B - Acessar conta
    C - Sair
{"-="*30}
Resposta: """).upper()

        if comand == "A":
            print("-="*30)
            login = input("Login: ")
            senha = input("Senha: ")
            email = input("Email: ")

            if len(email) >= 1:
                a = ""
                for i in data.lista_users:
                    if i.email == email:
                        a = "S"
                if a == "S":
                    print("Usuário já existente. ")
                else:
                    L = []                        #CRIAR UMA NOVA LISTA PARA CADA USUARIO NOVO
                    x = User(login,senha,email,(L,0)) 
                    data.lista_users.append(x)
            else:
                L = []            #SE FOR O PRIMEIRO CADASTRO NAO ENTRA NO FOR PARA VERIFICAR O NOME
                x = User(login,senha,email,(L,0))  
                data.lista_users.append(x)
                     
            print("-="*30)
        

        elif comand == "B":
            print("-="*30)
            email = input("Email: ")
            senha = input("Senha: ")
            print("-="*30)

            if len (email) >= 1:
                for i in data.lista_admin:
                    if i.email == email and i.senha == senha:
                        print("Bem vindo, administrador. Por segurança do sistema, favor insira seu pin de administração para prosseguir.")
                        pin = input("Pin: ")
                        if i.senha_admin == pin:
                            user_atual = i.login
                        else:
                            print("Pin incorreto")
                            break
                for i in data.lista_users:
                    if i.email == email and i.senha == senha:
                        user_atual = i.login
                    else:
                        print("Senha ou email incorretos")
            else:
                print("Senha ou email inválidos")

        elif comand == "C":
            return 'exit'
            break
                
        else:
            pass

    return user_atual

def menu_user(user_atual, j, data):
    print(f'\nBem vindo, {user_atual}!')
    while user_atual == j.login:
        comand = input(f"""
Sistema da Administracao:
    A - Criar Receita
    B - Pesquisa
    C - Minhas Receitas
    D - Minha Conta 
    E - Sair
{"-="*30}
Resposta: """).upper()

        if comand == "A":
                print("-="*30)
                print(f'Criar Receita')
                print("-="*30)


        elif comand == "B":
                print("-="*30)
                print(f'Pesquisa')
                print("-="*30)


        elif comand == "C":
                print("-="*30)
                print(f'Minhas Receitas: ')
                print("-="*30)

        elif comand == "D":
                print("-="*30)
                print(f'Minha Contas: ')
                print("-="*30)

        elif comand == "E":
                user_atual = 0
        else:
            pass


def menu_admin(user_atual, i, data):

    while user_atual == i.login:
        comand = input(f"""
Sistema da Administracao:
    A - Todas as Contas
    B - Pesquisa
    C - Denuncias
    D - Sair
{"-="*30}
Resposta: """).upper()
        
        if comand == "A":
            for j in data.lista_users:
                print(j)


        elif comand == "B":
            print("-="*30)
            print(f'Pesquisa de Receitas')
            print("-="*30)


        elif comand == "C":
            print("-="*30)
            print(f'Denuncias Recebidas: ')
            print("-="*30)


        elif comand == "D":
            user_atual = 0

        else:
            pass