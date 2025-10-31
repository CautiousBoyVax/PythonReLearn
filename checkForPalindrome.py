#function that returns if the word is a palindrome

def pal(word):
    return word == word[::-1]

p = pal('tom')
print (p)