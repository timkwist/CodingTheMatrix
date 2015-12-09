# Author: Tim Kwist

# Given a list of strings (documents), returns a dictionary that maps earch word to the set consisting of the
# document numbers of documents in which that word appears.
def makeInverseIndex(strlist):
	dictionary = {}
	for (documentNumber, document) in enumerate(strlist):
		words = document.split()
		for word in words:
			if word in dictionary:
				dictionary[word] = dictionary[word] + [documentNumber]
			else:
				dictionary[word] = list({documentNumber})
	return dictionary

documents = ["one", "two", "one two"]
print makeInverseIndex(documents)
# Output: {'two': [1, 2], 'one': [0, 2]}