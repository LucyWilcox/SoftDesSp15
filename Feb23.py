def hawaiian(s):
	#hawaiian_alphebet = ["A", "K", "O", "I"]
	hawaiian_alphebet = {"A": 1, "K":2, "O": 3, "I":4}
	score = 0
	for c in s:
		if c not in hawaiian_alphebet.keys():
			return -1
		else:
			score = score + hawaiian_alphebet[c]
	return score

print hawaiian("CA")