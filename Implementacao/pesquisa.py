from receita import Receita
from user import User #
import interface

def pesquisar_receita(data):

    lista_total = []                       #   lista de todas as receitas
    for i in data.lista_users:
        for j in i:
            lista_total.append(j.lista_receitas)
    pesquisa = menu_pesquisa_receita(lista_total)

    #for receita in lista_total: 
    for receita_encontrada in lista_total:
        if len (receita_encontrada.palavras_chave) > 0:
            for palavra in receita_encontrada.palavras_chave:
                if pesquisa == palavra:             #imprimir a uma tabela sobre a receita
                    interface.retornar_receita(receita_encontrada)
                    denunciar_avaliar(receita_encontrada,data.lista_denuncia)       # lista de denuncia
        else:
            for receita_encontrada in lista_total:
                for ingrediente in receita_encontrada.lista_ingredientes:
                    if pesquisa == ingrediente.keys():
                        interface.retornar_receita(receita_encontrada)
                    else:
                        print("0 receitas encontradas.")


def avaliar_receita(receita):        # para avaliar uma receita
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


def denunciar_receita(receita, lista_denuncia:list):
    motivo = ''
    while len(motivo<=0):
        denuncia = {}
        motivo = menu_denunciar_motivo()

        if motivo in ("1","2","3"):
            denuncia[receita.nome_usuario]=[receita.nome,motivo]
            lista_denuncia.append(denuncia)
        elif motivo == "0":
            break
        else:
            print("Valor inválido. ")
            motivo = ''

def denunciar_avaliar(receita,lista_denuncia):
    while True:
        comando = menu_comando_avaliar()
        if comando == '1':
            avaliar_receita(receita)
        elif comando == '2':
            denunciar_receita(receita,lista_denuncia)
        elif comando == '0':
            break
        else:
            print(" Comando inválido. ")


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
            nome_usuario, nome_receita = menu_nome_receita()
            try:
                for i in lista_denuncia:
                    for c,v in i.items():
                        if nome_usuario == c:
                            if nome_receita == v[0]:
                                verificar_receitas(nome_usuario, nome_receita, lista_users)  # metodo para retornar os dados
            except:
                print(" Dados não encontrados. ")

        elif comand == '2':
            nome_usuario, nome_receita = menu_nome_receita()
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
        
        elif comand == '0':
            break

        else:
            print(" Comando inválido. ")

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