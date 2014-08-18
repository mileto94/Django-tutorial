from django.db import models
from django.utils import timezone
import datetime


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=30, default="")
    text = models.TextField(max_length=1000000000)
    pub_date = models.DateTimeField("date published")
    author = models.ForeignKey(Author)
    # image = models.ImageField(height_field=600, width_field=500)
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=300, default="")

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=5)
    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"
