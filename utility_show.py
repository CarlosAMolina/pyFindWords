#!/usr/bin/python

__author__ = "Carlos A. Molina"

class Show:

	def showWords2searchAlert(self, fileContent):
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

	def showResults (self, results, showOption = 0, showNoFound = 0, showExactPartial = 0):
		# showOption = 1: show all results together
		# showOption = 0: separate results: word founds and not found
		# showNoFound = 1: show not found words
		# showNoFound = 0: show only found words
		# showExactPartial = 1: show number of total, exact and partial matches
		# showExactPartial = 0: show only number of total matches
		headers = ['Word', 'Total']
		if showExactPartial == 1:
			headers.append('Exact')
			headers.append('Partial')
		if showOption == 0:  # separate results
			resultsFound, resultsNoFound = self.separateResults(results)
			if showNoFound == 1:
				infoNoFound, colWidthNoFound = self.tableInfo (headers, resultsNoFound, showExactPartial)
				print 'Words not found'
				print '#' * 40
				self.showInfo (infoNoFound, colWidthNoFound)
			infoFound, colWidthFound = self.tableInfo (headers, resultsFound, showExactPartial)
			print '\nWords found'
			print '#' * 40
			self.showInfo (infoFound, colWidthFound)
		elif showOption == 1: # all results
			info, colWidth = self.tableInfo (headers, results, showExactPartial)
			self.showInfo (info, colWidth)

	def tableInfo (self, headers, results, showExactPartial):
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

	def separateResults (self, results):
		# save found results in one list and no found results in other list
		resultsFound = []
		resultsNoFound = []
		for result in results:
			if result['numberOfSearchsTotal'] > 0:
				resultsFound.append(result)
			else:
				resultsNoFound.append(result)
		return resultsFound, resultsNoFound

	def showInfo (self, info, col_width=0):
		for row in info:
			print ("".join(str(word).ljust(col_width) for word in row)) # str(): avoid error if word = None