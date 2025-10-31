# function to return number of vowels
def count_vowels(word):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for c in word.lower():
        if c in vowels:
            vowels[c] = vowels[c] +1

    return vowels

print(count_vowels('I should gIvE this a quIck tEst'))
