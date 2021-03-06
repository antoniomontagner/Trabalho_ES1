import sistema
from bd import BD, initial_admin, initial_user
import interface


def main():
    lista_admin = []
    lista_users = []
    lista_denuncia = []
    user_atual = 0
    data = BD(lista_admin, lista_users, lista_denuncia)
    initial_admin(data)
    initial_user(data)
    normal_user = False
    sair = False

    while user_atual != 'exit':
        SisInterface = interface.Interface()
        s = sistema.Sistema(SisInterface, 1)
        # s2 = sistema.Sistema(SisInterface, 2)  # Singleton test
        # if s == s2:
        #    print(f"Singleton, n de verificacao s1:{s.n} s2: {s2.n}")
        user_atual = s.menu_cadastro(data)
        for i in data.lista_admin:
            if user_atual == i.login:
                s.menu_admin(user_atual, i, data)
            else:
                normal_user = True
        if normal_user:
            for j in data.lista_users:
                if user_atual == j.login:
                    s.menu_user(user_atual, j, data)


main()
