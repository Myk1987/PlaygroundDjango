from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^ingredients/$', views.ingredients, name='ingredients'),
               url(r'^(?P<cocktail_name>[A-Za-z0-9_.-]+)/$', views.cocktail_detail, name='cocktail_detail'),
               ]

