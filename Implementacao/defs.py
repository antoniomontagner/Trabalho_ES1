from receita import Receita

#def tabela(lista_receita):
#    lis = lista_receita[:]
#    
#    print(f"""
#    {"#"*60}
#    #{"DOCE":^29}|{"SALGADO":^28}#
#    #{"-"*29}+{"-"*28}#
#    #{"QUENTE":^14}|{"FRIO":^14}|{"QUENTE":^13}|{"FRIO":^14}#
#    #{"-"*14}+{"-"*14}+{"-"*13}+{"-"*14}#""")
#    cont = 0
#
#    for i in lis:
#        cont += 1
#        doce_quente = ""
#        doce_frio = ""
#        salgado_quente = ""
#        salgado_frio = ""
#        if i.doce_salgado == "A" and i.hot_cold == "A":
#            if len(i.nome) >= 12:
#                doce_quente = i.nome[0:12]
#            else:
#                doce_quente = i.nome
#
#        elif i.doce_salgado == "A" and i.hot_cold == "B":
#            if len(i.nome) >= 12:
#                doce_frio = i.nome[0:12]
#            else:
#                doce_frio = i.nome
#
#        elif i.doce_salgado == "B" and i.hot_cold == "A":
#            if len(i.nome) >= 12:
#                salgado_quente = i.nome[0:12]
#            else:
#                salgado_quente = i.nome
#
#        elif i.doce_salgado == "B" and i.hot_cold == "B":
#            if len(i.nome) >= 12:
#                salgado_frio = i.nome[0:12]
#            else:
#                salgado_frio = i.nome
#        
#        print(f""" {cont:^3}#{doce_quente:^14}|{doce_frio:^14}|{salgado_quente:^13}|{salgado_frio:^14}#""")
#
#    print(f"""    {"#"*60}""")


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

#porcoes
    porcoes = ''
    while porcoes != "A" and porcoes != "B":
        porcoes = input(f"""
{"-="*30}
    Porção geradas:
    
        A - ate de 2 pessoas
        B - mais de 2 pessoas 
{"-="*30}
    Resposta: """).upper()

    print("-="*30)
    while True:
        try:
            n_ingredientes = int(input("Número de ingredientes: "))
            break
        except ValueError:
            print("ERRO. Você não digitou um número!")

    descricao = input("Descrição da receita: ")

    return nome,palavras_chave,doce_salgado,gluten,porcoes,n_ingredientes, descricao


def lista_ingredientes(n_ingredientes):      #   INGREDIENTES   atualmente uma lista de dicionario
    lista = []
    for i in range(n_ingredientes):
        dic = {}
        print('1='*30)
        nome = input("Nome do ingrediente: ")
        dic[nome] = input("Quantidade em gramas ou unidades: ")
        lista.append(dic)

    return lista

################       funcoes (base) para o administrador
def acessar_denuncias(lista_denuncia:list, lista_users):
    for i in lista_denuncia:
        for c,v in i.items():      # chave, valor de cada item
            print(f" Usuário: {c} receita: {v[0]} motivo: {v[1]}")
    print('-'*40)
    
    while True:
        comand = input("""
        1 - Verificar receitas do usuario
        2 - Deletar receita do usuario

        0 - Exit
        """)

        if comand == '1':
            nome_usuario = input(" Nome do usuario que pretende acessar: ")
            nome_receita = input(" Nome da receita: ")
            try:
                for i in lista_denuncia:
                    for c,v in i.items():
                        if nome_usuario == c:
                            if nome_receita == v[0]:
                                verificar_receitas(nome_usuario, nome_receita, lista_users)  # metodo para retornar os dados
                
            except:
                print(" Dados não encontrados. ")

        elif comand == '2':
            nome_usuario = input(" Nome do usuario que pretende deletar: ")
            nome_receita = input(" Nome da receita que pretende deletar: ")
            try:
                for i in lista_denuncia:
                    dado_encontrado = False
                    for c,v in i.items():
                        if nome_usuario == c:
                            if nome_receita == v[0]:
                                dado_encontrado = True
                    if dado_encontrado:
                        lista_denuncia.pop(i)
                        # colocar o pop da lista do usuario
                        deletar_receitas(nome_usuario, nome_receita, lista_users)
            except:
                print(" Dados não encontrados. ")

def verificar_receitas(nome_usuario, nome_receita, lista_users):    # verificar a conta do usuario
    try:
        for i in lista_users:
            if i.nome == nome_usuario:
                for j in i.lista_receitas:
                    if j.nome == nome_receita:
                        print(f" Receita denunciada: {j}")
    except:
        print(" Dados não encontrados. ")   

def deletar_receitas(nome_usuario, nome_receita, lista_users):      # deletar a receita do usuario
    try:
        for i in lista_users:
            if i.nome == nome_usuario:
                for j in i.lista_receitas:
                    if j.nome == nome_receita:
                        i.lista_receitas.pop(j)
    except:
        print(" Dados não encontrados. ")   