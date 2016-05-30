from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

# Create your models here.
class MCplusplus(models.Model):
    question = models.TextField()
    solution = models.TextField()

class MCplusplusAdmin(admin.ModelAdmin):
    list_display = ('question', )

admin.site.register(MCplusplus, MCplusplusAdmin)
