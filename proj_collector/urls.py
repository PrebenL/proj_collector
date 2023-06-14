from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('series/', include("app_series.urls")),
    path('movies/', include("app_movies.urls")),
    path('manga/', include("app_manga.urls")),
    path('admin/', admin.site.urls),
]
