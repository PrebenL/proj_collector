from django.shortcuts import render
from django.http import request

from .models import Anime

table_anime_spreadsheet_header = ["#" ,"Anime", "Status"]

def serve_anime(request):
    anime = Anime.objects.all().order_by('anime_title')
    context = {
                'anime': anime, 
                'anime_ts_header': table_anime_spreadsheet_header, 
                }
    return render(request, 'app_anime/anime_index.html', context)