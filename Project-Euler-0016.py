#for this we will take the power, convert to string, then iterate to find the sum
x = 1000
string = str(2**x)

sum = 0
for i in string:
    sum += int(i)
    
print(sum)
#expected value:1366