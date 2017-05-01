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
arguments = sys.argv # [-f=text/-w=web, url, tex2chekInWeb]
filesNames = get.getFilesNames(arguments)
webHTML = None
if filesNames[1] == 'web.html':
	webHTML = con.connect(filesNames[1], arguments)
	if ask.askWebText2check(webHTML, arguments) == -1:
		filesNames[1] = ''
else:
	print '\nAnalyzing .txt file'
if ck.filesReady(filesNames) == 1:
	words2study = get.getWordsList(filesNames[1])
	words2find = get.getWordsList(filesNames[0],1)
	words2find = ch.avoidDuplicates(words2find)
	print 'Working with lowercase words and avoiding accents to improve results\n'
	results = ck.checkWordsInText(words2study, words2find)
	show.showResults(results,0,0,1) # 0,1: separated results or together. 0,1: only found words or all. 0,1: show only total matches or exact and partial matches too