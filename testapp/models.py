from django.db import models

class Test(models.Model):
    string_field = models.TextField()
    char_field = models.CharField()
    int_field = models.IntegerField()
    boolean_field = models.BooleanField()
    decimal_field = models.DecimalField(max_digits=100, decimal_places=2)
    time_field = models.TimeField()
    date_field = models.DateField() 
    url_field = models.URLField()