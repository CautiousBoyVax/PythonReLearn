# Write a function that finds the shortest transformation sequence from a start_word to an end_word, such that:

# - Only one letter can be changed at a time
# - Each transformed word must exist in a given word list
# - Return the sequence of words from start to end, or an empty list if no path exists

# start_word = "hit"
# end_word = "cog"
# word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

# word_ladder(start_word, end_word, word_list)
# Output: ['hit', 'hot', 'dot', 'dog', 'cog']

start_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

def get_neighbors(word, word_list):
    # Returns True if the words differ by exactly one letter
    neighbors = []
    for candidate in word_list:
        if len(candidate) != len(word):
            continue

        diff_count = 0
        for w1,w2 in zip(word,candidate):
            if w1 != w2:
                diff_count +=1
        if diff_count == 1:
            neighbors.append(candidate)
    return neighbors

def word_ladder(start, end, word_list):
    from collections import deque

    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        current_word, path = queue.popleft()
        if current_word == end:
            return path
        visited.add(current_word)
        for neighbor in get_neighbors(current_word, word_list):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    return []

print(word_ladder("hit", "cog", word_list))

