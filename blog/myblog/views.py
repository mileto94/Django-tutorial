from django.shortcuts import render
from django.http import Http404
from myblog.models import Article


def index(request):
    latest_articles = Article.objects.order_by("-pub_date")[:5]
    context = {"latest_articles": latest_articles}
    return render(request, "myblog/index.html", context)


def show_article(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, "myblog/base.html", {"article": article})
