from django.core import validators
from django.db import models
from django.forms import BooleanField
from django.core.validators import RegexValidator
import uuid

only_letters = RegexValidator(r'^[a-z]*$', 'Only letter characters are allowed.')
status_choices = [("Completed","Completed"),("Ongoing","Ongoing"),("Unknown","Unknown")]
reading_choices = [("Completed","Completed"),("Reading","Reading"),("Dropped","Dropped"),("On_hold","On Hold"),("Planning_To_Read","Planning To Read")]

class Manga(models.Model):
    manga_id = models.CharField(max_length=5, unique=True, validators=[only_letters])
    manga_title = models.CharField(max_length=200)
    manga_alternative_title = models.CharField(max_length=100, blank=True)
    manga_author = models.CharField(max_length=200)
    manga_volumes = models.IntegerField(default=0)
    manga_read_volumes = models.IntegerField(default=0)
    manga_publisher = models.CharField(max_length=200)
    manga_status = models.CharField(max_length=250, choices=(status_choices), default="unknown")
    manga_reading_status = models.CharField(max_length=250, choices=(reading_choices), default="reading")
    manga_cover_image = models.URLField(max_length=200)
    def __str__(self):
    	return self.manga_title

class Manhwa(models.Model):
    manhwa_id = models.CharField(max_length=5, unique=True, validators=[only_letters])
    manhwa_title = models.CharField(max_length=250)
    manhwa_chapters = models.IntegerField(default=0)
    manhwa_read_chapters = models.IntegerField(default=0)
    manhwa_status = models.CharField(max_length=250, choices=(status_choices), default="unknown")
    manhwa_reading_status = models.CharField(max_length=250, choices=(reading_choices), default="reading")
    manhwa_cover_image = models.URLField(max_length=200)
    def __str__(self):
    	return self.manhwa_title