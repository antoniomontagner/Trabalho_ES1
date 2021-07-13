
from receita import Receita
from user import User
from user import Admin
from bd import BD
from interface import parametros
import interface
import pesquisa

def menu_cadastro(data):
    user_atual = 0
    while user_atual == 0 :
        comand = menu_comando()
        if comand == "A":
            login,senha,email = login_senha_email()
            if len(email) >= 1:
                aux = ""
                for i in data.lista_users:
                    if i.email == email:
                        aux = "S"
                if aux == "S":
                    print("Usuário já existente. ")
                else:
                    lista_receitas = []                        #CRIAR UMA NOVA LISTA PARA CADA USUARIO NOVO
                    x = User(login,senha,email,lista_receitas) 
                    data.lista_users.append(x)
            else:
                lista_receitas = []            #SE FOR O PRIMEIRO CADASTRO NAO ENTRA NO FOR PARA VERIFICAR O NOME
                x = User(login,senha,email,lista_receitas)  
                data.lista_users.append(x)
                     
            print("-="*30)
        

        elif comand == "B":
            email,senha = email_senha()
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
            if data.lista_users:
                    for i in data.lista_users:
                        if i.email == email and i.senha == senha:
                            user_atual = i.login
            else:
                print("Senha ou email incorretos")

        elif comand == "C":
            return 'exit'
            break
                
        else:
            pass

    return user_atual


## TODO: 
# A -> menu criar receitas (baseado nos comentados lá embaixo)      pronto
# B -> menu de pesquisa
# C -> menu de acesso às receitas, criando um novo menu no C, podendo ver as receitas e alterá-las/excluí-las
# D -> menu de acesso à conta do usuário, podendo acessar seus dados, podendo excluir conta e alterar dados(senha, login, email).

def menu_user(user_atual, j, data):
    print(f'Bem vindo, {user_atual}!')
    
    while user_atual == j.login:
        comand = menu_comando_user()
        if comand == 'A':
            #lista = [] 
            nome,palavras_chave,doce_salgado,gluten,porcoes,n_ingredientes, descricao, modo_preparo =parametros()     #funcao valores
            if len(j.lista_receitas) >= 1:
                aux = ""
                print(j.lista_receitas)
                for receita in j.lista_receitas:
                    print(receita)
                    if receita.nome == nome:
                        aux = "S"
                if aux == "S":
                    print("\n ~~ Nome já existente ~~ ")
                else:
                    ingre = interface.lista_ingredientes(n_ingredientes)           #funcao que retorna uma lista dos ingredientes que vai usar
                    food = Receita(nome,user_atual,palavras_chave,doce_salgado,gluten,porcoes,ingre, descricao, modo_preparo)
                    #lista.append(food)
                    j.lista_receitas.append(food)
            else:
                ingre = interface.lista_ingredientes(n_ingredientes)
                food = Receita(nome,user_atual,palavras_chave,doce_salgado,gluten,porcoes,ingre, descricao, modo_preparo)
                j.lista_receitas.append(food)
                print


        elif comand == "B":
            pesquisa.pesquisar_receita(data)

        elif comand == "C":
                print("-="*30)
                if len(j.lista_receitas) >= 1:
                    print(f""" 
                        {'-'*30}
                        Minhas Receitas:
                        
                        """)
                    for receita in j.lista_receitas:
                        print(f""" 
                        Nome: {receita.nome}       Descricao: {receita.descricao}

                        """)

        elif comand == "D":
            print("-="*30)
            if len(j.lista_receitas) >= 1:
                nome = input("Nome da Receita: ")
                for receita in j.lista_receitas:
                    if receita.nome == nome :
                        interface.retornar_receita(receita)
            else:
                print("Não há dados.")

        #login senha, email, alterar e excluir
        elif comand == "E":
            while True:
                alteracao = menu_alteracao(j)
                if alteracao == '1':
                    login,senha,novo_nome = login_senha_novo_nome()
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                usuarios.login = novo_nome
                
                elif alteracao == '2':
                    login,senha,novo_senha = login_senha_novo_nome()
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                usuarios.senha = novo_senha   
                
                elif alteracao == '3':
                    login,senha,novo_email = login_senha_novo_nome() 
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                usuarios.email = novo_email   
                
                elif alteracao == '4':

                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                data.lista_users.remove(usuarios)
                                user_atual = 0          # excluiu a conta entao sai     # quando deleta o user nao sai da conta mas deleta as coisas
                                break
                elif alteracao == '0':
                    break
                else:
                    print(" Comando inválido. ")    

        elif comand == "F":
            user_atual = 0

        else:
            print(" Comando inválido. ")


def menu_admin(user_atual, i, data):
    while user_atual == i.login:
        comand = menu_comando_admin()
        if comand == "A":
            aux_user = 1
            aux_adm = 1
            for usuario in data.lista_users:
                print("USERS -="*30)
                print(f'Usuario {aux_user}, Login : {usuario.login}, Email : {usuario.email}, Senha : {usuario.senha}')
                aux_user += 1
            for admin in data.lista_admin:
                print("ADMIN -="*30)
                print(f'Admin {aux_adm}, Login : {admin.login}, Email : {admin.email}, Senha : {admin.senha}, Pin : {admin.senha_admin}')
                print("-="*30)
                aux_adm += 1

            alteracao = menu_alteracao_admin()
            if alteracao == 'A':
                login = input(" Email do usuário: ")
                for usuario_pesquisa in data.lista_users:
                    if login == usuario_pesquisa.login:
                        data.lista_users.pop(usuario_pesquisa)
            elif alteracao == 'B':
                print("Alterar dados de uma conta.")
            elif alteracao == 'C':
                print("Adicionar uma conta admnistrativa.")
            elif alteracao == 'D':
                print("Sair")
            else:
                pass

        elif comand == "B":
            print("-="*30)
            print('Pesquisa de Receitas')
            print("-="*30)
            login = input(" Email do usuário: ")
            for usuario_pesquisa in data.lista_users:
                if login == usuario_pesquisa.login:
                    print(f"Login : {usuario_pesquisa.login}, Email : {usuario_pesquisa.email}, Senha : {usuario_pesquisa.senha}")

        elif comand == "C":
            print("-="*30)
            print('Denuncias Recebidas: ')
            pesquisa.acessar_denuncias(data.lista_denuncia, data.lista_users)    # denuncias nao esta funcionando direito
            print("-="*30)

        elif comand == "D":
            user_atual = 0

        else:
            print(" Comando inválido. ")


## interface usadas no sistema

def login_senha_novo_nome():
    login = input(" Email de acesso: ")
    senha = input(" Senha de acesso: ")
    novo_nome = input(" Digite o novo parametro: ")
    return login,senha, novo_nome

def login_senha_email():
    print("-="*30)
    login = input("Login: ")
    senha = input("Senha: ")
    email = input("Email: ")
    return login,senha,email

def email_senha():
    print("-="*30)
    email = input("Email: ")
    senha = input("Senha: ")
    print("-="*30)
    return email,senha

def menu_alteracao(j):
    print(f"""
    {'-'*30}
        Nome:   {j.login}
        Email:  {j.email}
    {'-'*30}
    """)
    alteracao = input("""
        1 - Alterar nome
        2 - Alterar senha
        3 - Alterar email
        4 - Excluir conta

        0 - Sair
    """)
    return alteracao

def menu_comando():
    comand = input(f"""
    Sistema de Cadastro:
        A - Cadastrar usuario
        B - Acessar conta
        C - Sair
    {"-="*30}
    Resposta: """).upper()
    return comand


def menu_comando_user():
    comand = input(f"""
{"##"*30}    
    A - Criar Receita
    B - Pesquisa
    C - Minhas Receitas
    D - Pesquisar uma receita própria
    E - Minha Conta 
    
    F - Sair
{"-="*30}
Resposta: """).upper()
    return comand

def menu_comando_admin():
    comand = input(f"""
        Sistema da Administracao:
            A - Todas as Contas
            B - Pesquisa
            C - Denuncias
            D - Sair
        {"-="*30}
        Resposta: """).upper()
    return comand


def menu_alteracao_admin():
    print('\n  Deseja fazer alguma alteracao?'  )
    comand = input(f"""
                A - Excluir uma conta.
                B - Alterar dados de uma conta.
                C - Adicionar uma conta admnistrativa.
                D - Nao, sair.
                {"-="*30}
                Resposta: """).upper()  
    return comand