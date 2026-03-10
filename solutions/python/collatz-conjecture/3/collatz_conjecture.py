def steps(number):
    """Cette fonction compte le nombre de fois que le nombre fait avant 
    d'arriver a 1
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    compteur = 0
    while number != 1 :
        if number % 2 == 0:
            number = number // 2
        else :
            number = (number *3) + 1
            
        compteur += 1      
    return compteur  
    
print(steps(12))