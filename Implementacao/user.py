class User:
    def __init__(self,login,senha,data,user_receita,cont):
        self.login = login
        self.senha = senha
        self.data = data
        self.user_receita = user_receita 
        self.cont = cont

    def contar(self,contar):
        self.cont += contar
        return self.cont

    def nome_data(self):
        return f"""{"":10} User: {self.login}     Data de login: {self.data}"""