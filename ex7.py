import random

def gera_ajuda(questao):
    opcoes_incorretas = [letra for letra in questao["opcoes"] if letra != questao["correta"]]
    num_opcoes_erradas = random.randint(1, 2)
    opcoes_erradas_sorteadas = random.sample(opcoes_incorretas, num_opcoes_erradas)

    dica = f"DICA:\nOpções certamente erradas: {', '.join(questao['opcoes'][opcao] for opcao in opcoes_erradas_sorteadas)}"

    return dica



questao = {
    "titulo": "Qual destes parques não se localiza em São Paulo?!",
    "nivel": "facil",
    "opcoes": {
        "A": "Ibirapuera",
        "B": "Parque do Carmo",
        "C": "Parque Villa Lobos",
        "D": "Morro da Urca"
    },
    "correta": "D"
}

ajuda = gera_ajuda(questao)
print(ajuda)
