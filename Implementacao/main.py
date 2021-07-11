from receita import Bolo
from receita import Comida
from user import User
from user import Admin
import bd
from defs import parametros
from defs import tabela
from defs import nomequant

def email_center ():
    email = []             #VAI ARMAZENAR OS DADOS DO USUARIO E PORTANDO SUAS RECEITAS TAMBEM
    while True :
        comand = input(f"""
    Sistema De Cadastro:
        A - Cadastrar usuario
        B - Acessar conta
        C - Alterar dados
        D - Excluir conta
        E - Contas
        F - Sair
{"-="*30}
        Resposta: """).upper()

        if comand == "A":
            print("-="*30)
            login = input("Login: ")
            senha = input("Senha: ")
            email = input("Email: ")

            if len(email) >= 1:
                a = ""
                for i in range(len(email)):
                    if email[i].login == login:
                        a = "S"
                if a == "S":
                    print("Usuário já existente. ")
                else:
                    L = []                        #CRIAR UMA NOVA LISTA PARA CADA USUARIO NOVO
                    x = User(login,senha,email,receita(L,0),0) 
                    bd.new_user(User)       
                    email.append(x)
            else:
                L = []            #SE FOR O PRIMEIRO CADASTRO NAO ENTRA NO FOR PARA VERIFICAR O NOME
                x = User(login,senha,email,receita(L,0),0)  
                bd.new_user(User)     
                email.append(x)
            print("-="*30)
            

        elif comand == "B":
            print("-="*30)
            email = input("Email: ")
            senha = input("Senha: ")
            print("-="*30)

            if len (email) >= 1:
                for i in email:
                    if i.login == login and i.senha == senha:
                        y = i.contar(1)                       #PARA SABER O NUMERO DE ACESSOS QUE O USUARIO JA FEZ( VAI SER USADO NA FUNCAO   "receita")
                        x = receita(i.user_receita,y) #apos criar uma lista de dicionario e atribuir a "x " 
                        i.user_receita = []           
                        i.user_receita = x[:]
            for i in bd.lista_admin:
                if email == bd.lista_admin[i].email
            else:
                print("Sem dados.")
            print("-="*30)


        elif comand == "C":
            print("-="*30)
            login = input("Login: ")
            senha = input("Senha: ")
            print("-="*30)

            if len (email) >= 1:
                for i in email:
                    if i.login == login and i.senha == senha:
                        i.login = input("Novo login: ")
                        i.senha = input("Nova senha: ")
                        print("Dados alterados.")

            else:
                print("Sem dados.")
            print("-="*30)


        elif comand == "D":
            print("-="*30)
            login = input("Login: ")
            senha = input("Senha: ")
            print("-="*30)
            if len (email) >= 1:
                for i in email:
                    if i.login==login and i.senha == senha:
                        email.remove(i)
                        print("Dados excluidos.")

            else:
                print("Sem dados.")
            print("-="*30)


        elif comand == "E":
            print("Contas: ")
            if len(email) >= 1:
                for i in email:
                    c = i.nome_email()     #usar o metodo da classe User que retorna uma STR 
                    print(c)
            else:
                print("         Não há dados.")
            print("-="*30)


        elif comand == "F":
            break
            
        else:
            pass

    return email

def receita(lst,y): 
                                                                #herança uso a classe bolo que recebe a classe comida
    l = lst
    lista = l[:]      #caso o usuario ja tenha receitas
    if y == 0:        # y é o numero de acessos que o usuario fez, para adicionar o Bolo apenas uma vez nao importa a quantidade de logins
        lista.append(Bolo("Bolo","A","B","A","B","B",[{0: ('ovo', '3 unidades')}, {1: ('farinha', '1kg')}, {2: ('leite', '500ml')}, {3: ('fermento', '1 colher se sopa')}],"padrao"))

    while True:
        comando = input(f"""
{"-="*30}
   ############
   # Receitas #
   ############
        A: Cadastro
        B: Cadastrar Bolo  
        C: Consultar dados 
        D: Alterar dados 
        E: Mostrar menu de receitas      
        F: Excluir item
        G: Sair
{"-="*30}
        Resposta: """).upper()

        if comando == "A":
            print("-="*30)
            nome,palavras_chave,doce_salgado,star,hot_cold,porc,nomequant =parametros()     #funcao valores
            if len(lista) >= 1:
                a = ""
                for i in range(len(lista)):
                    if lista[i].nome == q:
                        a = "S"
                if a == "S":
                    print()
                    print(" ~~ Nome já existente ~~ ")
                else:
                    ingre = nomequant(u)           #funcao que retorna uma lista dos ingredientes que vai usar
                    food = Comida(nome,palavras_chave,doce_salgado,star,hot_cold,porc,nomequant,ingre)
                    lista.append(food)
            
        elif comando == "B":
            print("-="*30)
            nome,palavras_chave,doce_salgado,star,hot_cold,porc,nomequant =parametros()    #funcao valores
            if len(lista) >= 1:
                a = ""
                for i in range(len(lista)):
                    if lista[i].nome == q:
                        a = "S"
                if a == "S":
                    print()
                    print(" ~~ Nome já existente ~~ ")
                else:
                    ingre = nomequant(u)           
                    food = Bolo(q,w,e,r,t,y,ingre,"padrao")
                    lista.append(food)

        elif comando == "C":
            print("-="*30)
            if len(lista) >= 1:
                nome = input("Nome do alimento: ")
                for i in lista:
                    if nome == "Bolo":
                        if i.nome == nome and i.r_padrao == "padrao":
                            x = i.printar()          #uso de polimorfismo   pois objeto Bolo e Comida tem o mesmo metodo   (printar)
                            a = i.retorno()       # metodo que retorna os valorem em forma de lista
                            print(f"""
                            Nome da receita: {a[0]}
                                            {x}
                                                                      Legenda:
                                                {"#"*53}
                                Tipo: {a[1]}        |  {"A- Doce":<23} /  {"B- Salgado":<23}|
                                Tipo: {a[2]}        |  {"A- Até 3 estrelas":<23} /  {"B- Mais de 3 estrelas":<23}|
                                Tipo: {a[3]}        |  {"A- Quente":<23} /  {"B- Frio":<23}|
                                Tipo: {a[4]}        |  {"A- Menos de 30 minutos":<23} /  {"B- Mais de 30 minutos":<23}|
                                Tipo: {a[5]}        |  {"A- Ate de 2 pessoas":<23} /  {"B- Mais de 2 pessoas":<23}|
                                                {"#"*53}
                                    Numero de ingredientes: {len(a[6])} 
                                            Ingredientes: """)
                            for k in range(len(a[6])):
                                print(f"""          {"Nome:":>48} {i.nomequant[k][k][0]:<15}{" ":8}quantidade: {i.nomequant[k][k][1]}""")
                    else:
                        if i.nome == nome :
                            a = i.retorno()
                            x = i.printar()
                            print(f"""
                            Nome da receita: {a[0]}
                                                                      Legenda:
                                                {"#"*53}
                                Tipo: {a[1]}        |  {"A- Doce":<23} /  {"B- Salgado":<23}|
                                Tipo: {a[2]}        |  {"A- Até 3 estrelas":<23} /  {"B- Mais de 3 estrelas":<23}|
                                Tipo: {a[3]}        |  {"A- Quente":<23} /  {"B- Frio":<23}|
                                Tipo: {a[4]}        |  {"A- Menos de 30 minutos":<23} /  {"B- Mais de 30 minutos":<23}|
                                Tipo: {a[5]}        |  {"A- Ate de 2 pessoas":<23} /  {"B- Mais de 2 pessoas":<23}|
                                                {"#"*53}
                                    Numero de ingredientes: {len(a[6])} 
                                            Ingredientes: """)
                            for k in range(len(a[6])):
                                print(f"""          {"Nome:":>48} {i.nomequant[k][k][0]:<15}{" ":8}quantidade: {i.nomequant[k][k][1]}""")
            else:
                print("Não há dados.")


        elif comando == "D":
            print("-="*30)
            nome = input("Nome do alimento: ")
            if len(lista) >= 1:
                for i in lista:
                    if i.nome == nome:
                        q,w,e,r,t,y,u = parametros()
                        ingre = nomequant(u)
                        lista.remove(i)
                        food = Comida(q,w,e,r,t,y,ingre)
                        lista.append(food)
            else:
                print("Não há elementos.")


        elif comando == "E":
            if len(lista) >= 1:
                tabela(lista)
            else:
                print("Não há elementos.")


        elif comando == "F":
            if len(lista) >= 1:
                deletar = input("Elemento que deseja excluir: ")
                for i in lista:
                    if i.nome == deletar:
                        lista.remove(i)
                        print("Item excluído.")
            else:
                print("Não há elementos.")


        elif comando == "G":
            break
        
        else:
            pass
    return lista


email_center()