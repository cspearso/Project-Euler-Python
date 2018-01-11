#loop until largest value reaches sum value
test = False
for i in range(1000):
    #other two variables loop until largest value
    for j in range(1,i):
        for k in range(1,j):
            #is the set meets conditions, print and end loops
            if j**2 + k**2 == i**2 and i + j + k == 1000:
                test = True
                print (i*j*k)
                break
            if test == True:
                break
    if test == True:
        break

#expected value: 31875000
#runs a little slow