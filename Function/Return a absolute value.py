def distance_from_zero(x):
    if type(x)==int or type(x)==float:
        return abs(x)
    else:
        return "Nope"
x=distance_from_zero(-5.6)
print(x)   
