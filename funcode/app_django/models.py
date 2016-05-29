from django.db import models
from django.contrib import admin

# Create your models here.
class MDjango(models.Model):
    question = models.TextField()
    solution = models.TextField()

class MDjangoAdmin(admin.ModelAdmin):
    list_display = ('question', )

admin.site.register(MDjango, MDjangoAdmin)
