# from django.shortcuts import render
from django.http import HttpResponse
from myblog.models import Article
from django.template import RequestContext, loader


def index(request):
    latest_articles = Article.objects.order_by("-pub_date")[:5]
    template = loader.get_template("myblog/index.html")
    context = RequestContext(request, {"latest_articles": latest_articles})
    return HttpResponse(template.render(context))


def show_article(request, article_id):
    return HttpResponse("You're looking for %s" % article_id)
