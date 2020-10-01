import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here


def markov(words):
    dic = {}
    words = words.split(' ')
    for i in range(0, len(words)-1):
        if words[i] in dic:
            dic[words[i]].append(words[i+1])
        else:
            dic[words[i]] = [words[i + 1]]
    start_not_found = True
    while start_not_found:
        start = random.choice(words)
        if start.isupper() or start[0] == '"':
            start_not_found = False

    next_word = start
    sentence = start
    stop_list = ['.', '?', '!', '."', '?"', '!"']
    stop_not_found = True
    while stop_not_found:
        next_word = random.choice(dic[next_word])
        if next_word[-1] in stop_list:
            sentence += ' ' + next_word
            stop_not_found = False
        else:
            sentence += ' ' + next_word
    print(sentence)
# TODO: construct 5 random sentences
# Your code here


for i in range(0, 5):
    markov(words)
