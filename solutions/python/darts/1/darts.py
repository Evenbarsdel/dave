import math

def score(x, y):
   #cacul de la distance 

    d = math.sqrt(x**2 + y**2)

    if d > 10:
        return 0
    elif d > 5:
        return 1
    elif d > 1:
        return 5
    else:
        return 10
    
    
    pass
