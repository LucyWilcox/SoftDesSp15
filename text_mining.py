"""


"""
import string
from pattern.web import *
from pattern.en import *

#the_picture_of_grey = URL('https://www.gutenberg.org/cache/epub/174/pg174.txt').download()
the_picture_of_grey = URL('http://www.gutenberg.lib.md.us/1/7/174/174.txt').download()
#the_picture_of_grey = open('kamasutra.txt')
#print the_picture_of_grey
#print len(the_picture_of_grey)
#print sentiment(the_picture_of_grey)
# def text_processing(book):
#     all_words = []
#     for line in book:
#         #words = line.strip()
#         all_words.append(line)
#     return all_words

def book_to_list(book):
    words = book.split()
    all_words = []
    for word in words:
        all_words.append(word)
    return all_words
# allwords = [word for word in words]


def strip_book(all_words):
    indices = [i for i, s in enumerate(all_words) if '***' in s]
    print indices[1]
    print indices[2]
    loop_len = len(all_words)
    i = 0
    #print all_words
    for i in range(0, 2):
        print i
        all_words.pop(i)
        print all_words[i]
        print all_words
    # for i in range(indices[2], len(all_words)- (loop_len - indices[2])):
    #     all_words.pop(i)
    #     i += 1
    return all_words

#the_picture_of_grey = text_processing(the_picture_of_grey)
all_words = book_to_list(the_picture_of_grey)
words = strip_book(all_words)
#print all_words
#print words

#names = open('class_names.txt')
# name_sentiment = []

# g = Bing()
# for name in names:
#   for result in g.search(name):
#       text = result.text.encode('utf8')
#       print text
#       name_sentiment[result] = sentiment(text)

#   print sentiment(text)

