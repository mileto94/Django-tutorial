from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)


class Article(models.Model):
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("date published")
    author = models.ForeignKey(Author)
