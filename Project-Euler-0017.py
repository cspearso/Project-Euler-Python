#dictionaries will be useful for this problem
#create a dictionary that contains values for 1-19 (10-19 are exceptions), 20, 30, 40, 50, 60, 70, 80, 90 and 1000
numbers = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',
           10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
           20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety', 1000:'onethousand'}
#add values less than 100
for i in range(20,100):
    if i % 10 != 0:
        numbers[i] = numbers[int(i/10)*10] + numbers[i%10]
#add multiples of 100
for i in range(1,10):
    numbers[i*100] = numbers[i]+'hundred'
#add the missing values
for i in range(101,1000):
    if i % 100 != 0:
        numbers[i] = numbers[int(i/100)*100]+'and'+numbers[i - int(i/100)*100]
#now sum the lengths of all the strings in our dictionary
sum = 0
for i in numbers:
    sum += len(numbers[i])
print (sum)
#expected value:21124