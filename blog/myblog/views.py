from django.shortcuts import render
from django.http import HttpResponse
from myblog.models import Article


def index(request):
    latest_articles = Article.objects.order_by("-pub_date")[:5]
    context = {"latest_articles": latest_articles}
    return render(request, "myblog/index.html", context)


def show_article(request, article_id):
    return HttpResponse("You're looking for %s" % article_id)
