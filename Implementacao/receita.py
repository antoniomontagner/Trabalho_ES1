class Comida:
    def __init__ (self,nome,palavras_chave,doce_salgado,avaliacoes,glutem,porc,nomequant):
        self.nome = nome
        self.palavras_crave = palavras_chave
        self.doce_salgado = doce_salgado
        self.avaliacoes = avaliacoes
        self.glutem = glutem
        #self.temp = temp
        self.porcoes = porc
        self.nomequant = nomequant      # lista de ingredientes
    
    def retorno (self):
        return self.nome,self.doce_salgado,self.avaliacoes,self.glutem,self.porcoes,self.nomequant
    
    def printar(self):
        return self.nome                                         #polimorfismo com Bolo.printar         nao usa pra nada
    

class Bolo(Comida):             #heranca            #nao usa pra nada 
    def __init__(self,nome,doce_salgado,star,hot_cold,temp,porc,nomequant,r_padrao):
            Comida.__init__(self,nome,doce_salgado,star,hot_cold,temp,porc,nomequant)
            self.r_padrao = r_padrao   # defifir que é uma receita padrao do sistema
            
    def printar(self):
        return "A receita de bolo vem de bonus."