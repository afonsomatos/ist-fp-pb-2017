# 90699 - Afonso Luis de Freitas Matos

def juntar_tuplos(t1, t2):
    """Aplica concatenacao distributiva entre dois tuplos

    Args:
        t1 (tuple): Primeiro tuplo.
        t2 (tuple): Segundo tuplo.

    Retorna:
        tuple: Conjunto de todos os valores do primeiro tuplo, concatenados com
            todos os valores do segundo tuplo.

    Exemplos:
        >>> juntar_tuplos(('X', 'Y'), ('Z',))
        ('XZ', 'YZ')
        >>> juntar_tuplos(('A', 'B'), ('C', 'D'))
        ('AC', 'AD', 'BC', 'BD')
    """

    t3 = ()

    for x1 in t1:
        for x2 in t2:
            t3 += (x1 + x2,)

    return t3

def juntar_tuplo_str(tuplo, string):
    """Concatena uma string a todos os elementos dum tuplo

    Args:
        tuplo (tuple)
        string (str)

    Retorna:
        tuple: Conjunto de todos os elementos de `tuplo` concatenados com
            `string`

    Exemplos:
        >>> juntar_tuplo_str(('X', 'Y'), 'H')
        ('XH', 'YH')
        >>> juntar_tuplo_str(('A',), 'B')
        ('AB',)
    """

    return juntar_tuplos(tuplo, (string,))

# Definicao de tuplos auxiliares
artigo_def      = ('A', 'O')
vogal_palavra   = artigo_def + ('E',)
vogal           = ('I', 'U') + vogal_palavra

ditongo_palavra = ('AI', 'AO', 'EU', 'OU')
ditongo         = ('AE', 'AU', 'EI', 'OE', 'OI', 'IU') + ditongo_palavra
par_vogais      = ditongo + ('IA', 'IO')

consoante_freq      = ('D', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V')
consoante_terminal  = ('L', 'M', 'R', 'S', 'X', 'Z')
consoante_final     = ('N', 'P') + consoante_terminal
consoante           = ('B', 'C', 'D', 'F', 'G', 'H',
                       'J', 'L', 'M', 'N', 'P', 'Q',
                       'R', 'S', 'T', 'V', 'X', 'Z')

par_consoantes = ('BR', 'CR', 'FR', 'GR', 'PR', 'TR', 'VR', 'BL', 'CL', 'FL', 'GL', 'PL')

monossilabo_2 = ('AR', 'IR', 'EM', 'UM')                +\
                juntar_tuplo_str(vogal_palavra, 'S')    +\
                ditongo_palavra                         +\
                juntar_tuplos(consoante_freq, vogal)

monossilabo_3 = juntar_tuplos( juntar_tuplos(consoante, vogal) , consoante_terminal)    +\
                juntar_tuplos(consoante, ditongo)                                       +\
                juntar_tuplos(par_vogais, consoante_terminal)

monossilabo = vogal_palavra + monossilabo_2 + monossilabo_3

silaba_2 = par_vogais                               +\
           juntar_tuplos(consoante, vogal)          +\
           juntar_tuplos(vogal, consoante_final)

silaba_3 = ('QUA', 'QUE', 'QUI', 'GUE', 'GUI')                                  +\
           juntar_tuplo_str(vogal, 'NS')                                        +\
           juntar_tuplos(consoante, par_vogais)                                 +\
           juntar_tuplos( juntar_tuplos(consoante, vogal) , consoante_final)    +\
           juntar_tuplos(par_vogais, consoante_final)                           +\
           juntar_tuplos(par_consoantes, vogal)

silaba_4 = juntar_tuplo_str(par_vogais, 'NS')                                       +\
           juntar_tuplo_str( juntar_tuplos(consoante, vogal) , 'NS')                +\
           juntar_tuplo_str( juntar_tuplos(consoante, vogal), 'IS')                 +\
           juntar_tuplos(par_consoantes, par_vogais)                                +\
           juntar_tuplos( juntar_tuplos(consoante, par_vogais) , consoante_final)

silaba_5 = juntar_tuplo_str( juntar_tuplos(par_consoantes, vogal), 'NS')

# Topo da cadeia de definicoes
silaba_final    = monossilabo_2 + monossilabo_3 + silaba_4 + silaba_5
silaba          = vogal + silaba_2 + silaba_3 + silaba_4 + silaba_5

def check_str(objeto, msgErro):
    """Verifica se um objeto e uma string

    Args:
        objeto (object): Objeto a verificar.
        msgErro (string): Mensagem de erro.

    Levanta:
        ValueError: Se `objeto` nao e uma string. Este erro contem a mensagem
            `msgErro`.

    """

    if type(objeto) != str:
        raise ValueError(msgErro)

def check_silabas(string):
    """Verifica se a string e uma cadeia de silabas

    Args:
        string (str): String para verificar.

    Retorna:
        bool: True se `string` for uma sequencia de silabas. False caso o
            contrario.
    """

    if string in silaba:
        # A string e valida porque toda ela e uma silaba
        return True

    # Tenta todas as sequencias possiveis de silabas
    for i in range(1, len(string)):

        # Verifica se os primeiros i caracteres formam uma silaba
        if string[:i] in silaba:

            # Verifica se os restantes caracteres sao uma cadeia de silabas
            if check_silabas(string[i:]):
                return True

    return False


def e_silaba(arg):
    """Verifica se um objeto e uma silaba

    Args:
        arg (object)

    Levanta:
        ValueError: Caso `arg` nao for uma string.

    Retorna:
        bool: True se `arg` for considerado uma silaba. False caso o contrario.
    """

    check_str(arg, 'e_silaba:argumento invalido')

    return arg in silaba

def e_monossilabo(arg):
    """Verifica se um objeto e um monossilabo

    Args:
        arg (object)

    Levanta:
        ValueError: Caso `arg` nao for uma string.

    Retorna:
        bool: True se `arg` for considerado um monossilabo. False caso o contrario.
    """

    check_str(arg, 'e_monossilabo:argumento invalido')

    return arg in monossilabo

def e_palavra(arg):
    """Verifica se um objeto e uma palavra

    Args:
        arg (object)

    Levanta:
        ValueError: Caso `arg` nao for uma string.

    Retorna:
        bool: True se `arg` for considerado uma palavra. False caso o contrario.
    """

    check_str(arg, 'e_palavra:argumento invalido')

    string = arg

    if e_monossilabo(string):
        return True

    if string in silaba_final:
        return True

    # Tenta todas as cadeias de silabas possiveis que acabam numa silaba final
    for i in range(len(string) - 1, 0, -1):

        # Verifica se a cadeia dos ultimos caracteres a partir de i forma uma silaba final
        if string[i:] in silaba_final:

            # Verifica se os restantes caracteres formam uma cadeia de silabas
            if check_silabas(string[:i]):
                return True

    return False