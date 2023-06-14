from django.core import validators
from django.db import models
from django.forms import BooleanField
from django.core.validators import RegexValidator
import uuid

only_letters = RegexValidator(r'^[a-z]*$', 'Only letter characters are allowed.')

class Manga(models.Model):
    status_choices = [("completed","Completed"),("ongoing","Ongoing"),("unknown","Unknown")]
    reading_choices = [("completed","Completed"),("reading","Reading"),("dropped","Dropped"),("on_hold","On Hold"),("x","x")]
    manga_id = models.CharField(max_length=5, unique=True, validators=[only_letters])
    manga_title = models.CharField(max_length=200)
    manga_alternative_title = models.CharField(max_length=100, blank=True)
    manga_author = models.CharField(max_length=200)
    manga_volumes = models.IntegerField(default=0)
    manga_read_volumes = models.IntegerField(default=0)
    manga_publisher = models.CharField(max_length=200)
    manga_status = models.CharField(max_length=250, choices=(status_choices), default="unknown")
    manga_reading_status = models.CharField(max_length=250, choices=(reading_choices), default="reading")
    manga_cover_picture = models.URLField(max_length=200)
    def __str__(self):
    	return self.manga_title

class Manhwa(models.Model):
    manhwa_title = models.CharField(max_length=200)
    manhwa_alternative_title = models.CharField(max_length=200)
    manhwa_volumes = models.IntegerField(default=0)
    manhwa_publisher = models.CharField(max_length=200)
    def __str__(self):
    	return self.manhwa_title