#initial condition
sum = 0
#sum
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        
print (sum)
#expected value: 233168