from __future__ import unicode_literals
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(max_length = 1000)
    date_added = models.DateTimeField(auto_now_add = True)