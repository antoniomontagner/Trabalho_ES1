from defs import lista_ingredientes
from receita import Receita
from user import User
from user import Admin
from bd import BD
from interface import email_senha, parametros
import interface
import pesquisa


def menu_cadastro(data):
    user_atual = 0
    while user_atual == 0:
        comand = interface.menu_comando()
        if comand == "A":
            login, senha, email = interface.login_senha_email()
            if len(data.lista_users) >= 1:
                nome_existe = ""
                for user in data.lista_users:
                    if user.email == email:
                        nome_existe = "S"
                if nome_existe == "S":
                    interface.retorno_print("Usuário já existente. ")
                else:
                    lista_receitas = []  # CRIAR UMA NOVA LISTA PARA CADA USUARIO NOVO
                    x = User(login, senha, email, lista_receitas)
                    data.lista_users.append(x)
            else:
                lista_receitas = []  # SE FOR O PRIMEIRO CADASTRO NAO ENTRA NO FOR PARA VERIFICAR O NOME
                x = User(login, senha, email, lista_receitas)
                data.lista_users.append(x)

            interface.retorno_print("-="*30)

        elif comand == "B":
            email, senha = interface.email_senha()
            admin = False
            if len(email) >= 1:
                erro_pin = 0
                for i in data.lista_admin:
                    if i.email == email and i.senha == senha:
                        pin = interface.menu_input_pin()
                        admin = True
                        if i.senha_admin == pin:
                            user_atual = i.login
                        else:
                            interface.invalid_input()
                            erro_pin = 1
                if admin == False:
                    found = ''
                    for i in data.lista_users:
                        if found == '':
                            if i.email == email and i.senha == senha:
                                user_atual = i.login
                                found = 'S'
                            else:
                                user_atual = 0
                    if user_atual == 0 and erro_pin == 0:
                        interface.retorno_print("Senha ou email incorretos")

        elif comand == "C":
            return 'exit'
            break

        else:
            pass

    return user_atual


def menu_user(user_atual, j, data):
    interface.retorno_print(f'Bem vindo, {user_atual}!')

    while user_atual == j.login:
        comand = interface.interface_menu_user()

        if comand == "A":
            #lista = []
            nome, palavras_chave, doce_salgado, gluten, porcoes, lista_ingredientes, descricao, modo_preparo = parametros()  # funcao valores
            # print(j.lista_receitas)
            if len(j.lista_receitas) >= 1:
                aux = ""
                for receita in j.lista_receitas:
                    if receita.nome == nome:
                        aux = "S"
                if aux == "S":
                    interface.retorno_print(
                        "\n ~~ Nome já existente, cadastre novamente.  ~~ \n")
                else:
                    food = Receita(nome, user_atual, palavras_chave, doce_salgado, porcoes, gluten, lista_ingredientes, descricao, modo_preparo)
                    j.lista_receitas.append(food)
            else:
                food = Receita(nome, user_atual, palavras_chave, doce_salgado, porcoes, gluten, lista_ingredientes, descricao, modo_preparo)
                j.lista_receitas.append(food)
            
        elif comand == "B":
            pesquisa.pesquisar_receita(data)

        elif comand == "C":
            interface.retorno_print("-="*30)
            cont = 1
            if len(j.lista_receitas) >= 1:
                for receita in j.lista_receitas:
                    interface.retornar_lista_receitas(cont, receita)
                    cont += 1
                alterar = interface.deseja_alterar_receita()
                if alterar == '1':
                    rec_escolhida = interface.alterar_receita_escolhida()
                    if (rec_escolhida) <= len(j.lista_receitas):
                        i = rec_escolhida - 1
                        rec_escolhida = j.lista_receitas[i]
                        interface.retorno_print(rec_escolhida) # rec_escolhida é um objeto 

                        # alterar dados da receita ##########################

                    else:
                        interface.retorno_print("Inválido. ")
                else:
                    pass
            else:
                interface.retorno_print(
                    "O usuário ainda não possui receitas cadastradas. ")

        # login senha, email, alterar e excluir
        elif comand == "D":
            alterar_dados = True
            while alterar_dados:
                alteracao = interface.menu_alteracao(j)
                if alteracao == '1':
                    login, senha, novo_nome = interface.login_senha_novo_nome()
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                usuarios.login = novo_nome
                            else:
                                interface.retorno_print(" Senha inválida.")
                        else:
                            interface.retorno_print(" Email inválido.")

                elif alteracao == '2':
                    login, senha, novo_senha = interface.login_senha_novo_nome()
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                usuarios.senha = novo_senha
                            else:
                                interface.retorno_print(" Senha inválida.")
                        else:
                            interface.retorno_print(" Email inválido.")

                elif alteracao == '3':
                    login, senha, novo_email = interface.login_senha_novo_nome()
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                usuarios.email = novo_email
                            else:
                                interface.retorno_print(" Senha inválida.")
                        else:
                            interface.retorno_print(" Email inválido.")

                elif alteracao == '4':
                    login, senha = interface.email_senha()
                    for usuarios in data.lista_users:
                        if login == usuarios.email:
                            if senha == usuarios.senha:
                                data.lista_users.remove(usuarios)
                                # excluiu a conta entao sai     # quando deleta o user nao sai da conta mas deleta as coisas
                                user_atual = 0
                                break
                            else:
                                interface.retorno_print(" Senha inválida.")
                        else:
                            interface.retorno_print(" Email inválido.")

                elif alteracao == '0':
                    alterar_dados = False
                else:
                    interface.invalid_input()

        elif comand == "E":
            user_atual = 0

        else:
            interface.invalid_input()


def menu_admin(user_atual, i, data):
    while user_atual == i.login:
        comand = interface.menu_comando_admin()  # interface grafica
        if comand == "A":
            aux_user = 1
            aux_adm = 1
            for usuario in data.lista_users:
                interface.menu_lista_user(
                    aux_user, usuario)  # interface grafica
                aux_user += 1
            for admin in data.lista_admin:
                interface.menu_lista_admin(aux_adm, admin)  # interface grafica
                aux_adm += 1

            alteracao = interface.menu_alteracao_admin()
            if alteracao == 'A':
                login = interface.email_usuario()
                for usuario_pesquisa in data.lista_users:
                    if login == usuario_pesquisa.login:
                        data.lista_users.pop(usuario_pesquisa)

            elif alteracao == 'B':
                interface.retorno_print("Alterar dados de uma conta.")

                alterar_dados = True
                while alterar_dados:
                    alteracao = interface.menu_alterar_dados_user()
                    if alteracao == '1':
                        login, senha, novo_nome = interface.login_senha_novo_nome()
                        for usuarios in data.lista_users:
                            if login == usuarios.email:
                                if senha == usuarios.senha:
                                    usuarios.login = novo_nome
                                else:
                                    interface.retorno_print(" Senha inválida.")
                            else:
                                interface.retorno_print(" Email inválido.")

                    elif alteracao == '2':
                        login, senha, novo_senha = interface.login_senha_novo_nome()
                        for usuarios in data.lista_users:
                            if login == usuarios.email:
                                if senha == usuarios.senha:
                                    usuarios.senha = novo_senha
                                else:
                                    interface.retorno_print(" Senha inválida.")
                            else:
                                interface.retorno_print(" Email inválido.")

                    elif alteracao == '3':
                        login, senha, novo_email = interface.login_senha_novo_nome()
                        for usuarios in data.lista_users:
                            if login == usuarios.email:
                                if senha == usuarios.senha:
                                    usuarios.email = novo_email
                                else:
                                    interface.retorno_print(" Senha inválida.")
                            else:
                                interface.retorno_print(" Email inválido.")

                    elif alteracao == '4':
                        login, senha = interface.email_senha()
                        for usuarios in data.lista_users:
                            if login == usuarios.email:
                                if senha == usuarios.senha:
                                    data.lista_users.remove(usuarios)
                                    # excluiu a conta entao sai     # quando deleta o user nao sai da conta mas deleta as coisas
                                    user_atual = 0
                                    break
                                else:
                                    interface.retorno_print(" Senha inválida.")
                            else:
                                interface.retorno_print(" Email inválido.")

                    elif alteracao == '0':
                        alterar_dados = False
                    else:
                        interface.invalid_input()

            elif alteracao == 'C':
                interface.retorno_print("Adicionar uma conta admnistrativa.")
            elif alteracao == 'D':
                interface.retorno_print("Sair")
            else:
                pass

        elif comand == "B":
            interface.retorno_print(f"""
        {'-=' *30}
                Pesquisa de Receitas
        {'-='*30}""")
            login = interface.email_usuario()
            for usuario_pesquisa in data.lista_users:
                if login == usuario_pesquisa.login:
                    interface.retorno_print(
                        f"Login : {usuario_pesquisa.login}, Email : {usuario_pesquisa.email}, Senha : {usuario_pesquisa.senha}")

        elif comand == "C":
            interface.retorno_print(f"""
    { '-='*30}
            Denuncias Recebidas: """)

            # denuncias nao esta funcionando direito
            pesquisa.acessar_denuncias(data.lista_denuncia, data.lista_users)
            interface.retorno_print("-="*30)

        elif comand == "D":
            user_atual = 0

        else:
            interface.invalid_input()
