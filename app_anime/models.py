from django.core import validators
from django.db import models
from django.forms import BooleanField
from django.core.validators import RegexValidator
import uuid

only_letters = RegexValidator(r'^[a-z]*$', 'Only letter characters are allowed.')
status_choices = [("Completed","Completed"),("Ongoing","Ongoing"),("Unknown","Unknown")]
watching_choices = [("Completed","Completed"),("Watching","Watching"),("Dropped","Dropped"),("On_hold","On Hold"),("Planning_To_Watch","Planning To Watch")]

class Anime(models.Model):
    anime_id = models.CharField(max_length=5, unique=True, validators=[only_letters])
    anime_title = models.CharField(max_length=200)
    anime_alternative_title = models.CharField(max_length=100, blank=True)
    anime_studio = models.CharField(max_length=200)
    anime_seasons = models.IntegerField(default=0)
    anime_episodes = models.IntegerField(default=0)
    anime_watched_episodes = models.IntegerField(default=0)
    anime_status = models.CharField(max_length=250, choices=(status_choices), default="unknown")
    anime_watching_status = models.CharField(max_length=250, choices=(watching_choices), default="reading")
    anime_cover_image = models.URLField(max_length=200)
    def __str__(self):
    	return self.anime_title