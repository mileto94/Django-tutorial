from django.shortcuts import render, get_object_or_404, HttpResponse
from myblog.models import Article
from django.views.decorators.csrf import csrf_exempt


def index(request):
    latest_articles = Article.objects.order_by("-pub_date")[:5]
    context = {"latest_articles": latest_articles}
    return render(request, "myblog/index.html", context)


def oldest_news_index(request):
    oldest_news = Article.objects.order_by("-pub_date")[-5:]
    context = {"oldest_news": oldest_news}
    return render(request, "myblog/index.html", context)


@csrf_exempt
def show_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        article.rating += 1
        article.save()
        return HttpResponse("You've liked this article " + str(article.rating))
    return render(request, "myblog/show_article.html", {"article": article})


def contact(request):
    return render(request, "myblog/contact.html", {"contact": contact})
