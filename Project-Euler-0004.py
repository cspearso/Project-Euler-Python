#palindrome check
def is_palindrome(number):
    text = str(number)
    reverse = text[::-1]
    if reverse == text:
        return True
    else:
        return False
#iterate over all possible products and add to list
palindromes = []
for i in range(1000):
    for j in range(1000):
        if is_palindrome(i*j):
            palindromes.append(i*j)
#find the largest palindrome
print (max(palindromes))
#expected value: 906609