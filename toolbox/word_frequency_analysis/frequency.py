""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import string

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    f = open(file_name,'r')
    punctuation = string.punctuation
    count = dict()
    all_words = []
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]

    for line in lines:
        words_in_line = string.split(line)
        for word in words_in_line:
            word = word.lower()
            for char in punctuation:
                word = word.replace(char, "")
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    return count


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    sort = sorted(word_list, key = word_list.get, reverse = True)
    return sort[:n]


counts = get_word_list("kamasutra.txt")
print get_top_n_words(counts, 100)