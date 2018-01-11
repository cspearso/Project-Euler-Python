#check if divisible by all values, where number is the test and divisor is the largest divisor
def is_divisible(number, divisor):
    for i in range(1,divisor+1):
        if number % i == 0:
            continue
        else:
            return False
            break
    else:
        return True    
#initial conditions
i = 1
divisor = 20
#go one by one until the number is found 
while not is_divisible(i,divisor):
    i += 1
else:
    print(i)
#expected value:232792560

#takes long time for 20 will take MUCH longer for high values