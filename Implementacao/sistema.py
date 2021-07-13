
from receita import Receita
from user import User
from user import Admin
from bd import BD
from defs import parametros
import defs

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
                        print('b')
                        if i.email == email and i.senha == senha:
                            print('c')
                            user_atual = i.login
                        else:
                            print("Senha ou email incorretos")
                else:
                            print("Usuario não cadastrado")
            else:
                print("Senha ou email inválidos")

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
    print(f'\nBem vindo, {user_atual}!')
    
    while user_atual == j.login:
        comand = input(f"""
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
            nome,palavras_chave,doce_salgado,gluten,porcoes,n_ingredientes, descricao =parametros()     #funcao valores
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
                    food = Receita(nome,palavras_chave,doce_salgado,gluten,porcoes,ingre, descricao)
                    #lista.append(food)
                    j.lista_receitas.append(food)
            else:
                ingre = defs.lista_ingredientes(n_ingredientes)
                food = Receita(nome,palavras_chave,doce_salgado,gluten,porcoes,ingre, descricao)
                j.lista_receitas.append(food)
                print


        elif comand == "B":
            pesquisa = input(f"""
{"-="*30}
   ######################
   # Pesquisar Receitas #
   ######################
{"-="*30}
    O que iremos cozinhar hoje? 
    \n    """).upper()
            data.lista_total = []   #lista de todas as receitas
            for i in data.lista_users:
                lista_total.append(i.lista_receitas)
            for receita in lista_total:
                if pesquisa == receita.palavras_chave:
                    print(receita.retorno())
                else:
                    for ingrediente in receita.lista_ingredientes:
                        if pesquisa == ingrediente.keys():
                            print(receita.retorno())
                        else:
                            print("0 receitas encontradas.")

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
                        nome, doce_salgado, avaliacoes, gluten, porcoes, lista_ingredientes, descricao =  receita.retorno()
                        print(f"""
                        Nome da receita: {nome}
                                                                    Legenda:
                                            {"#"*53}
                            Tipo: {doce_salgado}        |  {"A- Doce":<23} /  {"B- Salgado":<23}|
                            Tipo: {avaliacoes}        |  {"A- Até 3 estrelas":<23} /  {"B- Mais de 3 estrelas":<23}|
                            Tipo: {gluten}        |  {"A- Com gluten":<23} /  {"B- Sem gluten":<23}|
                            Tipo: {porcoes}        |  {"A- Ate de 2 pessoas":<23} /  {"B- Mais de 2 pessoas":<23}|
                                            {"#"*53}
                                Numero de ingredientes: {len(lista_ingredientes)} 
                                        Ingredientes: """)
                        for k in lista_ingredientes:
                            for c,v in k.items():                            
                                print(f"""          {"Nome:":>48} {c:<15}{" ":8}quantidade: {v}""")
            else:
                print("Não há dados.")

        #login senha, email, alterar e excluir
        elif comand == "E":
            while True:
                print(f"""
                {'-'*30}
                    Nome:   {j.nome}
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
                        if login == usuarios.login:
                            if senha == usuarios.senha:
                                novo_nome = input(" Novo nome: ")
                                usuarios.nome = novo_nome
                
                elif alteracao == '2':
                    login = input(" Email de acesso: ")
                    senha = input(" Senha de acesso: ")
                    for usuarios in data.lista_users:
                        if login == usuarios.login:
                            if senha == usuarios.senha:
                                novo_senha = input(" Nova senha: ")
                                usuarios.senha = novo_senha   
                
                elif alteracao == '3':
                    login = input(" Email de acesso: ")
                    senha = input(" Senha de acesso: ")
                    for usuarios in data.lista_users:
                        if login == usuarios.login:
                            if senha == usuarios.senha:
                                novo_email = input(" Novo email: ")
                                usuarios.email = novo_email   
                
                elif alteracao == '4':
                    login = input(" Email de acesso: ")
                    senha = input(" Senha de acesso: ")
                    for usuarios in data.lista_users:
                        if login == usuarios.login:
                            if senha == usuarios.senha:
                                data.lista_users.pop(usuarios)
                                user_atual = 0          # excluiu a conta entao sai 

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
            print(f'Pesquisa de Receitas')
            print("-="*30)
            login = input(" Email do usuário: ")
            for usuario_pesquisa in data.lista_users:
                if login == usuario_pesquisa.login:
                    print(f"Login : {usuario_pesquisa.login}, Email : {usuario_pesquisa.email}, Senha : {usuario_pesquisa.senha}")


        elif comand == "C":
            print("-="*30)
            print(f'Denuncias Recebidas: ')
            defs.acessar_denuncias(data.denuncias, data.lista_users)    # denuncias nao esta funcionando direito
            print("-="*30)


        elif comand == "D":
            user_atual = 0

        else:
            print(" Comando inválido. ")

