import requests as re

from script import Script
from bs4 import BeautifulSoup

class Brain():
	genresIDs = Script().getIDs()
	genresNames = Script().getNames()
	link = 'https://myanimelist.net/anime/genre/'
	
	def linkBuilder(self , genre):
		genre = genre.lower()
		
		if genre in self.genresNames:
			genrInx = self.genresNames.index(genre)
			return f'https://myanimelist.net/anime/genre/{self.genresIDs[genrInx]}'
		return 'This genre is not exist'
	
	
	
	def getAnimes(self, genre):
		finalList = []
		link = self.linkBuilder(genre)
		response = re.get(link).text
		soup = BeautifulSoup(response, 'lxml')
		animeList = soup.find_all('span' , {'class' : 'js-title'})
		for anime in animeList:
			if anime != None:
				finalList.append(anime.text)
		return finalList