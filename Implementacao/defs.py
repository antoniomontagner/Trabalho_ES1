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
        A receita é:   
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