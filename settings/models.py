from django.db import models

class UserSettings(models.Model):
    user_id = models.IntegerField(primary_key=True, serialize=False, verbose_name='User ID')
    username = models.CharField()
    email = models.EmailField()
    verified_email = models.BooleanField()
    password = models.CharField()
    account_created_date = models.DateField()
    first_name = models.CharField()
    middle_name = models.CharField()
    last_name = models.CharField()
    birth = models.DateField()
    theme = models.CharField()
    notifications = models.BooleanField()
    meditation_tab = models.BooleanField()