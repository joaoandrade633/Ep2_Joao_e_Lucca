import colorama
from colorama import Fore
from colorama import Style
import random



QUESTOES = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
        ]

print(f"{Fore.YELLOW+ Style.BRIGHT}Olá! Você está no jogo dos seus alunos preferidos e terá a oportunidade de enriquecer!{Style.RESET_ALL}")

nome = input('Qual seu nome?')

print(f'\nOk {nome}, você tem direito a pular 3 vezes e 2 ajudas!')
print(f'{Fore.RED + Style.BRIGHT}opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!{Style.RESET_ALL}\n'  )
input('Aperte ENTER para continuar...')

print('\nO jogo já vai começar! Lá vem a primeira questão!\n\nVamos começar com questões do nível FACIL!\n')
input('Aperte ENTER para continuar...')

def valida_questao(questao):
    lista_niveis = ['facil', 'medio', 'dificil']
    lista_caractere = ['', '\t', '\n']
    lista_opcoes = ['A', 'B', 'C', 'D']
    
    correcao = {}
    
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

def valida_questoes(questoes):
    correcao = []
    for questao in questoes:
        erros = valida_questao(questao)
        if not erros:
            correcao.append({})
        else:
            correcao.append(erros)
        
    return correcao

def sorteia_questao_inedita(questoes_sorteadas):
    questoes_nao_sorteadas = [questao for questao in QUESTOES if questao not in questoes_sorteadas]
    if not questoes_nao_sorteadas:
        return None
    return random.choice(questoes_nao_sorteadas)

def questao_para_texto(questao, id_questao):
    titulo = questao["titulo"]
    nivel = questao["nivel"].upper()
    opcoes = questao["opcoes"]
    correta = questao["correta"].upper()

    respostas = "\n".join(f"{letra}: {opcoes[letra]}" for letra in opcoes)

    texto_questao = f"----------------------------------------\n" \
                   f"QUESTAO {id_questao}\n\n" \
                   f"{titulo}\n\n" \
                   f"RESPOSTAS:\n" \
                   f"{respostas}\n"
    return texto_questao

def gera_ajuda(questao):
    opcoes_incorretas = [letra for letra in questao["opcoes"] if letra != questao["correta"]]
    num_opcoes_erradas = random.randint(1, 2)
    opcoes_erradas_sorteadas = random.sample(opcoes_incorretas, num_opcoes_erradas)

    dica = f"DICA:\nOpções certamente erradas: {', '.join(questao['opcoes'][opcao] for opcao in opcoes_erradas_sorteadas)}"

    return dica

def jogo():
    questoes_sorteadas = []
    dinheiro_atual = 0
    pulos = 0

    nome = input('Digite seu nome: ')
    print('Ok,', nome, ', você tem direito a pular 3 vezes e 2 ajudas!')
    print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
    print('Aperte ENTER para continuar...')
    
    id_questao = 0
    while True:
        questao = sorteia_questao_inedita(questoes_sorteadas)

        if questao is None:
            print("Fim do jogo!")
            print('dinheiro atual:', dinheiro_atual)
            break

        id_questao += 1
        print(questao_para_texto(questao, id_questao))

        resposta = input("Sua resposta: ").strip().upper()

        if resposta == "PARAR":
            print("Fim do jogo!")
            print('dinheiro atual:', dinheiro_atual)
            break
        elif resposta == "PULA" and pulos < 3:
            pulos += 1
            if len(questoes_sorteadas) < len(QUESTOES):
                questoes_sorteadas.append(questao)
                print("Pulou para a próxima pergunta.\n")
                print('dinheiro atual:', dinheiro_atual)
            else:
                print("Todas as perguntas já foram puladas.\n")
        elif resposta == "AJUDA":
            ajuda = gera_ajuda(questao)
            print(ajuda)
        elif resposta in ["A", "B", "C", "D"]:
            if resposta == questao["correta"]:
                dinheiro_atual += 1000
                print("Resposta correta! Você ganhou 1000 reais.\n")
                print('dinheiro atual:', dinheiro_atual)
            else:
                print("Resposta incorreta.\n")
                print('dinheiro atual:', dinheiro_atual)
        else:
            print("Opção inválida. Digite uma das letras de resposta válidas ou uma ação (ajuda, pula, parar).\n")

    print(f"Parabens \n{nome}, vc ganhou {dinheiro_atual} reais.")

if __name__ == "__main__":
    jogo()
