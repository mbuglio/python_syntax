def print_upper_words(words):
    """ Print each word on a individual line, uppercased.
        >>> print_upper_words(['planets','are','amazing'])
    """

    for word in words:
        print(word.upper())


def print_upper_words_2(words):
    """Print words that start with upper or lowercase e only
    """
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_words_3(words,must_start_with):
    """print words that start with a letter of your choosing
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break