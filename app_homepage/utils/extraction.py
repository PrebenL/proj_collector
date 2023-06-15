import re, requests
from bs4 import BeautifulSoup

def extractMostRecentAnimeList(pBaseUrl, pWantedList):
	vEpisodeLib = {}
	for page in range(1, 4):
		mainset = BeautifulSoup(requests.get(pBaseUrl + str(page)).text,'lxml').find(
			'ul', {'class': 'items'})
		for x in mainset.find_all("li"):
			name = x.find("p", class_='name').a['title']
			episode = x.find("p", class_='episode').get_text()
			url = '{}{}'.format('https://gogoanime.tel', x.find("a", href=True).get('href'))
			down = 'https://nyaa.si/?q={}&f=0&c=0_0&s=seeders&o=desc'.format(name.replace(' ', '+'))
			if name in pWantedList:
				vEpisodeLib[name] = [] 
				vEpisodeLib[name].append(episode)
				vEpisodeLib[name].append(url)
				vEpisodeLib[name].append(down)

	return vEpisodeLib