from user import User
from user import Admin

lista_admin = []
lista_users = []

lista_admin.append(Admin('admin_1','abc123','admin1@email.com','1111'))
lista_admin.append(Admin('admin_2','abc123','admin2@email.com','2222'))
lista_admin.append(Admin('admin_3','abc123','admin3@email.com','3333'))
lista_admin.append(Admin('admin_4','abc123','admin4@email.com','4444'))
lista_admin.append(Admin('admin_5','abc123','admin5@email.com','5555'))
lista_admin.append(Admin('admin_6','abc123','admin6@email.com','6666'))

def new_user(User):
    lista_users.append(User)