
def wordPerms(word):
    """ wordPerms --- 
    Returns all the permutations of a string. 
    -- input: a string.
    -- output: an array containing all the permutations
    """
    from itertools import permutations
    perms = [''.join(p) for p in permutations(word)]
    return(perms)

def dictSearch(perms):
    """ dictSearch --- 
    searches permutations of a word in a spanish dictionary. 
    -- input: a list with all the permutations of a word.
    -- output: a set with all the words in the dictionary.
    """
    import unidecode
    # lista de palabras: 
    with open("espanol.txt") as word_file:
        spanish_words = set(word.strip().lower() for word in word_file)
    
    diccionario = set()
    
    # quitar los acentos del diccionario: 
    for i in list(spanish_words):
        w = unidecode.unidecode(i)
        diccionario.add(w)
        
    Perms = set(perms)
    return Perms.intersection(diccionario)
    