class User:
    def __init__(self,login,senha,email,user_receita):
        self.login = login
        self.senha = senha
        self.email = email
        self.user_receita = user_receita

    def nome_data(self):
        return f"""{"":10} User: {self.login}     Data de login: {self.email}"""

class Admin(User):
    def __init__(self, login, senha, email, user_receita, senha_admin):
        self.login = login
        self.senha = senha
        self.email = email
        self.user_receita = user_receita
        self.senha_admin = senha_admin