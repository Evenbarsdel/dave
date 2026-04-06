def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower() # pour que la phrase soit insensiblea a case 
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True

    pass
