from django.shortcuts import render
from django.http import HttpResponse, request

from .models import Manga, Manhwa

table_manga_spreadsheet_header = ["#" ,"Manga", "Status"]
table_manhwa_spreadsheet_header = ["#" ,"Manhwa", "Status"]

def serve_manga(request):
    manga = Manga.objects.all().order_by('manga_title')
    manhwa = Manhwa.objects.all().order_by('manhwa_title')
    context = {
                'manga': manga,
                'manhwa': manhwa, 
                'manga_ts_header': table_manga_spreadsheet_header, 
                'manhwa_ts_header': table_manhwa_spreadsheet_header
                }
    return render(request, 'app_manga/manga_index.html', context)