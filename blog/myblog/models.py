from django.db import models
from django.utils import timezone
import datetime


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    # title = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("date published")
    author = models.ForeignKey(Author)
    # image = models.ImageField(height_field=600, width_field=500)

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"
