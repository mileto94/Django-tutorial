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


def create_article(title, text, days, author_name, rating, comment):
    author = Author(name=author_name)
    author.save()
    return Article.objects.create(title=title,
                                  text=text,
                                  pub_date=timezone.now() + datetime.timedelta(days=days),
                                  author=author,
                                  rating=rating,
                                  comment=comment
                                  )


class ArticleViewTest(TestCase):
    def test_index_view_with_no_articles(self):
        response = self.client.get(reverse("myblog:index"))
        self.assertEqual(response.status_code, 200)
        # is done if there are no articles
        # self.assertContains(response, "No polls available")
        self.assertQuerysetEqual(response.context["latest_articles"], [])

    def test_index_view_with_past_article(self):
        create_article("James", "Arthur", -30, "joe", 3, "Nice")
        response = self.client.get(reverse("myblog:index"))
        self.assertQuerysetEqual(response.context["latest_articles"],
                                 ["<Article: James>"])

    def test_index_view_with_future_article(self):
        create_article("Homer", "Simpsons", 30, "Emily", 3, "Good")
        response = self.client.get(reverse("myblog:index"))
        self.assertQuerysetEqual(response.context["latest_articles"], [])
