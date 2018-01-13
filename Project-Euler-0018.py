#for this problem we want to calculate from the bottom up
#we check both paths for the second to last row, eliminating the lesser one
#and replacing the second to last row with the value of the greater path
#now the second to last row is the last row, and we can repeat until we reach the top
test =[
[75],
[95, 64],
[17, 47, 82],
[18,35,87,10],
[20, 4,82,47,65],
[19, 1,23,75, 3,34],
[88, 2,77,73, 7,63,67],
[99,65, 4,28, 6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
[ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23]
]

#iterate from the second to last up
for i in range(len(test)-1)[::-1]:
    for j in range(len(test[i])):
        # check which path is greater and chose it
        if test[i+1][j] > test[i+1][j+1]:
            test[i][j] += test[i+1][j]
        else:
            test[i][j] += test[i+1][j+1]
#the item in the top of the pyramid is the result
print(test[0][0])
#expected value:1074