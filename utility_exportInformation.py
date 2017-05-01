#!/usr/bin/python
#-*-coding:utf-8-*-

__author__ = "Carlos A. Molina"

import sys, time, os.path
from utility_ask import Ask

class UtilityExport:

	def __init__(self):
		self.ask = Ask()
		self.fileExtension = '.html'

	def createFile(self, savePath, name4file, information2save, overwrite='yes'): # overwrite: no = allow save old web.html files
		fileName = name4file #+ self.fileExtension
		fileName, filePathAndName = self.__checkFileExistsAndAsk(fileName, savePath, overwrite)
		file = open(filePathAndName,'w') # create file
		file.write(information2save)	# write information in file
		file.close()	# end work with file
		print '\nWeb page HTML was saved. File: ' + fileName

	def __checkFileExistsAndAsk(self, fileName, savePath, overwrite):
		filePathAndName = os.path.join(savePath, fileName)
		if self.__checkFileExists(filePathAndName) == 1 and overwrite != 'yes':
			if self.ask.askOverwriteFile(fileName) == -1:
				fileName = fileName.replace(self.fileExtension, '_'+self.__getDatetime()+self.fileExtension)
				filePathAndName = os.path.join(savePath, fileName)
		return fileName, filePathAndName

	def __checkFileExists(self, filePathAndName):
		try:
			open(filePathAndName,'r')
			return 1
		except:
			return -1

	def __getDatetime(self):
		time2 = time.strftime("%H-%M-%S")
		date = time.strftime("%Y-%m-%d")
		datetime = '%s_%s' %(date, time2)
		return datetime


"""
def saveInFile(what2save, savePath, fileName):
    filePathAndName = os.path.join(savePath, fileName)
    try:
        what2save = str(what2save)
    except:
        what2save = str(what2save.encode('utf-8')) #  avoid error UnicodeEncodeError: 'ascii' codec can't encode character ... in position ...: ordinal not in range(128)
    file = open(filePathAndName,'w') # create file
    file.write(what2save)   # write information in file
    file.close()
    print 'Information saved'
"""