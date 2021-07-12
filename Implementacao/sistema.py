from receita import Receita
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

def menu_user(user_atual, j, data):
    print(f'\nBem vindo, {user_atual}!')
    while user_atual == j.login:
        comand = input(f"""
    A - Criar Receita
    B - Pesquisa
    C - Minhas Receitas
    D - Minha Conta 
    E - Sair
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
            j.lista_receitas.append()
            # nome,palavras_chave,doce_salgado,star,hot_cold,porc,nomequant =parametros()     #funcao valores
            # if len(lista) >= 1:
            #     a = ""
            #     for i in range(len(lista)):
            #         if lista[i].nome == q:
            #             a = "S"
            #     if a == "S":
            #         print()
            #         print(" ~~ Nome já existente ~~ ")
            #     else:
            #         ingre = nomequant(u)           #funcao que retorna uma lista dos ingredientes que vai usar
            #         food = Comida(nome,palavras_chave,doce_salgado,star,hot_cold,porc,nomequant,ingre)
            #         lista.append(food)

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


# def menu_receita(lst,y): 
#                                                                 #herança uso a classe bolo que recebe a classe comida
#     # l = lst
#     # lista = l[:]      #caso o usuario ja tenha receitas
#     # if y == 0:        # y é o numero de acessos que o usuario fez, para adicionar o Bolo apenas uma vez nao importa a quantidade de logins
#     #     lista.append(Bolo("Bolo","A","B","A","B","B",[{0: ('ovo', '3 unidades')}, {1: ('farinha', '1kg')}, {2: ('leite', '500ml')}, {3: ('fermento', '1 colher se sopa')}],"padrao"))

#     while True:
#         comando = input(f"""
# {"-="*30}
#    ############
#    # Receitas #
#    ############
#         A: Cadastro
#         B: Cadastrar Bolo  
#         C: Consultar dados 
#         D: Alterar dados 
#         E: Mostrar menu de receitas      
#         F: Excluir item
#         G: Sair
# {"-="*30}
#         Resposta: """).upper()

#         if comando == "A":
#             print("-="*30)
#             nome,palavras_chave,doce_salgado,star,hot_cold,porc,nomequant =parametros()     #funcao valores
#             if len(lista) >= 1:
#                 a = ""
#                 for i in range(len(lista)):
#                     if lista[i].nome == q:
#                         a = "S"
#                 if a == "S":
#                     print()
#                     print(" ~~ Nome já existente ~~ ")
#                 else:
#                     ingre = nomequant(u)           #funcao que retorna uma lista dos ingredientes que vai usar
#                     food = Comida(nome,palavras_chave,doce_salgado,star,hot_cold,porc,nomequant,ingre)
#                     lista.append(food)
            
#         elif comando == "B":
#             print("-="*30)
#             nome,palavras_chave,doce_salgado,star,hot_cold,porc,nomequant =parametros()    #funcao valores
#             if len(lista) >= 1:
#                 a = ""
#                 for i in range(len(lista)):
#                     if lista[i].nome == q:
#                         a = "S"
#                 if a == "S":
#                     print()
#                     print(" ~~ Nome já existente ~~ ")
#                 else:
#                     ingre = nomequant(u)           
#                     food = Bolo(q,w,e,r,t,y,ingre,"padrao")
#                     lista.append(food)

#         elif comando == "C":
#             print("-="*30)
#             if len(lista) >= 1:
#                 nome = input("Nome do alimento: ")
#                 for i in lista:
#                     if nome == "Bolo":
#                         if i.nome == nome and i.r_padrao == "padrao":
#                             x = i.printar()          #uso de polimorfismo   pois objeto Bolo e Comida tem o mesmo metodo   (printar)
#                             a = i.retorno()       # metodo que retorna os valorem em forma de lista
#                             print(f"""
#                             Nome da receita: {a[0]}
#                                             {x}
#                                                                       Legenda:
#                                                 {"#"*53}
#                                 Tipo: {a[1]}        |  {"A- Doce":<23} /  {"B- Salgado":<23}|
#                                 Tipo: {a[2]}        |  {"A- Até 3 estrelas":<23} /  {"B- Mais de 3 estrelas":<23}|
#                                 Tipo: {a[3]}        |  {"A- Quente":<23} /  {"B- Frio":<23}|
#                                 Tipo: {a[4]}        |  {"A- Menos de 30 minutos":<23} /  {"B- Mais de 30 minutos":<23}|
#                                 Tipo: {a[5]}        |  {"A- Ate de 2 pessoas":<23} /  {"B- Mais de 2 pessoas":<23}|
#                                                 {"#"*53}
#                                     Numero de ingredientes: {len(a[6])} 
#                                             Ingredientes: """)
#                             for k in range(len(a[6])):
#                                 print(f"""          {"Nome:":>48} {i.nomequant[k][k][0]:<15}{" ":8}quantidade: {i.nomequant[k][k][1]}""")
#                     else:
#                         if i.nome == nome :
#                             a = i.retorno()
#                             x = i.printar()
#                             print(f"""
#                             Nome da receita: {a[0]}
#                                                                       Legenda:
#                                                 {"#"*53}
#                                 Tipo: {a[1]}        |  {"A- Doce":<23} /  {"B- Salgado":<23}|
#                                 Tipo: {a[2]}        |  {"A- Até 3 estrelas":<23} /  {"B- Mais de 3 estrelas":<23}|
#                                 Tipo: {a[3]}        |  {"A- Quente":<23} /  {"B- Frio":<23}|
#                                 Tipo: {a[4]}        |  {"A- Menos de 30 minutos":<23} /  {"B- Mais de 30 minutos":<23}|
#                                 Tipo: {a[5]}        |  {"A- Ate de 2 pessoas":<23} /  {"B- Mais de 2 pessoas":<23}|
#                                                 {"#"*53}
#                                     Numero de ingredientes: {len(a[6])} 
#                                             Ingredientes: """)
#                             for k in range(len(a[6])):
#                                 print(f"""          {"Nome:":>48} {i.nomequant[k][k][0]:<15}{" ":8}quantidade: {i.nomequant[k][k][1]}""")
#             else:
#                 print("Não há dados.")


#         elif comando == "D":
#             print("-="*30)
#             nome = input("Nome do alimento: ")
#             if len(lista) >= 1:
#                 for i in lista:
#                     if i.nome == nome:
#                         q,w,e,r,t,y,u = parametros()
#                         ingre = nomequant(u)
#                         lista.remove(i)
#                         food = Comida(q,w,e,r,t,y,ingre)
#                         lista.append(food)
#             else:
#                 print("Não há elementos.")


#         elif comando == "E":
#             if len(lista) >= 1:
#                 tabela(lista)
#             else:
#                 print("Não há elementos.")


#         elif comando == "F":
#             if len(lista) >= 1:
#                 deletar = input("Elemento que deseja excluir: ")
#                 for i in lista:
#                     if i.nome == deletar:
#                         lista.remove(i)
#                         print("Item excluído.")
#             else:
#                 print("Não há elementos.")


#         elif comando == "G":
#             break
        
#         else:
#             pass
#     return lista

