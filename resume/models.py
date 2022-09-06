
from unicodedata import name
from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True )
    url = models.CharField(max_length=500, null=True, blank=True )
    created = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created']

    def __str__(self) :
        return self.name


class Techstack(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name
       