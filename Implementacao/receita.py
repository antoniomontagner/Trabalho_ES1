class Comida:
    def __init__ (self,nome,doce_salgado,star,hot_cold,temp,porc,nomequant):
        self.nome = nome
        self.doce_salgado = doce_salgado
        self.star = star
        self.hot_cold = hot_cold
        self.temp = temp
        self.porc = porc
        self.nomequant = nomequant
    
    def retorno (self):
        return self.nome,self.doce_salgado,self.star,self.hot_cold,self.temp,self.porc,self.nomequant
    
    def printar(self):
        return self.nome                                         #polimorfismo com Bolo.printar
    

class Bolo(Comida):             #heranca
    def __init__(self,nome,doce_salgado,star,hot_cold,temp,porc,nomequant,r_padrao):
            Comida.__init__(self,nome,doce_salgado,star,hot_cold,temp,porc,nomequant)
            self.r_padrao = r_padrao   # defifir que é uma receita padrao do sistema
            
    def printar(self):
        return "A receita de bolo vem de bonus."