"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return "un" + word
    pass


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]

    word_prefix =[prefix + word for word in vocab_words[1:]]
    return " :: ".join([prefix] + word_prefix) 

    pass


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    root = word[:-4] #enleve les 4 derniere lettre du mot donc le suffixe ness
    
    """
    root.endswith("i"): verifie si le mot se termine par i
    root[-2] not in "aieou": verifie que la lettre avant le i est un consonne 
    len(root) > 1 permet de verifier que le mot a au moin deux caractère 
    """
    if root.endswith("i") and len(root) > 1 and root[-2] not in "aieou":
        root = root[:-1] + "y"
    return root  
    
    pass


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    #On decoupe la phrase en mot avec .split()
    word = sentence.split()

    #On recupere le mot a l'index donner 
    word = word[index]

    #On enleve les ponctuation avec .strip("!.?,")
    word = word.strip("?!.,")

    #Et on ajoute le suffixe 
    return word + "en"
      

    pass
