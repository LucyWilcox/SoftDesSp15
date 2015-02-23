""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import string
from pattern.web import *
from pattern.en import *
book = URL('http://www.gutenberg.lib.md.us/1/7/174/174.txt').download()


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    f = open(file_name,'r')
    prnc= string.punctuation.split()
    punc =  [i for i, s in prnc]
    print punc
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]

    for line in lines:
        words = string.split(line)
        #print words
        # for word in words:
        #     if word in punc:

            # for c in word:
            #     c.replace(string.punctuation, "")

    return words
    pass

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    pass

print get_word_list("kamasutra.txt")