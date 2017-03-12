#!/usr/bin/python

__author__ = "Carlos A. Molina"

def checkFileExists (fileNameWithExtension):
    try:
        open(fileNameWithExtension, 'r')
        return 1
    except:
        return -1

def checkFiles (files2check):
    for file2check in files2check:
        if checkFileExists(file2check) == -1:
            return -1
    return 1

def getWordsList (fileWithWords,gettingWords2search=0):
    # input: fileWithWords - file name with its extension
    # output: list of words of the file
    fileContent = getFileContent(fileWithWords)
    if gettingWords2search == 1:
        showWords2searchAlert(fileContent)
    fileContent = noCharacters(fileContent)
    fileContent = fileContent.lower() # more searches if all words are lowercase
    wordsList = fileContent.split()
    return wordsList 

def showWords2searchAlert(fileContent):
    characters2avoid = [',',
                        '.',
                        '-',
                        '_',
                        ';',
                        ':'] # characters that can reduce the results
    for character2avoid in characters2avoid:
        if character2avoid in fileContent:
            print 'Alert: "' + character2avoid + '" was detected in the words you want to search, it can reduce the results'
    print ''

def avoidDuplicates(wordsList):
    # input: list of strings
    # output: list of string without duplicates
    wordsList = list(set(wordsList)) # note: order is altered
    return wordsList

def noCharacters(string2change):
    # more searches if accents and other characters are avoided
    dicCharacters = {'a':'\xc3\xa1',
                     'e':'\xc3\xa9',
                     'i':'\xc3\xad',
                     'o':'\xc3\xb3',
                     'u':'\xc3\xba',
                     'A':'\xc3\x81',
                     'E':'\xc3\x89',
                     'I':'\xc3\x8d',
                     'O':'\xc3\x93',
                     'U':'\xc3\x9a',
                     'egnie':'\xc3\xb1',
                     'egNie':'\xc3\x91'}
    for character in dicCharacters:
        string2change = string2change.replace(dicCharacters[character],character) # character = dictinary key
    return string2change

def getFileContent (fileNameWithExtension):
    fileOpened = open(fileNameWithExtension)
    fileContent = fileOpened.read()
    fileOpened.close()
    #fileContent = fileContent.decode('utf8') # work with accents. Using noCharacters() function this line is not necessary
    return fileContent

def checkWord (wordsOfTextWhereFind, word2find):
    numberOfChecksExact = 0
    numberOfChecksPartial = 0
    for wordInText in wordsOfTextWhereFind:
        if word2find == wordInText:
            numberOfChecksExact += 1
        elif word2find in wordInText:
            numberOfChecksPartial += 1
    return numberOfChecksExact, numberOfChecksPartial

def checkWords (wordsOfTextWhereFind, words2find):
    result = {'word':0, 'numberOfSearchsExact':0, 'numberOfSearchsPartial':0, 'numberOfSearchsTotal':0}
    # example: mouse and mouse -> searchExtact, mouse and mouses -> searchPartial
    results = []
    for word2find in words2find:
        result['word'] = word2find
        result['numberOfSearchsExact'], result['numberOfSearchsPartial'] = checkWord(wordsOfTextWhereFind, word2find)
        result['numberOfSearchsTotal'] =  result['numberOfSearchsExact'] + result['numberOfSearchsPartial']
        results.append(result)
        result = {'word':0, 'numberOfSearchsExact':0, 'numberOfSearchsPartial':0, 'numberOfSearchsTotal':0} # necessary initialize the dictionary object
    resultsSorted = sorted(results, key=lambda k: k['numberOfSearchsTotal']) #http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
    return resultsSorted # descending order

def showResults (results,showOption = 0, showExactPartial = 0):
	# showOption = 1: show all results together
	# showOption = 0: separate results: word founds and not found
	# showExactPartial = 1: show number of total, exact and partial matches
	# showExactPartial = 0: show only number of total matches
	headers = ['Word', 'Total']
	if showExactPartial == 1:
		headers.append('Exact')
		headers.append('Partial')
	if showOption == 0:  # separate results
		resultsFound, resultsNoFound = separateResults(results)
		infoNoFound, colWidthNoFound = tableInfo (headers, resultsNoFound, showExactPartial)
		infoFound, colWidthFound = tableInfo (headers, resultsFound, showExactPartial)
		print 'Words not found'
		print '#' * 40
		showInfo (infoNoFound, colWidthNoFound)
		print '\nWords found'
		print '#' * 40
		showInfo (infoFound, colWidthFound)
	elif showOption == 1: # all results
		info, colWidth = tableInfo (headers, results, showExactPartial)
		showInfo (info, colWidth)

def tableInfo (headers, results, showExactPartial):
	info = []
	info.append(headers)
	for result in results:
		if showExactPartial == 0:
			result2info = [result['word'], result['numberOfSearchsTotal']]
		elif showExactPartial == 1:
			result2info = [result['word'], result['numberOfSearchsTotal'], result['numberOfSearchsExact'], result['numberOfSearchsPartial']]
		info.append(result2info)
	colWidth = max ( len(str(word)) for row in info for word in row ) + 3 # padding http://stackoverflow.com/questions/9989334/create-nice-column-output-in-python
	return info, colWidth

def separateResults (results):
    # save found results in one list and no found results in other list
    resultsFound = []
    resultsNoFound = []
    for result in results:
        if result['numberOfSearchsTotal'] > 0:
            resultsFound.append(result)
        else:
            resultsNoFound.append(result)
    return resultsFound, resultsNoFound

def showInfo (info, col_width=0):
	for row in info:
		print ("".join(str(word).ljust(col_width) for word in row)) # str(): avoid error if word = None

#main

filesNames = ['words2Find.txt', 'fileWhereFindWords.txt']
if checkFiles(filesNames) == -1:
    print 'Check these files exist: '+ str(filesNames)
else:
    wordsText = getWordsList(filesNames[1])
    words2find = getWordsList(filesNames[0],1)
    words2find = avoidDuplicates(words2find)
    print 'Working with lowercase words and avoiding accents to improve results\n'
    results = checkWords(wordsText, words2find)
    showResults(results,0,0) # 0,1: separated results or together. 0,1: show only total matches or exact and partial matches too