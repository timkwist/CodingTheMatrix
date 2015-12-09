# Author: Tim Kwist

# Given a list of strings (documents), returns a dictionary that maps earch word to the set consisting of the
# document numbers of documents in which that word appears.
def makeInverseIndex(strlist):
	dictionary = {}
	for (documentNumber, document) in enumerate(strlist):
		words = document.split()
		for word in words:
			if word in dictionary:
				dictionary[word].append(documentNumber)
			else:
				dictionary[word] = list({documentNumber})
	return dictionary

# Takes in an inverse index and list of words, and returns the set of document numbers specifying all documents
# that contain any of the words in query
def orSearch(inverseIndex, query):
	queryWordsInIndex = set()
	words = query.split()
	for word in words:
		if word in inverseIndex:
			queryWordsInIndex.update(inverseIndex[word])
	return queryWordsInIndex


documents = ["Here is quite a few words", "and a few more", "and some more"]
print("Initial document: ", documents)
# Test makeInverseIndex
index = makeInverseIndex(documents)
print("Test makeInverseIndex: ", index)
# Output: {'two': [1, 2], 'one': [0, 2]}

# Test orSearch
query = "more"
print("Initial query: ", query)
searchResults = orSearch(index, query)
print("Test orSearch: ", searchResults)