from receita import Receita
from user import User
from user import Admin  #
from bd import BD, initial_admin
from defs import parametros

# from defs import nomequant -> lista_ingredientes
import sistema as s

def main():
    lista_admin_ = []
    lista_users_ = []
    lista_denuncia = []
    user_atual = 0
    data = BD(lista_admin_, lista_users_, lista_denuncia)
    initial_admin(data)
    initial_user(data)
    normal_user = False
    sair = False
    
    while user_atual != 'exit':
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