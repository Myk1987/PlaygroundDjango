from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Cocktail, Ingredient, Components


def index(request):
    cocktail_list = Cocktail.objects.order_by('name')
    template = loader.get_template('bar/index.html')
    context = RequestContext(request, {'cocktail_list': cocktail_list, })

    return HttpResponse(template.render(context))


def cocktail_detail(request, cocktail_name):

    current_cocktail = get_object_or_404(Cocktail, link_name=cocktail_name)
    components_list = Components.objects.filter(cocktail=current_cocktail.id).order_by('amount')



    return render(request, 'bar/cocktail_detail.html', {'cocktail': current_cocktail,
                                                        'components_list': components_list,
                                                        })
