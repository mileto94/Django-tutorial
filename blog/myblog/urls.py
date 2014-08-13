from django.conf.urls import patterns, url

from myblog import views

urlpatterns = patterns("",
                       url(r"^$", views.index, name="index"),
                       url(r"^(?P<article_id>\d+)/$", views.show_article,
                           name="show_article"),
                       url(r"^contact/$", views.contact,
                           name="contact"),
                       )
