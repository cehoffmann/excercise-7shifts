import re

def Add(args=""):
    res = 0
    negativeArray = []
    
    cleanArray = re.findall("(-?\d+)", args)
    if  not cleanArray:
        raise ValueError("You haven't entered any valid numbers.")
    
    for n in cleanArray:
        n = int(n)
        if n < 0:
            negativeArray.append(n)
        elif n <= 1000:
            res += n
    
    # Check if no negative numbers were found, if there were throws exception and lists negatives
    if negativeArray:
        exceptionReturn = ", ".join(str(x) for x in negativeArray)
        raise ValueError("Negative numbers are not allowed. " + exceptionReturn)
    
    return res
