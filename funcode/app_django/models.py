from django.db import models
from django.contrib import admin

# Create your models here.
class DataBase(models.Model):
    question = models.TextField()
    solution = models.TextField()

class Templates(models.Model):
    question = models.TextField()
    solution = models.TextField()

class DBAdmin(admin.ModelAdmin):
    list_display = ('question', )

admin.site.register(DataBase, DBAdmin)
admin.site.register(Templates, DBAdmin)
