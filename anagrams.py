# Write a function that takes a list of words and groups them into lists of anagrams.

# group_anagrams(["listen", "silent", "enlist", "rat", "tar", "art", "evil", "vile", "live"])

# [
#   ["listen", "silent", "enlist"],
#   ["rat", "tar", "art"],
#   ["evil", "vile", "live"]
# ]

def group_anagrams(dict):
    output = {}
    for word in dict:
        sorted_chars = sorted(word)
        sorted_word = "".join(sorted_chars)
        if sorted_word not in output:
            output[sorted_word] = []
        output[sorted_word].append(word)

    return output
#makes the ouput a little easier to add the list formatting to in print
result = group_anagrams(["listen", "silent", "enlist", "rat", "tar", "art", "evil", "vile", "live"])
#force output as a list
print(list(result.values()))