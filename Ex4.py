import random

def sorteia_questao(questoes, nivel):
    questoes_nivel = questoes.get(nivel, [])
    if not questoes_nivel:
        return None
    return random.choice(questoes_nivel)
