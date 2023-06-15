from django.contrib import admin

# Register your models here.
from .models import Card, Watch


admin.site.register(Card)
admin.site.register(Watch)