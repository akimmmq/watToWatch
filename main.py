from random import randint

import requests as re
from brain import Brain


class Main():
	chap = Brain() 	
	def getAnime(self, genre: str) -> str:
		try :
			alist = self.chap.getAnimes(genre)
			return f'You can watch {alist[randint(0 , len(alist)-1)]}!'
		except:
			return 'You got an error :('
	
if __name__ == '__main__':
	while True:
		start = Main()
		result = start.getAnime(input("What genre you'd like to watch? "))
		print(result)