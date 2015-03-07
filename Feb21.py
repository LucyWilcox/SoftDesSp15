import string
from pattern.web import *
from pattern.en import *



#fin = open('words.txt')
#book = open('kamasutra.txt')
book = URL('http://www.gutenberg.lib.md.us/1/7/174/174.txt').download()
#fin.strip()
#string.translate(fin)

def text_processing(book):
	for line in book:
		word = line.strip()

	print book.readline()
	#print book

text_processing(book)

def has_no_e(words):
	e = 0
	no_e = 0
	for word in words:
		if 'e' not in word:
			no_e += 1
			print word
	 	else:
	 		e += 1

	total = e + no_e
	print 'percentage with e is', float(e)/total * 100
	print 'percentage without e is', float(no_e)/total * 100


#has_no_e(['cabbage', 'who', 'yeah', 'hey', 'dont', 'why'])
def avoids(word, forbidden):
	for letter in word:
		if letter in forbidden:
			return False
	return True

#print avoids('cabbage', ['t', 'j', 'k'])

def is_abecedarian(word):
	previous = word[0]
	for c in word:
		if c < previous:
			return False
		previous = c
	return True

# for line in fin:
# 	word = line.strip()
# 	if len(word) > 20:
# 		print word

#print fin.readline()

# def is_palindrome(word):
# 	i = 0
# 	j = len(word) - 1

# 	while i < j:
# 		if word[i] != word[j]:
# 			return False
# 		i += 1
# 		j -= 1
# 	return True

# for line in fin:
# 	word = line.strip()
# 	if is_palindrome(word) == True:
# 		print word

