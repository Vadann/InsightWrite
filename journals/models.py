from django.db import models
from datetime import date

# Journal Models

class Journal(models.Model):
    journal_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    tag_id = models.CharField()
    title = models.CharField(max_length=200)
    entry_date = models.DateField(auto_now_add=True, verbose_name='Date published')
    last_modified_date = models.DateField(auto_now=True, verbose_name='Last modified')
    content = models.TextField() 

class Tag(models.Model):
    tag_id = models.IntegerField(primary_key=True, serialize=False, verbose_name='Tag ID')
    journal_id = models.IntegerField()
    tag_name = models.CharField(max_length = 200)
    tag_color = models.CharField(max_length = 10)