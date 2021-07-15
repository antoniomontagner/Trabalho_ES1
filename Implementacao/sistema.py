
from receita import Receita
from user import User
from user import Admin
from bd import BD
from defs import parametros
import defs
import pesquisa

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
            print("-="*30)
            email = input("Email: ")
            senha = input("Senha: ")
            print("-="*30)

            if len (email) >= 1:
                erro_pin = 0
                for i in data.lista_admin:
                    if i.email == email and i.senha == senha:
                        print("Bem vindo, administrador. Por segurança do sistema, favor insira seu pin de administração para prosseguir.")
                        pin = input("Pin: ")
                        if i.senha_admin == pin:
                            user_atual = i.login
                        else:
                            print("Pin incorreto")
                            erro_pin = 1
                            break
                    else:
                        user_atual = 0

                for i in data.lista_users:
                    if i.email == email and i.senha == senha:
                        user_atual = i.login
                    else:
                        user_atual = 0
                if user_atual == 0 and erro_pin == 0:
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
        comand = input(f"""{"##"*30}    
    A - Criar Receita
    B - Pesquisa
    C - Minhas Receitas
    D - Pesquisar uma receita própria
    E - Minha Conta 
    
    F - Sair
{"-="*30}
Resposta: """).upper()

        if comand == "A":
            print(f"""
{"-="*30}
   ################
   # Nova Receita #
   ################
{"-="*30}
        """)
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
                    ingre = defs.lista_ingredientes(n_ingredientes)           #funcao que retorna uma lista dos ingredientes que vai usar
                    food = Receita(nome,user_atual,palavras_chave,doce_salgado,gluten,porcoes,ingre, descricao, modo_preparo)
                    #lista.append(food)
                    j.lista_receitas.append(food)
            # else:
            #     ingre = defs.lista_ingredientes(n_ingredientes)
            #     food = Receita(nome,user_atual,palavras_chave,doce_salgado,gluten,porcoes,ingre, descricao, modo_preparo)
            #     j.lista_receitas.append(food)
            #     print


        elif comand == "B":
            pesquisa.pesquisar_receita(data)

        elif comand == "C":
                print("-="*30)
                i = 1
                if len(j.lista_receitas) >= 1:
                    print(f""" 
                        {'-'*30}
                        Minhas Receitas:
                        """)
                    for receita in j.lista_receitas:
                        print(f"""################\n# RECEITA {i} #\n################\n\nNome: {receita.nome} \n\nIngredientes: {receita.lista_ingredientes} \n\nModo de preparo: {receita.modo_preparo} \n\nDescricao: {receita.descricao} \n\nPalavras Chave: {receita.palavras_chave}
                            """)
                        i += 1
                    alterar = input(f'Deseja alterar alguma receita? \n1 - sim, 2 - não')
                    if alterar == 1:
                        receita = ('Qual receita deseja alterar? Insira o número referente à pesquisa.')
                    else:
                        pass
                else:
                    print("O usuário ainda não possui receitas cadastradas. ")

        #login senha, email, alterar e excluir
        elif comand == "E":
            while True:
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
                if alteracao == '1':
                    login = input(" Email de acesso: ")
                    senha = input(" Senha de acesso: ")
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                novo_nome = input(" Novo nome: ")
                                usuarios.login = novo_nome
                
                elif alteracao == '2':
                    login = input(" Email de acesso: ")
                    senha = input(" Senha de acesso: ")
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                novo_senha = input(" Nova senha: ")
                                usuarios.senha = novo_senha   
                
                elif alteracao == '3':
                    login = input(" Email de acesso: ")
                    senha = input(" Senha de acesso: ")
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                novo_email = input(" Novo email: ")
                                usuarios.email = novo_email   
                
                elif alteracao == '4':
                    login = input(" Email de acesso: ")
                    senha = input(" Senha de acesso: ")
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

## TODO: 
# A -> menu de acesso aos dados de todos os usuários (login, senha e email), podendo excluir contas
# B -> menu de pesquisa igual ao de clientes
# C -> menu de denuncias (feito, só falta organizar)

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
            aux_user = 1
            aux_adm = 1
            print('\n#######################\n# Usuarios do Sistema #\n#######################')
            for usuario in data.lista_users:
                print("-="*30)
                print(f'Usuario {aux_user}, Login : {usuario.login}, Email : {usuario.email}, Senha : {usuario.senha}')
                print("-="*30)
                aux_user += 1
            print('\n###################\n# Administradores #\n###################')
            for admin in data.lista_admin:
                # print("-="*30)
                print(f'Admin {aux_adm}, Login : {admin.login}, Email : {admin.email}, Senha : {admin.senha}, Pin : {admin.senha_admin}')
                print("-="*30)
                aux_adm += 1
            print('\n  Deseja fazer alguma alteracao?'  )
            alteracao = input(f"""
                A - Excluir uma conta.
                B - Alterar dados de uma conta.
                C - Adicionar uma conta admnistrativa.
                D - Nao, sair.
                {"-="*30}
                Resposta: """).upper()  
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

