#from receita import Receita
#from user import User #
import interface

def pesquisar_receita(data):

    lista_total = []                       #   lista de todas as receitas
    for i in data.lista_users:
        #for j in i:
        lista_total.append(i.lista_receitas)
        print(i.lista_receitas)
    pesquisa = interface.menu_pesquisa_receita(lista_total)

    #for receita in lista_total: 
    for receita_encontrada in lista_total[0]:
        if len (receita_encontrada.palavras_chave) > 0:
            for palavra in receita_encontrada.palavras_chave:
                print(palavra,pesquisa)
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
        nota = interface.menu_nota_receita()
        if 0 <= nota <= 10:
            receita.avaliar(nota)
            break
        else:
            interface.invalid_input()

def denunciar_receita(receita, lista_denuncia:list):
    motivo = ''
    while len(motivo) <=0 :
        denuncia = {}
        motivo = interface.menu_denunciar_motivo()

        if motivo in ("1","2","3"):
            denuncia[receita.nome_usuario]=[receita.nome,motivo]
            lista_denuncia.append(denuncia)
        elif motivo == "0":
            break
        else:
            interface.invalid_input()
            motivo = ''

def denunciar_avaliar(receita,lista_denuncia):
    while True:
        comando = interface.menu_comando_avaliar()
        if comando == '1':
            avaliar_receita(receita)
        elif comando == '2':
            denunciar_receita(receita,lista_denuncia)
        elif comando == '0':
            break
        else:
            interface.invalid_input()


################       funcoes (base) para o administrador
def acessar_denuncias(lista_denuncia:list, lista_users):
    interface.menu_lista_denuncia(lista_denuncia)
    
    while True:
        comand = interface.menu_verificar_receita_user()
        if comand == '1':
            nome_usuario, nome_receita = interface.menu_nome_receita()
            try:
                for i in lista_denuncia:
                    for c,v in i.items():
                        if nome_usuario == c:
                            if nome_receita == v[0]:
                                verificar_receitas(nome_usuario, nome_receita, lista_users)  # metodo para retornar os dados
            except:
                interface.erro404()

        elif comand == '2':
            nome_usuario, nome_receita = interface.menu_nome_receita()
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
                interface.erro404()
        
        elif comand == '0':
            break

        else:
            interface.invalid_input()
def verificar_receitas(nome_usuario, nome_receita, lista_users):    # verificar a conta do usuario
    try:
        for i in lista_users:
            if i.nome == nome_usuario:
                for j in i.lista_receitas:
                    if j.nome == nome_receita:
                        print(f" Receita denunciada: {j}")
    except:
        interface.erro404()  

def deletar_receitas(nome_usuario, nome_receita, lista_users):      # deletar a receita do usuario
    try:
        for i in lista_users:
            if i.nome == nome_usuario:
                for j in i.lista_receitas:
                    if j.nome == nome_receita:
                        i.lista_receitas.pop(j)
    except:
        interface.erro404()   
