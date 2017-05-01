#!/usr/bin/python

__author__ = "Carlos A. Molina"

class Change:

	def avoidDuplicates(self, wordsList):
		# input: list of strings
		# output: list of string without duplicates
		wordsList = list(set(wordsList)) # note: order is altered
		return wordsList

	def noCharacters(self, string2change):
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

	def convertString2Int (self,string2convert):
		# input: type string
		# output: type int
		intConverted = int(string2convert)
		return intConverted