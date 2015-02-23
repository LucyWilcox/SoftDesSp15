"""


"""
import string
from pattern.web import *
from pattern.en import *

the_picture_of_dorian_grey = URL('http://www.gutenberg.lib.md.us/1/7/174/174.txt').download()
the_yellow_wallpaper = URL('http://www.gutenberg.lib.md.us/1/9/5/1952/1952.txt').download()
frankenstein = URL('http://www.gutenberg.lib.md.us/8/84/84.txt').download()
turn_of_the_screw = URL('http://www.gutenberg.lib.md.us/2/0/209/209.txt').download()
dracula = URL('http://www.gutenberg.lib.md.us/3/4/345/345.txt').download()
book = dracula

#print sentiment(the_picture_of_grey)
# def text_processing(book):
#     all_words = []
#     for line in book:
#         #words = line.strip()
#         all_words.append(line)
#     return all_words

def book_to_list(book):
    """

    """
    words = book.split()
    return words


def remove_gute(book):
    """Removes header and footer from project gutenberg books.
    book: list of strings
    returns: 
    """
    indices = [i for i, s in enumerate(book) if '***' in s]
    start = indices[1] + 1
    end = indices[2]  
    book = book[start:end]
    return book
 

def split_to_parts(book):
    """

    """
    segment_len = len(book) / 5
    segment_list = []
    for i in range(0, 5):
        segment_list.append(book[i * segment_len: (i + 1) * segment_len])

    return segment_list

    # segment_1 = book[0:segment_len]
    # segment_2 = book[segment_len: 2 * segment_len]
    # segment_3 = book[2 * segment_len: 3 * segment_len]
    # segment_4 = book[3 * segment_len: segment_len *4]
    # segment_5 = book[4* segment_len:]


def group_to_string(list_of_words):
    """

    """
    book_strings = []
    for i in range(0, 5):
        book_strings.append(" ".join(list_of_words[i]))

    return book_strings

def get_sentiment(five_strings):
    """

    """
    sentiment_list = []
    for i in range(0, 5):
        sentiment_list.append(sentiment(five_strings[i]))
    sentiment_list =  [x[0] for x in sentiment_list]
    return sentiment_list


all_words = book_to_list(book)
words = remove_gute(all_words)
five_lists = split_to_parts(words)
five_strings = group_to_string(five_lists)
sentiments = get_sentiment(five_strings)
print sentiments

#names = open('class_names.txt')
# name_sentiment = []

# g = Bing()
# for name in names:
#   for result in g.search(name):
#       text = result.text.encode('utf8')
#       print text
#       name_sentiment[result] = sentiment(text)

#   print sentiment(text)

