import math

def euclidianGCD(A: int, B: int):
  
  numArray = [A, B]
  
  if A > B:
    numArray = [B, A]
    
  print(math.gcd(numArray[1] % numArray[0], numArray[0]))

euclidianGCD(510, 646)
