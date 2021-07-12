from user import User
from user import Admin

class BD:
    def __init__(self, lista_admin, lista_users):
        self.lista_admin = lista_admin
        self.lista_users = lista_users

    @property
    def lista_admin(self):
        return self._lista_admin

    @lista_admin.setter
    def lista_admin(self, value):
        self._lista_admin = value
    
    @property
    def lista_users(self):
        return self._lista_users

    @lista_users.setter
    def lista_users(self, value):
        self._lista_users = value

def initial_admin(data):
    a1 = Admin('admin_1','abc123','admin_1@email.com','1111')
    a2 = Admin('admin_2','abc123','admin_2@email.com','2222')
    a3 = Admin('admin_3','abc123','admin_3@email.com','3333') 
    data.lista_admin.append(a1)
    data.lista_admin.append(a2)
    data.lista_admin.append(a3)