from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from myblog.models import Article
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.urlresolvers import reverse


def index(request):
    latest_articles = Article.objects.filter(pub_date__lte=timezone.now()
                                             ).order_by("-pub_date")[:5]
    most_rated = Article.objects.order_by("-rating")[:3]
    for article in most_rated:
        if article.text.count(".") > 1:
            current = article.text.split(".")
            article.text = current[0] + ". " + current[1]
        else:
            article.text = article.text[:30]
    context = {"latest_articles": latest_articles, "most_rated": most_rated}
    return render(request, "myblog/index.html", context)


@csrf_exempt
def show_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        if request.POST.get("id"):
            article.rating += 1
            article.save()
            print("show_article - like")
            return HttpResponse(request.POST.get("id"))
        article.comment = request.POST.get("comment")
        article.save()
        print("show_article - send comment")
        return HttpResponse(article.comment)
    print("show_article - get")
    return render(request, "myblog/show_article.html", {"article": article})


def contact(request):
    return render(request, "myblog/contact.html", {"contact": contact})
