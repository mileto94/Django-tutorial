from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from myblog.models import Article
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.urlresolvers import reverse


def index(request):
    latest_articles = Article.objects.filter(pub_date__lte=timezone.now()
                                             ).order_by("-pub_date")[:5]
    context = {"latest_articles": latest_articles}
    return render(request, "myblog/index.html", context)


@csrf_exempt
def show_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        if request.POST.get("id"):
            article.rating += 1
            article.save()
            return HttpResponse(request.POST.get("id"))
        article.comment = request.POST.get("comment")
        article.save()
        return HttpResponse(article.comment)
    return render(request, "myblog/show_article.html", {"article": article})


def contact(request):
    return render(request, "myblog/contact.html", {"contact": contact})
