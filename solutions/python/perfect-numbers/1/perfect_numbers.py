def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    #cette fonction vérifie si un nombre est un nombre parfit abondant ou deficient avec des comparaison
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
 
    some = 0
    for i in range(1,number):
        if number % i == 0:
            some += i
            
    if some == number:
        return"perfect"
    elif some > number:
        return "abundant"
    else:
        return "deficient"
        
    
    pass
