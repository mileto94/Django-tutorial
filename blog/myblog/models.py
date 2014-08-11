from django.db import models
from django.utils import timezone
import datetime


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("date published")
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
