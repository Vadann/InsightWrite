from django.shortcuts import render, redirect
from django.db import models


class Meditation(models.Model):
    meditation_id = models.IntegerField(primary_key=True, serialize=False, verbose_name='Meditation ID')
    user_id = models.IntegerField()
    video_url = models.URLField()