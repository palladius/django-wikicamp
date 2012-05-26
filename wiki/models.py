from django.db import models

class Page(models.Model):
    name   = models.CharField(maxlength="20", primary_key=True) # so this IS the primary key
    content = models.TextField(blank=True)
