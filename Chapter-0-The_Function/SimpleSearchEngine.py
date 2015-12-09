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

# Takes an inverse index and list of words query and returns the set of document numbers specifying all documents that
# contain all of the words in the query
def andSearch(inverseIndex, query):
	words = query.split()
	if words[0] not in inverseIndex: # If the first word is not in the index, we can stop now
		return set()
	queryWordsInIndex = set()
	queryWordsInIndex.update(inverseIndex[words[0]])
	words = words[1:]
	for word in words:
		if word not in inverseIndex: # If any word is not in the inverseIndex, returns empty set
			return set()
		queryWordsInIndex = {documentNumber for documentNumber in queryWordsInIndex if documentNumber in inverseIndex[word]}
		if queryWordsInIndex == set(): # If we ever get to a point where we have a null set, just return
			return set()
	return queryWordsInIndex


documents = ["Here is quite a few words", "and a few more", "and some more"]
print("Initial document: ", documents)
# Test makeInverseIndex
index = makeInverseIndex(documents)
print("Test makeInverseIndex: ", index)

# Test orSearch
query = "more" # Exists in 1 and 2
print("Initial query: ", query)
searchResults = orSearch(index, query)
print("Test orSearch: ", searchResults)
query = "a more" # Exists in 0, 1 and 2
print("Initial query: ", query)
searchResults = orSearch(index, query)
print("Test orSearch: ", searchResults)
query = "test" # Exists in none of the documents
print("Initial query: ", query)
searchResults = orSearch(index, query)
print("Test orSearch: ", searchResults)

# Test andSearch
query = "a more" # Exists in the first set
print("New query: ", query)
searchResults = andSearch(index, query)
print("Test andSearch: ", searchResults)
query = "Here a more" # All three of these do not exist in any single set
print("New query: ", query)
searchResults = andSearch(index, query)
print("Test andSearch: ", searchResults)