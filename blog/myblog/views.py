# from django.shortcuts import render
from django.http import HttpResponse
from myblog.models import Article


def index(request):
    latest_articles = Article.objects.order_by("-pub_date")[:5]
    output = ", ".join([a.text for a in latest_articles])
    return HttpResponse(output)


def show_article(request, article_id):
    return HttpResponse("You're looking for %s" % article_id)
