from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

# Create your models here.
class MRzrk(models.Model):
    question = models.TextField()
    solution = models.TextField()

class MRzrkAdmin(admin.ModelAdmin):
    list_display = ('question', )

admin.site.register(MRzrk, MRzrkAdmin)
