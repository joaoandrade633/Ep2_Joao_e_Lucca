#EP2 ex1
# Transforma Base de Questões
def transforma_base(lista):
    dict_nivel = {}
    for dict_questao in lista:
        if dict_questao['nivel'] not in dict_nivel:
            dict_nivel[dict_questao['nivel']] = [dict_questao]
        else:
            dict_nivel[dict_questao['nivel']] += [dict_questao]
    return dict_nivel