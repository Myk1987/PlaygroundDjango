from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext, loader

from .models import Cocktail


def index(request):
    cocktail_list = Cocktail.objects.order_by('name')
    template = loader.get_template('bar/index.html')
    context = RequestContext(request,
                             {'cocktail_list': cocktail_list, }
                             )
    return HttpResponse(template.render(context))
