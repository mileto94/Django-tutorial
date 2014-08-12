from django.contrib import admin
from myblog.models import Article, Author
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [(None,          {"fields": ["text"]}),
                 ("Author",      {"fields": ["author"]}),
                 ("Date info",   {"fields": ["pub_date"], "classes": ["collapse"]}),
                 ]

    list_display = ("text", "author", "pub_date", "was_published_recently")

    list_filter = ["pub_date"]

    search_fields = ["text"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
