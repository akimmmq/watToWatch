import requests as re

from random import randint
from bs4 import BeautifulSoup
  


class Script():
	url = 'https://myanimelist.net/anime.php'
	response = re.get(url).text
	
	gnList = [] #genres name array
	idList = [] #ids array
	mainList = [] #result list
	
	def getGanres(self):
		
		
		soup = BeautifulSoup(self.response, 'lxml')
		genreHead = soup.find('div', {'class' : 'category-wrapper'})
		
		pNames = genreHead.find_all('p')
		idNumbers = genreHead.find_all('input')
		
		for pValue in pNames:
			pValue = str(pValue)
			pName , q  = pValue.split(' (')
			pName = pName[3:]
			self.gnList.append(pName.lower())
			
		for idNum in idNumbers:
			idNum = str(idNum['value'])
			self.idList.append(idNum)
		
		for i in range(len(self.gnList)):
			value = f'[{self.idList[i]} , {self.gnList[i]}]'
			self.mainList.append(value)
		
	def getIDs (self):
		self.getGanres()
		return self.idList
	
	def getNames(self):
		self.getGanres()
		return self.gnList
	
	def getAll(self):
		self.getGanres()
		return self.mainList