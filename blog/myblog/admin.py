from django.contrib import admin
from myblog.models import Article, Author


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [(None,          {"fields": ["title"]}),
                 (None,          {"fields": ["text"]}),
                 ("Author",      {"fields": ["author"]}),
                 ("Date info",   {"fields": ["pub_date"], "classes": ["collapse"]}),
                 (0,             {"fields": ["rating"]}),
                 (None,          {"fields": ["comment"]}),
                 ("Image URL",   {"fields": ["image"]}),
                 ("Image URL",   {"fields": ["slider_image"]}),
                 ]

    list_display = ("title", "text", "pub_date",
                    "was_published_recently", "rating", "comment", "image", "slider_image")

    list_filter = ["pub_date"]

    search_fields = ["title"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
