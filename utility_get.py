#!/usr/bin/python

__author__ = "Carlos A. Molina"

from utility_ask import Ask
from utility_change import Change
from utility_show import Show

class Get:

	def __init__(self):
		self.ask = Ask()
		self.ch = Change()
		self.show = Show()

	def getWordsList (self, fileWithWords,gettingWords2search=0):
		# input: fileWithWords - file name with its extension
		# output: list of words of the file
		fileContent = self.getFileContent(fileWithWords)
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
		try:
			whatAnalyze = arguments[1] # f=file, w=web
			if whatAnalyze == 'f':
				whatAnalyze = 1
			elif whatAnalyze == 'w':
				whatAnalyze = 2
			else:
				whatAnalyze = self.ask.askAnalyzeFileOrWeb() #1 file. 2 URL
		except:
			whatAnalyze = self.ask.askAnalyzeFileOrWeb() #1 file. 2 URL
		if whatAnalyze == 1:
			filesNames.append('fileWhereFindWords.txt')
		else:
			filesNames.append('web.html')
		return filesNames