from django.db import models

class Card(models.Model):
	card_category_choices = [('dev', 'Development'), ('torrents', 'Torrents'),('media', 'Media')]
	card_title = models.CharField(max_length=200)
	card_category = models.CharField(max_length=100, choices=card_category_choices)
	card_url = models.CharField(max_length=200)
	def __str__(self):
		return self.card_title

class Watch(models.Model):
	show_name = models.CharField(max_length=200)
	show_aka_name = models.CharField(max_length=200)
	def __str__(self):
		return self.show_aka_name