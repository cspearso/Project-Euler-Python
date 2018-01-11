#eulerlib is very useful for primes, and makes this problem trivial
import sys
sys.path.append("c:\\users\\conrad pearson\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages")
from eulerlib import primes

#primes provides a list of primes below a max value
#all we need to is take a sum of values below our max
print(sum(primes(2000000)))
#expected value: 142913828922




#dysfunctionally slow non-import method
'''primes = [2]
def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in primes:
            if x % i == 0:
                return False
        else:
            for i in range(max(primes),x):
                if x % i == 0:
                    return False
                    break
            else:
                primes.append(x)
                return True
                
for i in range(2000000):
    is_prime(i)
print(sum(primes))'''