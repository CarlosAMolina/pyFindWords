#!/usr/bin/python

__author__ = "Carlos A. Molina"

import sys
from utility_ask import Ask
from utility_change import Change
from utility_check import Check
from utility_get import Get
from utility_show import Show
from utility_urlConnection import URLconnection

ask = Ask()
ch = Change()
ck = Check()
get = Get()
show = Show()
con = URLconnection()

#main
arguments = sys.argv # [f=text/w=web/r=repeated, url, tex2chekInWeb]
filesNames = get.getFilesNames(arguments)
webHTML = None
if len(filesNames) == 2 and filesNames[1] == 'web.html':
	webHTML = con.connect(filesNames[1], arguments)
	if ask.askWebText2check(webHTML, arguments) == -1:
		filesNames[1] = ''
else:
	print '\nAnalyzing .txt file'
if ck.filesReady(filesNames) == 1:
	if len(filesNames) == 1:
		modifyWords = 0
		showAlertExtrangeCharacters = 0
		words2study = get.getWordsList(filesNames[0],showAlertExtrangeCharacters,modifyWords)
		words2find = words2study
	else:
		modifyWords = 1
		showAlertExtrangeCharacters = 1
		words2study = get.getWordsList(filesNames[1])
		words2find = get.getWordsList(filesNames[0],showAlertExtrangeCharacters,modifyWords)
		print 'Working with lowercase words and avoiding accents to improve results\n'
	words2find = ch.avoidDuplicates(words2find)
	results = ck.checkWordsInText(words2study, words2find)
	results = ch.changeOrder (results,'numberOfSearchsTotal') # descending order
	showOption = 0 # 0,1: separate results or together
	showNoFound = 0 # 0,1: show only found words or all
	showExactPartial = 1 # 0,1: show only total matches or exact and partial matches too
	show.showResults(results, showOption, showNoFound, showExactPartial)  