def valida_questao(questao):
    retorno = {}

    chaves_presentes = {}
    for chave in questao.keys():
        chaves_presentes[chave] = True

    if not chaves_presentes.get('titulo'):
        retorno['titulo'] = 'nao_encontrado'
    if not chaves_presentes.get('nivel'):
        retorno['nivel'] = 'nao_encontrado'
    if not chaves_presentes.get('opcoes'):
        retorno['opcoes'] = 'nao_encontrado'
    if not chaves_presentes.get('correta'):
        retorno['correta'] = 'nao_encontrado'

    num_chaves = 0
    for chave in questao:
        num_chaves += 1

    if num_chaves != 4:
        retorno['outro'] = 'numero_chaves_invalido'

    if 'titulo' in chaves_presentes:
        titulo = questao['titulo']
        titulo_vazio = True
        for caractere in titulo:
            if not caractere.keys():
                titulo_vazio = False
                break
        if titulo_vazio:
            retorno['titulo'] = 'vazio'

    niveis_validos = ['facil', 'medio', 'dificil']
    if 'nivel' in chaves_presentes and questao['nivel'] not in niveis_validos:
        retorno['nivel'] = 'valor_errado'

    if 'opcoes' in chaves_presentes:
        opcoes = questao['opcoes']
        if len(opcoes) != 4:
            retorno['opcoes'] = 'tamanho_invalido'
        elif not ('A' in opcoes and 'B' in opcoes and 'C' in opcoes and 'D' in opcoes):
            retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        else:
            opcoes_vazias = {}
            if not opcoes['A']:
                opcoes_vazias['A'] = 'vazia'
            if not opcoes['B']:
                opcoes_vazias['B'] = 'vazia'
            if not opcoes['C']:
                opcoes_vazias['C'] = 'vazia'
            if not opcoes['D']:
                opcoes_vazias['D'] = 'vazia'
            if opcoes_vazias:
                retorno['opcoes'] = opcoes_vazias

    corretas_validas = ['A', 'B', 'C', 'D']
    if 'correta' in chaves_presentes and questao['correta'] not in corretas_validas:
        retorno['correta'] = 'valor_errado'

    return retorno
