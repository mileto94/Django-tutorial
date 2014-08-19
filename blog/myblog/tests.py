import datetime
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from myblog.models import Article, Author


class ArticleMethodTest(TestCase):
    """docstring for ArticleMethodTest - it shoult return False
        if it was published in past or future"""
    def setUp(self):
        self.joe = Author(name="joe")

    def test_was_published_with_future_date(self):
        future_article = Article("21255", pub_date=timezone.now() + datetime.timedelta(days=30),
                                 author=self.joe)
        self.assertEqual(future_article.was_published_recently(), False)

    def test_was_published_recently(self):
        recent_article = Article("21255", pub_date=timezone.now() - datetime.timedelta(hours=1),
                                 author=self.joe)
        self.assertEqual(recent_article.was_published_recently(), True)

    def test_was_published_not_recently(self):
        old_article = Article("21255", pub_date=timezone.now() - datetime.timedelta(days=30),
                              author=self.joe)
        self.assertEqual(old_article.was_published_recently(), False)


class ArticleViewTest(TestCase):
    def create_article(title, text, days, author, rating, comment):
        return Article.objects.create(title=title,
                                      text=text,
                                      pub_date=timezone.now() + datetime.timedelta(days=days),
                                      author=author,
                                      rating=rating,
                                      comment=comment
                                      )

    def test_index_view_with_no_articles(self):
        response = self.client.get(reverse("myblog:index"))
        self.assertEqual(response.status_code, 200)
        # is done if there are no articles
        # self.assertContains(response, "No polls available")
        self.assertQuerysetEqual(response.context["latest_articles"], [])
