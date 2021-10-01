def calculateGCD(x,y): 
    if (x%y) == 0:
        return y
    else:
        return calculate GCD(y, x%y)
  

print ("GCD is ",calculateGCD(80,12)) 
