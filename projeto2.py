# 90699 - Afonso Luis de Freitas Matos

from parte1 import e_palavra

from itertools import   permutations    as permutacoes,\
                        count           as contar_apartir

def verifica_maiusculas(iteravel):
    """Verifica se um objeto iteravel so tem letras maiusculas.

    Args:
        iteravel (collections.Iterable)

    Retorna:
        bool: True se `iteravel` so contem letras maiusculas. False caso o
            contrario.

    Exemplos:
        >>> verifica_maiusculas('ABCd')
        False
        >>> verifica_maiusculas(('A', 'B', 'C'))
        True
    """

    for i in iteravel:

        if type(i) != str or len(i) != 1 or not 'A' <= i <= 'Z':
            return False

    return True

def verifica_string_de_tuplo(string, tuplo_letras):
    """Verifica se uma string usa apenas os caracteres disponiveis num tuplo.

    Args:
        string (str)
        tuplo_letras (tuple)

    Retorna:
        bool: True se `string` usa os caracteres disponiveis em `tuplo_letras`.
            False caso o contrario.

    Exemplos:
        >>> verifica_string_de_tuplo('AB', ('A', 'B', 'C'))
        True
        >>> verifica_string_de_tuplo('ABA', ('A', 'B', 'C'))
        False
    """

    disponiveis = list(tuplo_letras)

    for x in string:

        if not x in disponiveis:
            return False

        disponiveis.remove(x)

    return True

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
# TAD palavra_potencial:
#
# E representado por um tuplo. O primeiro elemento desse tuplo contem a cadeia
# de caracteres representada. O segundo elemento desse tuplo contem o conjunto
# de letras que estavam disponiveis quando o TAD foi criado.
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #

def cria_palavra_potencial(string, tuplo):
    """Cria um TAD palavra_potencial com uma string e tuplo.

    Args:
        string (str)
        tuplo (tuple)

    Levanta:
        ValueError:
            1) Caso `string` nao for do tipo str ou `tuplo_letras` nao for
                do tipo tuple.
            2) Caso `string` ou `tuplo_letras` nao contenham so letras
                maiusculas.
            3) Caso `string` nao use so as letras disponiveis em
                `tuplo_letras`.

    Retorna:
        TAD palavra_potencial: Representa `string` e `tuplo`.
    """

    erro_args = ValueError('cria_palavra_potencial:argumentos invalidos.')

    # Verifica os tipos dos argumentos
    if type(string) != str or type(tuplo) != tuple:
        raise erro_args

    # Verifica validade dos argumentos
    if not verifica_maiusculas(string) or not verifica_maiusculas(tuplo):
        raise erro_args

    # Verifica validade da palavra
    if not verifica_string_de_tuplo(string, tuplo):
        raise ValueError('cria_palavra_potencial:a palavra nao e valida.')

    return (string, tuplo)

def palavra_tamanho(pp):
    """Obtem o tamanho da palavra representada por uma palavra_potencial.

    Args:
        pp (TAD palavra_potencial)

    Retorna:
        int: Tamanho da palavra que `pp` representa.
    """

    return len( palavra_potencial_para_cadeia(pp) )

def e_palavra_potencial(universal):
    """Verifica se o argumento e uma palavra_potencial.

    Args:
        universal (object)

    Retorna:
        bool: True se `universal` for considerado uma palavra_potencial. False
            caso o contrario.
    """

    # Verifica estrutura do objeto
    if type(universal) != tuple or len(universal) != 2:
        return False

    el1, el2 = universal

    # Verifica tipos dos elementos do tuplo
    if type(el1) != str or type(el2) != tuple:
        return False

    string, tuplo = universal

    # Verifica validade dos elementos
    if not verifica_maiusculas(string) or not verifica_maiusculas(tuplo):
        return False

    # Verifica validade da palavra
    if not verifica_string_de_tuplo(string, tuplo):
        return False

    return True

def palavras_potenciais_iguais(pp1, pp2):
    """Verifica se duas palavra_potencial representam a mesma palavra.

    Args:
        pp1 (TAD palavra_potencial)
        pp2 (TAD palavra_potencial)

    Retorna:
        bool: True se `pp1` representar a mesma palavra que `pp2`.
    """

    cadeia_1 = palavra_potencial_para_cadeia(pp1)
    cadeia_2 = palavra_potencial_para_cadeia(pp2)

    return cadeia_1 == cadeia_2

def palavra_potencial_menor(pp1, pp2):
    """Verifica se uma palavra_potencial representa uma palavra alfabeticamente
    anterior a palavra representada por outra palavra_potencial.

    Args:
        pp1 (TAD palavra_potencial)
        pp2 (TAD palavra_potencial)

    Retorna:
        bool: True se a palavra representada por `pp1` for anterior
            alfabeticamente a representada por `pp2`.
    """

    cadeia_1 = palavra_potencial_para_cadeia(pp1)
    cadeia_2 = palavra_potencial_para_cadeia(pp2)

    return cadeia_1 < cadeia_2

def palavra_potencial_para_cadeia(pp):
    """Obtem a cadeia de caracteres representada por uma palavra_potencial.

    Args:
        pp (TAD palavra_potencial)

    Retorna:
        str: Palavra que `pp` representa.
    """

    return pp[0]

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
# TAD conjunto_palavras
#
# E representado por uma lista. Esta lista contem zero ou mais elementos
# palavra_potencial unicos.
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #

def cria_conjunto_palavras():
    """Cria um TAD conjunto_palavras vazio.

    Retorna:
        TAD conjunto_palavras
    """

    return list()

def numero_palavras(cp):
    """Obtem o numero de palavras guardadas num conjunto_palavras.

    Args:
        cp (TAD conjunto_palavras)

    Retorna:
        int: Numero de palavras em `cp`.
    """

    return len(cp)

def subconjunto_por_tamanho(cp, n):
    """Obtem uma lista de palavra_potencial dum conjunto_palavras que
    representem palavras de um dado tamanho.

    Args:
        cp (TAD conjunto_palavras)
        n (int)

    Retorna:
        list: Contem zero ou mais palavra_potencial de `cp` que representem
            palavras com tamanho igual a `n`.
    """

    return [ pp for pp in cp if palavra_tamanho(pp) == n ]

def conjunto_palavras_contem(cp, pp):
    """Verifica se um conjunto_palavras contem uma dada palavra_potencial.

    Args:
        cp (TAD conjunto_palavras)
        pp (TAD palavra_potencial)

    Retorna:
        bool: True se `cp` conter `pp`. False caso o contrario.
    """

    # Subconjunto onde `pp` pode estar contida.
    subconjunto = subconjunto_por_tamanho(cp, palavra_tamanho(pp))

    for x in subconjunto:
        if palavras_potenciais_iguais(x, pp):
            return True

    return False

def acrescenta_palavra(cp, pp):
    """Acrescenta uma palavra_potencial a um conjunto_palavras.

    Args:
        cp (TAD conjunto_palavras)
        pp (TAD palavra_potencial)

    Levanta:
        ValueError: Caso `cp` nao seja um TAD conjunto_palavras ou `pp` nao seja
            um TAD palavra_potencial.

    Nota: `cp` fica inalterado se tiver uma palavra_potencial igual a `pp`.
    """

    # Verifica validade dos argumentos
    if not e_conjunto_palavras(cp) or not e_palavra_potencial(pp):
        raise ValueError("acrescenta_palavra:argumentos invalidos.")

    # Verifica se a nova palavra_potencial e unica
    if not conjunto_palavras_contem(cp, pp):
        cp.append(pp)

def e_conjunto_palavras(universal):
    """Verifica se um argumento e um TAD conjunto_palavras.

    Args:
        universal (object)

    Retorna:
        bool: True caso `universal` for um TAD conjunto_palavras. False caso o
            contrario.
    """

    # Verifica o tipo de objeto
    if type(universal) != list:
        return False

    lista = universal

    # Verifica existencia de apenas palavra_potencial
    for el in lista:
        if not e_palavra_potencial(el):
            return False

    pps = lista

    # Verifica unicidade de cada elemento
    for i in range(len(pps) - 1):

        # Se houver outra palavra_potencial igual
        if conjunto_palavras_contem(pps[i + 1:], pps[i:]):

            return False

    return True

def conjuntos_palavras_iguais(cp1, cp2):
    """Verifica se dois conjunto_palavras sao iguais.

    Args:
        cp1 (TAD conjunto_palavras)
        cp2 (TAD conjunto_palavras)

    Retorna:
        bool: True caso `cp1` conter as mesmas palavras que `cp2`.
    """

    # Verifica se tamanhos sao distintos
    if numero_palavras(cp1) != numero_palavras(cp2):
        return False

    # Verifica se `cp2` nao contem alguma palavra_potencial de `cp1`
    for pp1 in cp1:
        if not conjunto_palavras_contem(cp2, pp1):
            return False

    return True

def conjunto_palavras_para_cadeia(cp):
    """Obtem a representacao em string de um conjunto_palavras.

    Args:
        cp (TAD conjunto_palavras)

    Retorna:
        str: Representacao de `cp` em cadeia de caracteres.
    """

    palavras = {}

    # Indexa as palavras por tamanho
    for pp in cp:

        tamanho = str( palavra_tamanho(pp) )
        cadeia  = palavra_potencial_para_cadeia(pp)

        if tamanho in palavras:
            palavras[tamanho].append(cadeia)
        else:
            palavras[tamanho] = [cadeia]

    subconjuntos = []

    # Representa em string cada subconjunto
    for n in sorted(palavras):
        subconjuntos.append(n + '->[' + ', '.join( sorted(palavras[n]) ) + ']')

    # Representa o conjunto total
    return '[' + ';'.join(subconjuntos) + ']'

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #
# TAD Jogador
#
# E representado por um dicionario. Contem 4 chaves: 'nome' contem o nome do
# jogador; 'pontos' contem a pontuacao; 'validas' contem o conjunto de palavras
# validas sugeridas pelo jogador; 'invalidas contem o conjunto de palavras
# invalidas.
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #

def cria_jogador(string):
    """Cria um TAD Jogador com um dado nome.

    Args:
        nome (str)

    Levanta:
        ValueError: Caso `nome` nao for do tipo str.

    Retorna:
        TAD Jogador: Representa jogador chamado `nome`.
    """

    if type(string) != str:
        raise ValueError('cria_jogador:argumento invalido.')

    return {
        'nome':         string,
        'pontos':       0,
        'validas':      cria_conjunto_palavras(),
        'invalidas':    cria_conjunto_palavras()
    }

def jogador_nome(jogador):
    """Obtem nome dum Jogador.

    Args:
        jogador (TAD Jogador)

    Retorna:
        string: Nome de `jogador`.
    """

    return jogador['nome']

def jogador_pontuacao(jogador):
    """Obtem a pontuacao dum Jogador.

    Args:
        jogador (TAD Jogador)

    Retorna:
        int: Pontos de `jogador`.
    """

    return jogador['pontos']

def jogador_palavras_validas(jogador):
    """Obtem o conjunto de palavras validas dum Jogador.

    Args:
        jogador (TAD Jogador)

    Retorna:
        TAD conjunto_palavras: Palavras validas de `jogador`.
    """

    return jogador['validas']

def jogador_palavras_invalidas(jogador):
    """Obtem o conjunto de palavras invalidas dum Jogador.

    Args:
        jogador (TAD Jogador)

    Retorna:
        TAD conjunto_palavras: Palavras invalidas de `jogador`.
    """

    return jogador['invalidas']

def adiciona_palavra_valida(jogador, pp):
    """Adiciona uma palavra valida a um Jogador e atribui pontuacao
    correspondente.

    Args:
        jogador (TAD Jogador)
        pp (TAD palavra_potencial)

    Levanta:
        ValueError: Caso `jogador` nao for um TAD jogador ou `pp` nao for um
            TAD palavra_potencial.
    """

    # Verifica tipo dos argumentos
    if not e_jogador(jogador) or not e_palavra_potencial(pp):
        raise ValueError("adiciona_palavra_valida:argumentos invalidos.")

    cp_validas = jogador_palavras_validas(jogador)

    # Verifica se ja foi previamente adicionada
    if not conjunto_palavras_contem(cp_validas, pp):
        acrescenta_palavra(cp_validas, pp)
        jogador['pontos'] += palavra_tamanho(pp)

def adiciona_palavra_invalida(jogador, pp):
    """Adiciona uma palavra invalida a um Jogador e atribui pontuacao
    correspondente.

    Args:
        jogador (TAD Jogador)
        pp (TAD palavra_potencial)

    Levanta:
        ValueError: Caso `jogador` nao for um TAD jogador ou `pp` nao for um
            TAD palavra_potencial.
    """

    # Verifica tipo dos argumentos
    if not e_jogador(jogador) or not e_palavra_potencial(pp):
        raise ValueError("adiciona_palavra_invalida:argumentos invalidos.")

    cp_invalidas = jogador_palavras_invalidas(jogador)

    # Verifica se ja foi previamente adicionada
    if not conjunto_palavras_contem(cp_invalidas, pp):
        acrescenta_palavra(cp_invalidas, pp)
        jogador['pontos'] -= palavra_tamanho(pp)

def e_jogador(universal):
    """Verifica se o argumento e um Jogador.

    Args:
        universal (object)

    Retorna:
        bool: True caso `universal` for um TAD Jogador. False caso o contrario.
    """

    # Verifica o tipo
    if type(universal) != dict:
        return False

    dicio       = universal
    keys        = ('nome', 'pontos', 'validas', 'invalidas')

    # Verifica a estrutura do dicionario
    if sorted(dicio.keys()) != sorted(keys):
        return False

    # Verifica os tipos de dados

    if type(dicio['nome']) != str:
        return False

    if type(dicio['pontos']) != int:
        return False

    if not e_conjunto_palavras(dicio['validas']):
        return False

    if not e_conjunto_palavras(dicio['invalidas']):
        return False

    return True

def jogador_para_cadeia(jogador):
    """Representa um Jogador numa cadeia de caracteres.

    Args:
        jogador (Jogador)

    Retorna:
        str: Representacao de `jogador`.
    """

    cp_validas    = jogador_palavras_validas(jogador)
    cp_invalidas  = jogador_palavras_invalidas(jogador)

    nome        = 'JOGADOR '    + jogador_nome(jogador)
    pontos      = 'PONTOS='     + str( jogador_pontuacao(jogador) )
    validas     = 'VALIDAS='    + conjunto_palavras_para_cadeia(cp_validas)
    invalidas   = 'INVALIDAS='  + conjunto_palavras_para_cadeia(cp_invalidas)

    return ' '.join( (nome, pontos, validas, invalidas) )

def gera_todas_palavras_validas(tuplo_letras):
    """Gera um conjunto de palavras validas dado um conjunto de letras.

    Args:
        tuplo_letras (tuple)

    Retorna:
        TAD conjunto_palavras: Contem todas as palavra_potencial que representem
            palavras validas usando apenas as letras disponiveis em
            `tuplo_letras`.
    """

    cp = cria_conjunto_palavras()

    # Para todos os tamanhos possiveis
    for tamanho in range(1, len(tuplo_letras) + 1):

        # Para todas as permutacoes com esse tamanho
        for conjunto in permutacoes(tuplo_letras, tamanho):

            # Gera uma cadeia de caracteres
            possivel = ''.join(conjunto)

            # Guarda se for uma palavra valida
            if e_palavra(possivel):
                nova_pp = cria_palavra_potencial(possivel, tuplo_letras)
                acrescenta_palavra(cp, nova_pp)

    return cp

def guru_mj(tuplo_letras):
    """Inicializa o jogo Palavra Guru MultiJogador com um conjunto de letras
    a usar na formacao das palavras.
    """

    def bem_vindo(letras):

        print('Descubra todas as palavras geradas a partir das letras:')
        print(letras)

    def obter_jogadores():

        jogadores = []

        print ('Introduza o nome dos jogadores (-1 para terminar)...')

        for n in contar_apartir(1):

            nome = input('JOGADOR ' + str(n) + ' -> ')

            # Condicao de paragem da introducao de jogadores
            if nome == '-1':
                break

            jogadores.append( cria_jogador(nome) )

        return jogadores

    def ciclo_jogo(jogadores):

        cp_validas      = gera_todas_palavras_validas(tuplo_letras)
        numero_todas    = numero_palavras(cp_validas)

        cp_acertadas    = cria_conjunto_palavras()

        for jogada in contar_apartir(1):

            numero_acertadas = numero_palavras(cp_acertadas)

            # Se todas as palavras validas foram adivinhadas termina o ciclo
            if numero_acertadas >= numero_todas:
                break

            em_falta    = numero_todas - numero_acertadas
            msg_jogada  = 'JOGADA ' + str(jogada) + ' - ' +\
                'Falta descobrir ' + str(em_falta) + ' palavras'

            # Mensagem de informacao sobre a jogada
            print(msg_jogada)

            # Determina o jogador desta jogada
            jogador = jogadores[ (jogada - 1) % len(jogadores) ]

            # Obtem palavra tentada
            tentativa = input('JOGADOR ' + jogador_nome(jogador) + ' -> ')

            pp = cria_palavra_potencial(tentativa, tuplo_letras)

            if conjunto_palavras_contem(cp_validas, pp):

                print(tentativa + ' - palavra VALIDA')

                # Verifica se a palavra e nova no jogo
                if not conjunto_palavras_contem(cp_acertadas, pp):

                    acrescenta_palavra(cp_acertadas, pp)
                    adiciona_palavra_valida(jogador, pp)

            else:

                print(tentativa + ' - palavra INVALIDA')

                adiciona_palavra_invalida(jogador, pp)

    def estado_final(jogadores):

        def vitoria(jogador):

            pontos  = str(jogador_pontuacao(jogador))
            nome    = jogador_nome(jogador)

            msg = 'FIM DE JOGO! O jogo terminou com a vitoria do jogador ' +\
                nome + ' com ' + pontos + ' pontos.'

            print(msg)

        if len(jogadores) == 1:

            # Como so ha um jogador, ele e o proprio vencedor
            vitoria(jogadores[0])

        else:

            # Determina os pontos do primeiro jogador
            pontos_1 = jogador_pontuacao(jogadores[0])

            # Verifica se os pontos de todos os jogadores sao iguais
            empate = all(
                jogador_pontuacao(j) == pontos_1 for j in jogadores[1:]
            )

            if empate:

                print('FIM DE JOGO! O jogo terminou em empate.')

            else:

                # Obtem o jogador com maior pontuacao
                vencedor = max(jogadores, key = lambda j: jogador_pontuacao(j))

                vitoria(vencedor)

    def estado_jogadores(jogadores):

        for j in jogadores:
            print( jogador_para_cadeia(j) )

    # Mensagem de boas vindas
    bem_vindo(tuplo_letras)

    # Introducao dos jogadores
    jogadores = obter_jogadores()

    # Inicia o mecanismo central do jogo
    ciclo_jogo(jogadores)

    # Mostra o estado final do jogo
    estado_final(jogadores)

    # Mostra o estado final dos jogadores
    estado_jogadores(jogadores)