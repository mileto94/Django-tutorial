from django.forms import ModelForm
# from django import forms
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        # fields = ["title", "text", "author", "pub_date", "rating", "comment"]
        fields = "__all__"

# form = ArticleForm()
