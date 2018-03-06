from django.db import models


class Writer(models.Model):
    writer_name = models.CharField(max_length=200)
    dateOfBirth = models.DateTimeField('date published')

