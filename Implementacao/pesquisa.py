#from receita import Receita
#from user import User #
import interface


def pesquisar_receita(data):

    lista_total = []  # era uma lista de listas das receitas dos usuarios agora é uma lista com apenas receitas
    for i in data.lista_users:
        for j in i.lista_receitas:
            lista_total.append(j)
    # print(len(lista_total))

    continuar = True
    while continuar:
        pesquisa = interface.menu_pesquisa_receita(lista_total)
        if pesquisa != 'F':
            # for receita in lista_total:
            if len(lista_total) > 0:
                receita_encontrada = False
                encontro = ''
                for receita in lista_total:  # uma lissta da lista
                    # for receita in receita_encontrada:  # a receita da lita .palavra_chave
                    # if len(receita.palavras_chave) > 0:
                    # if not(receita_encontrada):
                    for palavra in receita.palavras_chave:
                        if pesquisa == palavra:  # imprimir a uma tabela sobre a receita
                            interface.retornar_receita(receita)
                            # lista de denuncia
                            denunciar_avaliar(receita, data.lista_denuncia)
                            receita_encontrada = True
                            encontro = 's'
                    if encontro == '':
                        if pesquisa == receita.nome:
                            interface.retornar_receita(receita)
                            # lista de denuncia
                            denunciar_avaliar(receita, data.lista_denuncia)
                            receita_encontrada = True
                            encontro = 's'
                    encontro = ''

                if not(receita_encontrada):
                    interface.retorno_print("Receita não encontrada. ")
                    sair = interface.sem_resposta_continuar_pesquisa()
                    if sair == '1':
                        continuar = False
                        break
                    elif sair == '2':
                        pass
                    else:
                        interface.retorno_print(" Inválido. ")

            else:
                interface.retorno_print(" # Sem receitas no banco.  ")

        elif pesquisa == 'F':
            sair = interface.sem_resposta_continuar_pesquisa()
            if sair == '1':
                continuar = False
                break
            elif sair == '2':
                pass
            else:
                interface.retorno_print(" Inválido. ")


def avaliar_receita(receita):        # para avaliar uma receita
    nota = -1
    while nota < 0 or nota > 10:
        nota = interface.menu_nota_receita()
        if 0 <= nota <= 10:
            receita.avaliar(nota)
            break
        else:
            interface.invalid_input()


def denunciar_receita(receita, lista_denuncia: list):
    motivo = ''
    while len(motivo) <= 0:
        denuncia = {}
        motivo = interface.menu_denunciar_motivo()

        if motivo in ("1", "2", "3"):
            denuncia[receita.nome_usuario] = [receita.nome, motivo]
            lista_denuncia.append(denuncia)
        elif motivo == "0":
            break
        else:
            interface.invalid_input()
            motivo = ''


def denunciar_avaliar(receita, lista_denuncia):
    usados = []
    while True:
        comando = interface.menu_comando_avaliar()
        if comando == '1' and (comando not in usados):
            avaliar_receita(receita)
            usados.append('1')
        elif comando == '2' and (comando not in usados):
            denunciar_receita(receita, lista_denuncia)
            usados.append('2')
        elif comando == '0':
            usados = []
            break
        else:
            interface.invalid_input()


# funcoes (base) para o administrador
def acessar_denuncias(lista_denuncia: list, lista_users):
    interface.menu_lista_denuncia(lista_denuncia)

    while True:
        comand = interface.menu_verificar_receita_user()
        if comand == '1':
            nome_usuario, nome_receita = interface.menu_nome_receita()
            try:
                for i in lista_denuncia:
                    for c, v in i.items():
                        if nome_usuario == c:
                            if nome_receita == v[0]:
                                # metodo para retornar os dados
                                verificar_receitas(
                                    nome_usuario, nome_receita, lista_users)
            except:
                interface.erro404()

        elif comand == '2':
            nome_usuario, nome_receita = interface.menu_nome_receita()
            try:
                for i in lista_denuncia:
                    dado_encontrado = False
                    for c, v in i.items():
                        if nome_usuario == c:
                            if nome_receita == v[0]:
                                dado_encontrado = True
                    if dado_encontrado:
                        lista_denuncia.pop(i)
                        # colocar o pop da lista do usuario
                        deletar_receitas(
                            nome_usuario, nome_receita, lista_users)
            except:
                interface.erro404()

        elif comand == '0':
            break

        else:
            interface.invalid_input()


# verificar a conta do usuario
def verificar_receitas(nome_usuario, nome_receita, lista_users):
    try:
        for i in lista_users:
            if i.nome == nome_usuario:
                for j in i.lista_receitas:
                    if j.nome == nome_receita:
                        interface.retorno_print(f" Receita denunciada: {j}")
    except:
        interface.erro404()


# deletar a receita do usuario
def deletar_receitas(nome_usuario, nome_receita, lista_users):
    try:
        for i in lista_users:
            if i.nome == nome_usuario:
                for j in i.lista_receitas:
                    if j.nome == nome_receita:
                        i.lista_receitas.pop(j)
    except:
        interface.erro404()
