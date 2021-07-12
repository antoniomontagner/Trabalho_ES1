from receita import Comida


def tabela(lst):
    l = lst
    lis = l[:]
    
    print(f"""
    {"#"*60}
    #{"DOCE":^29}|{"SALGADO":^28}#
    #{"-"*29}+{"-"*28}#
    #{"QUENTE":^14}|{"FRIO":^14}|{"QUENTE":^13}|{"FRIO":^14}#
    #{"-"*14}+{"-"*14}+{"-"*13}+{"-"*14}#""")
    cont = 0

    for i in lis:
        cont += 1
        doce_quente = ""
        doce_frio = ""
        salgado_quente = ""
        salgado_frio = ""
        if i.doce_salgado == "A" and i.hot_cold == "A":
            if len(i.nome) >= 12:
                doce_quente = i.nome[0:12]
            else:
                doce_quente = i.nome

        elif i.doce_salgado == "A" and i.hot_cold == "B":
            if len(i.nome) >= 12:
                doce_frio = i.nome[0:12]
            else:
                doce_frio = i.nome

        elif i.doce_salgado == "B" and i.hot_cold == "A":
            if len(i.nome) >= 12:
                salgado_quente = i.nome[0:12]
            else:
                salgado_quente = i.nome

        elif i.doce_salgado == "B" and i.hot_cold == "B":
            if len(i.nome) >= 12:
                salgado_frio = i.nome[0:12]
            else:
                salgado_frio = i.nome
        
        print(f""" {cont:^3}#{doce_quente:^14}|{doce_frio:^14}|{salgado_quente:^13}|{salgado_frio:^14}#""")

    print(f"""    {"#"*60}""")


def parametros():
#nome
    nome = input("Nome da comida: ")


#tempo
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


#estrelas

#contem glutem
    glutem = ''
    while glutem != "A" and glutem != "B":
        glutem = input(f"""
{"-="*30}
    A receita é:
        A - Com glutem
        B - Sem glutem
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


    return nome,palavras_chave,doce_salgado,glutem,porcoes,n_ingredientes

def nomequant(n_ingredientes):      # 
    lis = []

    for i in range(n_ingredientes):
        dic = {}
        dic[i] = input("Nome: "),input("Quantidade em gramas ou unidades: ")
        lis.append(dic)

    return lis


def avaliar_receita(receita:Comida):        # para avaliar uma receita
    nota = -1
    while nota < 0 or nota > 10:
        nota = input(f"""
    {"-="*30}
    Nota da receita (0-10):
    {"-="*30}
    Resposta: """)
        if 0 <= nota <= 10:
            receita.avaliar(nota)
            break
        else:
            print("Valor inválido. ")


def denunciar_receita(receita:Comida, lista_denuncia:list):
    motivo = ''
    denuncia = dict
    while len(motivo<=0):
        motivo = input(f"""
        {"-="*30}
        Motivo da denúncia:
            1 - Contêm conteúdo inapropriado
            2 - Não é uma receita
            3 - Receita plagiada

            0 - Sair
        {"-="*30}
        Resposta: """)
    
        if motivo in ("1","2","3"):
            denuncia[receita.nome]="motivo=" + motivo
            lista_denuncia.append(denuncia)
        elif motivo == "0":
            break
        else:
            print("Valor inválido. ")