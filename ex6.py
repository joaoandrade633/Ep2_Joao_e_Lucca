def questao_para_texto(questao, id):
    titulo = questao["titulo"]
    nivel = questao["nivel"].upper()
    opcoes = questao["opcoes"]
    correta = questao["correta"].upper()

    respostas = "\n".join(f"{letra}: {opcoes[letra]}" for letra in opcoes)

    texto_questao = f"----------------------------------------\n" \
                   f"QUESTAO {id}\n\n" \
                   f"{titulo}\n\n" \
                   f"RESPOSTAS:\n" \
                   f"{respostas}\n" \

    return texto_questao


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
id_questao = 5
saida_formatada = questao_para_texto(questao, id_questao)
print(saida_formatada)