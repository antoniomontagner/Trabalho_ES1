class User:
    def __init__(self,login,senha,email,user_receita):
        self.login = login
        self.senha = senha
        self.email = email
        self.user_receita = user_receita

    @property
    def login(self):
         return self._login

    @login.setter
    def login(self, value):
         self._login = value

    @property
    def senha(self):
         return self._senha

    @senha.setter
    def senha(self, value):
        self._senha = value
            
    @property
    def email(self):
         return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def user_receita(self):
         return self._user_receita

    @user_receita.setter
    def user_receita(self, value):
        self._user_receita = value

class Admin(User):
    def __init__(self, login, senha, email, senha_admin):
        self.login = login
        self.senha = senha
        self.email = email
        self.senha_admin = senha_admin
        