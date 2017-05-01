#!/usr/bin/python

__author__ = "Carlos A. Molina"

import urllib
import sys
import os
from utility_exportInformation import UtilityExport
from utility_ask import Ask


class URLconnection:

	def __init__(self):
		self.uE = UtilityExport()
		self.ask = Ask()
		self.scriptPath = os.path.dirname(os.path.abspath(__file__)) # script's path
		self.savePath = self.scriptPath

	def connect(self,fileName, arguments):
		try:
			webURL = arguments[2]
		except:
			webURL = self.ask.ask4url()
		con = urllib.urlopen(webURL)
		webHTML = con.read()
		self.uE.createFile(self.savePath, fileName, webHTML)
		return webHTML