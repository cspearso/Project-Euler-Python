#initial conditions

value1 = 1
value2 = 2
result = 0
#iteration and sum
while value1 < 4000000:
    if value1 % 2 == 0:
        result += value1
    value2 += value1
    value1 = value2 - value1
    
print (result)
#expected result: 4613732