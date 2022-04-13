def print_upper_words(words):
    """ Prints each string that passes through, to uppercase""" 
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """Prints each string that passes through and uppercase the e in the string"""
    for word in words:
        if word.startswith('e') or word.startswith('E'):

            print(word.upper('e'))

def print_upper_words3(words, letters):
    """ Prints each word on another line with one of the given letters"""
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())