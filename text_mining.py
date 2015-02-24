"""A Sentiment Analysis of Gothic Fiction:
This program calls a list of book from a Project Gutenburg
Mirror site and analyzies their sentiment over the span of the
book and plots it.
"""

import string
from pattern.web import *
from pattern.en import *
import matplotlib.pyplot as plt


def book_to_list(book):
    """Takes the book and breaks it into a list of words
    book: string
    returns: list of strings
    """
    words = book.split()
    return words


def remove_gute(book):
    """Removes Project Gutenburg header and footer from project gutenberg books.
    book: list of strings
    returns: 
    """
    indices = [i for i, s in enumerate(book) if '***' in s]
    start = indices[1] + 1
    end = indices[2]  
    book = book[start:end]
    return book
 

def split_to_parts(book):
    """Splits book into five parts
    book: a list of all words in the book
    returns: a list of 5 lists containing segments of the book 
    """
    segment_len = len(book) / 5
    segment_list = []
    for i in range(0, 5):
        segment_list.append(book[i * segment_len: (i + 1) * segment_len])

    return segment_list


def group_to_string(list_of_words):
    """Turns list of words in a single string of text (with punctuation
    and everything) so it can later be analyzed for sentiment.
    list_of_words: a list of lists of words
    returns: a list of 5 strings
    """
    book_strings = []
    for i in range(0, 5):
        book_strings.append(" ".join(list_of_words[i]))

    return book_strings


def get_sentiment(five_strings):
    """Takes the book which is split into five segments and finds sentiment
    five_strings: list of five string
    returns: list containing the sentiment of each segment
    """
    sentiment_list = []
    for i in range(0, 5):
        sentiment_list.append(sentiment(five_strings[i]))
    sentiment_list =  [x[0] for x in sentiment_list]
    return sentiment_list


def all_sentiments():
    """Loops through each book, calls previous functions on it, heart of data mining code
    returns: list of list of sentiments for each segment of each book
    """
    the_picture_of_dorian_grey = URL('http://www.gutenberg.lib.md.us/1/7/174/174.txt').download()
    the_yellow_wallpaper = URL('http://www.gutenberg.lib.md.us/1/9/5/1952/1952.txt').download()
    frankenstein = URL('http://www.gutenberg.lib.md.us/8/84/84.txt').download()
    turn_of_the_screw = URL('http://www.gutenberg.lib.md.us/2/0/209/209.txt').download()
    dracula = URL('http://www.gutenberg.lib.md.us/3/4/345/345.txt').download()

    books = [
    the_picture_of_dorian_grey,
    the_yellow_wallpaper,
    frankenstein,
    turn_of_the_screw,
    dracula
    ]

    sentiment_list = []

    for i in range(len(books)):
        book = books[i]
        all_words = book_to_list(book)
        words = remove_gute(all_words)
        five_lists = split_to_parts(words)
        five_strings = group_to_string(five_lists)
        sentiments = get_sentiment(five_strings)
        sentiment_list.append(sentiments)
    return sentiment_list


def plot_sentiments(sentiments):
    """Plots sentiments of all books
    sentiments: list of list of the sentiment for each
        segment of each book
    """
    plt.plot(
        x, sentiments[0], 'r',
        x, sentiments[1], 'g',
        x, sentiments[2], 'b',
        x, sentiments[3], 'k',
        x, sentiments[4], 'm'
        )
    plt.axis([0, 6, 0, 0.25])
    plt.title("Change of Sentiments Over Text")
    plt.ylabel("sentiment")
    plt.xlabel("segment of text")
    plt.show()

sentiments = all_sentiments()
plot_sentiments(sentiments)