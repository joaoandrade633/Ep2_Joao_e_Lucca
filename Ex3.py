#EP2 ex3
#Valida Lista de Questões
def valida_questao(questao):
    correcao = {}
    lista_niveis = ['facil', 'medio', 'dificil']
    lista_caractere = ['', '\t', '\n']
    lista_opcoes = ['A', 'B', 'C', 'D']
    if len(questao) != 4:
        correcao['outro'] = 'numero_chaves_invalido'
    if not questao.get('titulo'):
        correcao['titulo'] = 'nao_encontrado'
    elif questao.get('titulo').strip() in lista_caractere:
        correcao['titulo'] = 'vazio'
    if not questao.get('nivel'):
        correcao['nivel'] = 'nao_encontrado'
    elif questao.get('nivel') not in lista_niveis:
        correcao['nivel'] = 'valor_errado'
    if questao.get('opcoes') is None:
        correcao['opcoes'] = 'nao_encontrado'
    elif len(questao.get('opcoes')) != 4:
        correcao['opcoes'] = 'tamanho_invalido'
    elif len(questao.get('opcoes')) == 4:
        for c, v in questao.get('opcoes').items():
            if c not in lista_opcoes:
                correcao['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                break
            elif v.strip() in lista_caractere:
                if correcao.get('opcoes'):
                    correcao['opcoes'][c] = 'vazia'
                else:
                    correcao['opcoes'] = {}
                    correcao['opcoes'][c] = 'vazia'
    if not questao.get('correta'):
        correcao['correta'] = 'nao_encontrado'
    elif questao.get('correta') not in lista_opcoes:
        correcao['correta'] = 'valor_errado'

    return correcao

def valida_questoes(lista_questoes):
    correcao = []
    for questao in lista_questoes:
        erros = valida_questao(questao)
        if not erros:
            correcao.append({})
        else:
            correcao.append(erros)
        
    return correcao