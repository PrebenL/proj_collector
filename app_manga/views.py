from django.shortcuts import render
from django.http import HttpResponse, request

from .models import Manga, Manhwa

table_spreadsheet_header = ["#","Manga", "Volumes","Read", "Status", "Activity", "Cover"]

def serve_manga(request):
    manga = Manga.objects.all()
    context = {'manga': manga, 'ts_header': table_spreadsheet_header}
    return render(request, 'app_manga/manga_index.html', context)