#we could import math to get factorial but...
def factorial(x):
    if x == 0:
        return 1
    elif x < 0 or int(x) != x:
        return "That's beyond the scope of this simplified factorial function, use the gamma function"
    
    fact = 1
    while x > 0:
        fact *= x
        x -= 1
    else:
        return fact
#we convert the number to str, then iterate, summing the parts
sum = 0
for i in str(factorial(100)):
    sum += int(i)
print (sum)
#expected value: 648