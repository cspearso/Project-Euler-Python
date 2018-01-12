import sys
sys.path.append("c:\\users\\conrad pearson\\appdata\\local\\programs\\python\\python36-32\\lib\\site-packages")
#eulerlib is useful for finding divisors
#but too slow on this scale
from eulerlib import Divisors
#this sets max value of which divisors can be found
div = Divisors(100000000)
#initialize our triangle number and other useful variables
triangle = 0
max_div = 0
i = 0
#iterate and find next triangle number until condition is met
while max_div < 500:
    i+=1
    triangle += i
    max_div = len(div.divisors(triangle))
 
print (triangle)
#expected value: 76576500