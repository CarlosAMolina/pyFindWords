#!/usr/bin/python
#-*-coding:utf-8-*-

__author__ = "Carlos A. Molina"

import sys
from utility_check import Check
from utility_change import Change

class Ask:

	def __init__(self):
		self.ck = Check()
		self.ch = Change()

	def ask4url(self):
		url2study = ""
		print '\nWrite the URL to study (format example: https://github.com/)'
		while url2study == "":
			url2study = raw_input ('>> ')
		return url2study

	def ask4number(self):
		# ask until the answer is an integer
		number = ''
		while number == '':
			print 'Select number'
			number = self.askNumber()
		return number

	def ask4consonant(self):
		# ask until the answer is a consonant
		consonant = ''
		while consonant == '':
			#print 'Select consonant'
			consonant = self.askConsonant()
		return consonant

	def askNumber(self):
		# return number (type int) or '' (advising invalid syntax)
		number = raw_input ('>> ') # string
		if self.ck.checkStrIsInt(number) == -1:
			number = ''
			print '\nInvalid option\n'
		else:
			number = self.ch.convertString2Int(number)
		return number

	def askConsonant(self):
		# return consonant (type str) or '' (advising invalid syntax)
		consonant = raw_input ('>> ') # string
		if self.ck.checkStrIsConsonant(consonant,0) == -1:
			consonant = ''
			print 'Invalid option'
		return consonant

	def askOverwriteFile(self, fileName):
		print 'File ' +str(fileName)+ ' already exists'
		print 'Options:\n1.Overwrite \n2.New file'
		fileOptions = ''
		while fileOptions!=1 and fileOptions!=2:
			fileOptions = self.ask4number()
		if fileOptions == 2:
			fileOptions = -1
		return fileOptions

	def askAnalyzeFileOrWeb (self):
		print '\nSelect what to study:\n(f) File fileWhereFindWords.txt \n(r) Repeated words in file \n(w) URL'
		whatAnalyze = 'x'
		while whatAnalyze not in 'frw':
			whatAnalyze = self.ask4consonant()
		return whatAnalyze

	def askWebText2check (self, web2check, arguments):
		if arguments[3:] != []:
			try:
				text2check = ' '.join(arguments[3:])
			except:
				arguments[3:] == []
		elif arguments[3:] == []:
			print '\nTo check the tool is working with correct web content, please type a short piece of the text to analyze (case sensitive, not use accents)'
			text2check = raw_input('>>> ')
		return self.ck.checkCorrectWeb (web2check,text2check)