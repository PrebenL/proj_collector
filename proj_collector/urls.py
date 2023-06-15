from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('series/', include("app_series.urls")),
    path('home/', include("app_homepage.urls")),
    path('manga/', include("app_manga.urls")),
    path('anime/', include("app_anime.urls")),
    path('admin/', admin.site.urls),
]
