#!/usr/bin/python

# generate strings that are rotationally symmetrical

ambigram_characters = { 'H':'H', 'M':'W', 'N':'N', 'S':'S', 'W':'M', 'X':'X', 'Z':'Z', '6':'9', '8':'8', '9':'9' };

palindrome_characters = { 'H', 'N', 'S', 'X', 'Z', '8' }

# 3-character ambigrams

for a,a1 in ambigram_characters.iteritems():
	for b in palindrome_characters:
		name = a
		name += b
		name += a1
		print name


# 5-character ambigrams

for a,a1 in ambigram_characters.iteritems():
	for b,b1 in ambigram_characters.iteritems():
		for c in palindrome_characters:
			name = a
			name += b
			name += c
			name += b1
			name += a1
			print name
