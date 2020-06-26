from django.db import models

# Create your models here.
class todo(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

class todoweek(models.Model):
    content_week = models.TextField()

    def __str__(self):
        return self.content_week

class todomonth(models.Model):
    content_month = models.TextField()

    def __str__(self):
        return self.content_month
