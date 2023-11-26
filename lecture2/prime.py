from math import isqrt

def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

for i in range(101):
  if is_prime(i):
    print(str(i)+" IS a prime")
  else:
    print(str(i)+" IS NOT a prime")
