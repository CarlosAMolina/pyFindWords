#!/usr/bin/python

__author__ = "Carlos A. Molina"

from utility_ask import Ask
from utility_change import Change
from utility_check import Check
from utility_show import Show

class Get:

	def __init__(self):
		self.ask = Ask()
		self.ch = Change()
		self.ck = Check()
		self.show = Show()

	def getWordsList (self, fileWithWords=0, gettingWords2search= 1, modify=1):
		# input: fileWithWords - file name with its extension
		# output: list of words of the file
		fileContent = self.getFileContent(fileWithWords)
		if modify == 1:
			if gettingWords2search == 1:
				self.show.showWords2searchAlert(fileContent)
			fileContent = self.ch.noCharacters(fileContent)
			fileContent = fileContent.lower() # more searches if all words are lowercase
		wordsList = fileContent.split()
		return wordsList 

	def getFileContent (self, fileNameWithExtension):
		fileOpened = open(fileNameWithExtension)
		fileContent = fileOpened.read()
		fileOpened.close()
		#fileContent = fileContent.decode('utf8') # work with accents. Using noCharacters() function this line is not necessary
		return fileContent

	def getFilesNames (self, arguments):
		filesNames = ['words2Find.txt']
		if self.ck.checkArgumentsGiven(arguments) == -1:
			whatAnalyze = self.ask.askAnalyzeFileOrWeb()
		else:
			whatAnalyze = arguments[1] # f=file, r=repeated, w=web 
		if whatAnalyze == 'f':
			filesNames.append('fileWhereFindWords.txt')
		elif whatAnalyze == 'r':
			filesNames = ['fileWhereFindWords.txt'] # search in a file the number of times each word appears
		elif whatAnalyze == 'w':
			filesNames.append('web.html')
		else:
			whatAnalyze = self.ask.askAnalyzeFileOrWeb()	
		return filesNames