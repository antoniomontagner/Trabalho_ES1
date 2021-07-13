from receita import Receita

def avaliar_receita(receita:Receita):        # para avaliar uma receita
    nota = -1
    while nota < 0 or nota > 10:
        nota = input(f"""
    {"-="*30}
    Nota da receita (0-10):
    {"-="*30}
    Resposta: """)
        if 0 <= nota <= 10:
            receita.avaliar(nota)
            break
        else:
            print("Valor inválido. ")


def denunciar_receita(nome_usuario:str, nome_receita:str, lista_denuncia:list):
    motivo = ''
    while len(motivo<=0):
        denuncia = {}
        motivo = input(f"""
        {"-="*30}
        Motivo da denúncia:
            1 - Contêm conteúdo inapropriado
            2 - Não é uma receita
            3 - Receita plagiada
            0 - Sair
        {"-="*30}
        Resposta: """)
    
        if motivo in ("1","2","3"):
            denuncia[nome_usuario]=[nome_receita,motivo]
            lista_denuncia.append(denuncia)
        elif motivo == "0":
            break
        else:
            print("Valor inválido. ")
            motivo = ''
