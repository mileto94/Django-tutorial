from django.shortcuts import render, get_object_or_404, HttpResponse
from myblog.models import Article
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


def index(request):
    latest_articles = Article.objects.filter(pub_date__lte=timezone.now()
                                             ).order_by("-pub_date")[:5]
    context = {"latest_articles": latest_articles}
    return render(request, "myblog/index.html", context)


def oldest_news_index(request):
    news = Article.objects.filter(pub_date__lte=timezone.now()
                                  ).order_by("-pub_date")
    oldest_news = news[len(news) - 5:]
    context = {"oldest_news": oldest_news}
    return render(request, "myblog/index.html", context)


@csrf_exempt
def show_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        # if str(request.POST.get("comment")):
        #     return HttpResponse("Thank you for leaving a comment :)")
        article.rating += 1
        article.save()
        # return HttpResponse("You've liked this article " + str(article.rating))
        return HttpResponse(str(request.POST.get("id")))
    return render(request, "myblog/show_article.html", {"article": article})


def contact(request):
    return render(request, "myblog/contact.html", {"contact": contact})
