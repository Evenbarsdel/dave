""" Cecalcul est pour calculer le nombre de grain sur case et son total.
C'est en rapport avec les puissances comment calculer une puissance en fonction d'un nombre donné def square(number)
et la somme des puissances def total()

"""


def square(number):
    
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    return  2**(number -1) 
    pass


def total():
    total = 0
    for i in range (1,65):
        total +=  2**(i-1)
    return total    
    pass
