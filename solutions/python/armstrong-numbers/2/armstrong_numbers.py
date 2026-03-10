

def is_armstrong_number(number):
    """Dans cette fonction il S'agit de compter les nombre de chiffre qu'il y a dans un nombre
et en suite le transformer en chaine de carractere et compter ces chaine pour savoir combien il y 
a de de nombre on le fait avec 
    len(chaine): compte le nombre de caractere
    str(number): transforme en chaine de caractere
    
Et la suite du code est de faire la somme de cette chaine en les retransformant en int
On veut verrifier si un nombre est un nombre d Amstrong
"""
    chaine = str(number)

    somme = 0
    for chiffre in str(number):
        somme += int(chiffre)**len(chaine)
    return somme == number 
        
    pass
