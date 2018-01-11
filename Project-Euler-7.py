#check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
                break
        else:
            return True
#create loop value, prime counter, and desired prime number
i = 0
prime_count = 0
desired_prime = 10001
#loop while adding to loop value, and prime counter if it is prime
while  prime_count < desired_prime:
    if is_prime(i):
        prime_count +=1
    i += 1
#most recent value of i minus 1 will be the desired prime number
print(i-1)
#expected value:104743
#runs slow