#Write a Python function that takes a sentence and returns a dictionary showing how many times each word appears.

def count_words(sentence):
    output = {}
    # Remove punctuation
    for p in ".!?,;:":
        sentence = sentence.replace(p, "")
    # Normalize case and split into words
    words = sentence.lower().split()
    for word in words:
        output[word] = output.get(word, 0) + 1
    return output


print(count_words("the cat and the hat"))
# Output: {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}

