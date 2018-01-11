#initial conditions
x = 100
sum_square = 0
square_sum = 0
#create sum of squares, and regular sum
for i in range(1,x+1):
    sum_square += i**2
    square_sum += i
#square the regular sum and find the difference
print (square_sum**2 - sum_square)
#expected value:25164150