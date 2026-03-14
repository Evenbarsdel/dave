"""
Dans cete fontion la nouvelle chose est de voir si la phrase est une question , elle est ecrite en majuscule et si il des espace ou si c'est ecrit en majuxcule et c'est une question 

.isupper: c'est pour voir si c'est ecrit en majuscule 
.endswith : c'est pour voir si il y a un ? a la fin donc voir si c'est une question

Dans cette fonction la place des conditions est importante car il est important de verifier d'abord si c'est ecrit en majuscule et qu'il y a un point d'interrogation avant de les verrifier seule

"""  

def response(hey_bob):
    hey_bob = hey_bob.strip() 

    
    if hey_bob == "":
        return "Fine. Be that way!"
    elif hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.endswith("?"):
        return "Sure."
    else:
        return "Whatever."

        pass
