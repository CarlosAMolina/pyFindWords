#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, re

class Check:

	def __init__(self):
		self.vowels = 'aeiou'

	def checkArgumentsGiven (self, arguments):
		if len(arguments) == 1:
			return -1
		else:
			return 1

	def checkStrIsInt(self, string, message=1):
		try:
			int(string)
			return 1
		except:
			if message == 1:
				print 'Introduce a number'
			return -1

	def checkStrIsConsonant(self, string, message=1):
		try:
			if string not in self.vowels and len (string) == 1:
				return 1
			else:
				if message == 1:
					print 'Introduce a consonant'
				return -1
		except:
			return -1

	def checkFileExists(self, filePathAndName):
		try:
			open(filePathAndName,'r') # name and file extension
			return 1
		except:
			return -1

	def checkFiles (self, files2check):
		# files2check := list
		for file2check in files2check:
			if self.checkFileExists(file2check) == -1:
				return -1
		return 1

	def checkCorrectWeb (self, web2analyze, text2check):
		if text2check in web2analyze:
			print '\nWorking with correct web ..... OK'
			return 1
		else:
			print '\nWorking with correct web ..... ERROR'
			return -1

	def filesReady (self, filesNames):
		if len (filesNames) == 2 and filesNames[1] == 'web.html' and self.checkFiles(filesNames) == 1:
			return 1
		elif len(filesNames) == 1 and filesNames[0] == 'fileWhereFindWords.txt' and self.checkFiles(filesNames) == 1:
			return 1
		elif len(filesNames) == 2 and filesNames[1] == 'fileWhereFindWords.txt' and self.checkFiles(filesNames) == 1:
			return 1
		return -1 # bad fileName

	def checkWordInText (self, wordsOfTextWhereFind, word2find):
		numberOfChecksExact = 0
		numberOfChecksPartial = 0
		for wordInText in wordsOfTextWhereFind:
			if word2find == wordInText:
				numberOfChecksExact += 1
			elif word2find in wordInText:
				numberOfChecksPartial += 1
		return numberOfChecksExact, numberOfChecksPartial

	def checkWordsInText (self, wordsOfTextWhereFind, words2find):
		result = {'word':0, 'numberOfSearchsExact':0, 'numberOfSearchsPartial':0, 'numberOfSearchsTotal':0}
		# example: mouse and mouse -> searchExtact, mouse and mouses -> searchPartial
		results = []
		for word2find in words2find:
			result['word'] = word2find
			result['numberOfSearchsExact'], result['numberOfSearchsPartial'] = self.checkWordInText(wordsOfTextWhereFind, word2find)
			result['numberOfSearchsTotal'] =  result['numberOfSearchsExact'] + result['numberOfSearchsPartial']
			results.append(result)
			result = {'word':0, 'numberOfSearchsExact':0, 'numberOfSearchsPartial':0, 'numberOfSearchsTotal':0} # necessary initialize the dictionary object
		return results