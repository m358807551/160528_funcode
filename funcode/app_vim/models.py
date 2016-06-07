from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class Mvim(models.Model):
    question = models.TextField()
    solution = models.TextField()
    
    def __unicode__(self):
        return self.question

admin.site.register(Mvim)
