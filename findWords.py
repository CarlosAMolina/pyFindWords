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
    return results

def showResults (results,showOption = 0):
    if showOption == 0:  # separate results
        resultsFinded, resultsNoFinded = separateResults(results)
        print 'Words not found'
        print '###############'
        for result in resultsNoFinded:
            showResult(result)
        print '\nWords found'
        print '###############'
        for result in resultsFinded:
            showResult(result)
    elif showOption == 1: # show all results together
        for result in results:
            showResult(result)    

def separateResults (results):
    # save finded results in one list and no finded results in other list
    resultsFinded = []
    resultsNoFinded = []
    for result in results:
        if result['numberOfSearchsTotal'] > 0:
            resultsFinded.append(result)
        else:
            resultsNoFinded.append(result)
    return resultsFinded, resultsNoFinded

def showResult (result,showOption=0):
    if showOption == 1:
        print result['word'] + ': ' + str(result['numberOfSearchsTotal']) + ' (' + str(result['numberOfSearchsExact']) + ' extact, ' + str(result['numberOfSearchsPartial']) + ' partial)'
    else:
        print result['word'] + ': ' + str(result['numberOfSearchsTotal'])

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
    showResults(results)