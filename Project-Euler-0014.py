#We will use a dictionary
dict = {}
#Loop until max
for i in range(2,1000000):
    #create a value and list for this loop
    x = i
    lst = []
    #create the sequence
    while x > 1:
        lst.append(x)
        #if the value is in our dictionary we can use it to end the sequence here
        if x in dict:
            dict[i] = len(lst) + dict[x]-1
            break
        #otherwise continue the sequence
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
    else:
        #once the sequence ends, we add the original value and the sequence length to our dictionary
        lst.append(1)
        dict[i] = len(lst)
#this will find the key of the max value
print(max(dict, key=dict.get))
#expected value:837799