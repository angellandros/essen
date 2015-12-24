from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from models import Esser, Mittagessen


def index(request):
    return render(request, 'site_base.html')


def detail(request, esser):
    mahlzeiten = Mittagessen.objects.filter(person=esser)
    template = loader.get_template('mittagessen/details.html')
    context = {
        'esser': esser,
        'mahlzeiten': mahlzeiten,
    }
    return HttpResponse(template.render(context, request))


def detail_by_id(request, esser_id):
    try:
        esser = Esser.objects.get(id=esser_id)
        return detail(request, esser)
    except ObjectDoesNotExist:
        return HttpResponse("The bloody Esser not found.", status=404)


def detail_by_email(request, esser_team, esser_id_name):
    try:
        email = '%s@%s.ir' % (esser_id_name, esser_team)
        esser = Esser.objects.get(email=email)
        return detail(request, esser)
    except ObjectDoesNotExist:
        return HttpResponse("The bloody Esser not found.", status=404)
