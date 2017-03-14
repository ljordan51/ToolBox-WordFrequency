""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip(string.whitespace)
    lines = ' '.join(lines)
    lines = lines[lines.find('THE ADVENTURES  OF  HUCKLEBERRY FINN  (T'):]
    words = lines.split()
    for i in range(len(words)):
        words[i] = words[i].lower()
        words[i] = words[i].strip(string.punctuation)
        words[i] = words[i].replace("'s", '')
    return words


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    word_dict = {}
    for word in word_list:
        word_dict[word] = word_dict.get(word, 0) + 1
    ordered_by_frequency = sorted(word_dict, key=word_dict.get, reverse=True)
    return ordered_by_frequency[:n]


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    word_list = get_word_list('pg32325.txt')
    print(get_top_n_words(word_list, 100))
