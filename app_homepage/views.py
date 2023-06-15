from django.shortcuts import render
import app_homepage.utils.extraction as ext

from .models import Card, Watch
watch_headers = ["Show", "Episode", "Watch", "Download"]
def serve_homepage(request):
	card = Card.objects.all()
	watch = Watch.objects.all()
	show_list = []

	for x in watch:
		show_list.append(x.show_name)

	wanted = ext.extractMostRecentAnimeList('https://gogoanime.llc/?page=', show_list)
	context = {'card': card, 'watch': watch, 'show': wanted, 'w_header': watch_headers}
	return render(request, 'app_homepage/homepage_index.html', context)