class Receita:
    def __init__ (self,nome,palavras_chave,doce_salgado,gluten,porcoes,nomequant, descricao):
        self.nome = nome
        self.palavras_chave = palavras_chave
        self.doce_salgado = doce_salgado
        self.avaliacoes = []
        self.media_avaliacao = 0
        self.gluten = gluten
        #self.temp = temp
        self.porcoes = porcoes
        self.nomequant = nomequant      # lista de ingredientes
        self.descricao = descricao
    
    def retorno (self):
        return self.nome,self.doce_salgado,self.avaliacoes,self.gluten,self.porcoes,self.nomequant

    def avaliar(self, nota):
        self.avaliacoes.append(nota)
        media = 0
        
        for i in self.avaliacoes:
            media+=i

        self.media_avaliacao = media/len(self.avaliacoes)
        return self.media_avaliacao
    
    # def printar(self):
    #     return self.nome                                         #   nao usa pra nada
    

# class Bolo(Comida):         # nao usa pra nada 
#     def __init__(self,nome,doce_salgado,star,hot_cold,temp,porc,nomequant,r_padrao):
#             Comida.__init__(self,nome,doce_salgado,star,hot_cold,temp,porc,nomequant)
#             self.r_padrao = r_padrao   # defifir que é uma receita padrao do sistema
            
#     def printar(self):
#         return "A receita de bolo vem de bonus."