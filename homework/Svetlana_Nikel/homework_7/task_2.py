words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def print_words(word):
    for key, valye in word.items():
        print(key * valye)


print_words(words)
