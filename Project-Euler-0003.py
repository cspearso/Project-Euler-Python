#number from which to find largest prime factor and list of prime factors
number = 600851475143
prime_factors = []

#loop from 2 to number; if a prime factor is found, add to the list, divide and start over
i = 2
while i <= number:
    if number % i == 0:
        number /= i
        prime_factors.append(i)
        i = 1
    i+=1
#list now contains all prime factors, including frequency, use max to find largest
print (prime_factors)
print (max(prime_factors))
#expected value: 6857

