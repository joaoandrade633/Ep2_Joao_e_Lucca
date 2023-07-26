import random

def sorteia_questao_inedita(questoes, nivel, questoes_sorteadas):
    questoes_do_nivel = questoes.get(nivel, [])
    questoes_ineditas = [questao for questao in questoes_do_nivel if questao not in questoes_sorteadas]
    
    if not questoes_ineditas:
        return None
    
    questao_sorteada = random.choice(questoes_ineditas)
    questoes_sorteadas.append(questao_sorteada)
    
    return questao_sorteada
