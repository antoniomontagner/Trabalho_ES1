from receita import Receita

def parametros():
#nome
    nome = input("Nome da comida: ")
#palavras_chave
    palavras_chave = []
    while 0>=len(palavras_chave) or 100>=len(palavras_chave) :
        comand = input(f"""
        {"-="*30}
            1 -Inserir palavra chave
            0 - Exit
        {"-="*30}
            Resposta: """).upper()
        if comand == '1':
            palavra = input("\n Palavra chave: ")
            palavras_chave.append(palavra)
        elif comand == '0':
            break
        else:
            print("Input inválido. ")

#doce ou salgado
    doce_salgado = ''
    while doce_salgado != "A" and doce_salgado != "B":
        doce_salgado = input(f"""
{"-="*30}
        O comida é:   
            A - Doce
            B - Salgado
{"-="*30}
        Resposta: """).upper()

#contem gluten
    gluten = ''
    while gluten != "A" and gluten != "B":
        gluten = input(f"""
{"-="*30}
    A receita é:
        A - Com gluten
        B - Sem gluten
{"-="*30}
    Resposta: """).upper()


    
    porcoes = ''
    while porcoes != "A" and porcoes != "B":
        porcoes = input(f"""
{"-="*30}
    Porção geradas:
    
        A - ate de 2 pessoas
        B - mais de 2 pessoas 
{"-="*30}
    Resposta: """).upper()
    
    modo_preparo = input(" Modo de preparo. ")

    descricao = input("Descrição da receita: ")

    print("-="*30)
    while True:
        try:
            n_ingredientes = int(input("Número de ingredientes: "))
            break
        except ValueError:
            print("ERRO. Você não digitou um número!")

    return nome,palavras_chave,doce_salgado,gluten,porcoes,n_ingredientes, descricao, modo_preparo


def lista_ingredientes(n_ingredientes):      #   INGREDIENTES   atualmente uma lista de dicionario
    lista = []
    for i in range(n_ingredientes):
        dic = {}
        print('1='*30)
        nome = input("Nome do ingrediente: ")
        dic[nome] = input("Quantidade em gramas ou unidades: ")
        lista.append(dic)

    return lista


def retornar_receita (receita):     # imprimir os dados de uma receita
    nome, doce_salgado, avaliacoes, gluten, porcoes, lista_ingredientes, descricao, modo_preparo =  receita.retorno()
    print(f"""
    Nome da receita: {nome}
                                                Legenda:
                        {"#"*53}
        Tipo: {doce_salgado}        |  {"A- Doce":<23} /  {"B- Salgado":<23}|
        Tipo: {avaliacoes}        |  {" Avaliação ":<23} /  {" de 0 a 10 ":<23}|
        Tipo: {gluten}        |  {"A- Com gluten":<23} /  {"B- Sem gluten":<23}|
        Tipo: {porcoes}        |  {"A- Ate de 2 pessoas":<23} /  {"B- Mais de 2 pessoas":<23}|
                        {"#"*53}

        Descrição: {descricao}

            Numero de ingredientes: {len(lista_ingredientes)} 
                    Ingredientes: """)
    for k in lista_ingredientes:
        for c,v in k.items():                            
            print(f"""          {"Nome:":>48} {c:<15}{" ":8}quantidade: {v}""")
    print(f"""
            Modo de preparo: {modo_preparo}
    """)


########## interface pesquisa
def menu_nome_receita():
    nome_usuario = input(" Nome do usuario que pretende acessar: ")
    nome_receita = input(" Nome da receita: ")
    return nome_usuario, nome_receita

def menu_pesquisa_receita(lista_total):
    print(lista_total)
    pesquisa = input(f"""
        {"-="*30}
        ######################
        # Pesquisar Receitas #
        ######################
        {"-="*30}
            O que iremos cozinhar hoje? 

                *Colocar nome da receita ou palavra chave
            
            \n    """).upper()
    return pesquisa

def menu_denunciar_motivo():
    motivo = input(f"""
        {"-="*30}
        Motivo da denúncia:
            1 - Contêm conteúdo inapropriado
            2 - Não é uma receita
            3 - Receita plagiada
            0 - Sair
        {"-="*30}
        Resposta: """)
    return motivo

def menu_comando_avaliar():
    avaliar = input("""
            Deseja:
                1 - Avaliar a receita
                2 - Denunciar a receita

                0 - Não fazer nada
        """)
    return avaliar

def menu_verificar_receita_user():
    comand = input("""
        1 - Verificar receitas do usuario
        2 - Deletar receita do usuario

        0 - Exit
        """)
    return comand

def menu_nota_receita():
    nota = input(f"""
    {"-="*30}
    Nota da receita (0-10):
    {"-="*30}
    Resposta: """)
    return nota

def menu_lista_denuncia(lista_denuncia):
    for i in lista_denuncia:
        for c,v in i.items():      # chave, valor de cada item
            print(f" Usuário: {c} receita: {v[0]} motivo: {v[1]}")
    print('-'*40)

def erro404():
    print(" Dados não encontrados. ") 

def invalid_input():
    print("Valor inválido. ")


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
    D - Minha Conta 
    
    E - Sair
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

def menu_input_pin():
    print("Bem vindo, administrador. Por segurança do sistema, favor insira seu pin de administração para prosseguir.")
    pin = input("Pin: ")
    return pin

def interface_menu_user():
    comand = input(f"""{"##"*30}    
    A - Criar Receita
    B - Pesquisa
    C - Minhas Receitas
    D - Pesquisar uma receita própria
    E - Minha Conta 
    
    F - Sair
    {"-="*30}
    Resposta: """).upper()
    return comand

def menu_lista_admin(aux_adm,admin):
    print("ADMIN -="*30)
    print(f'Admin {aux_adm}, Login : {admin.login}, Email : {admin.email}, Senha : {admin.senha}, Pin : {admin.senha_admin}')
    print("-="*30)


def menu_lista_user(aux_user,usuario):
    print("USERS -="*30)
    print(f'Usuario {aux_user}, Login : {usuario.login}, Email : {usuario.email}, Senha : {usuario.senha}')