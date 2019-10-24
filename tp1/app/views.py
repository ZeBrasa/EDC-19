import os

from django.http import HttpRequest
from django.shortcuts import render
from datetime import datetime


# Create your views here.

from lxml import etree
from tp1.settings import BASE_DIR

fname = 'Mondial.xml'
pname = os.path.join(BASE_DIR, 'app/data/' + fname)
tree = etree.parse(pname)
root = tree.getroot()

def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
    }
    return render(request, 'index.html', tparams)


def about(request):
    tparams = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)


def list(request):
    assert isinstance(request, HttpRequest)

    if 'selection' in request.POST:
        print("selection")
        selection = request.POST['selection']

        elements = tree.xpath('//[@name="selection"]/@name')

        tparams = {
            'title': '...',
            'message': 'List of ...',
            'year': datetime.now().year,
            'selection': elements,
        }
        return render(request, 'list.html', tparams)

    else:
        print("nope")
        print(request.POST)
        continent_names = tree.xpath('/mondial/continent/@name')

        tparams = {
            'title': 'Continents',
            'message': 'List of continents',
            'year': datetime.now().year,
            'elements': continent_names,
        }
        return render(request, 'continents.html', tparams)

def continents(request):
    continent_names = tree.xpath('/mondial/continent/@name')

    tparams = {
        'title': 'Continents',
        'message': 'List of continents',
        'year': datetime.now().year,
        'continents': continent_names,
    }
    return render(request, 'continents.html', tparams)


def countries(request):
    country_names = tree.xpath('/mondial/country/@name')

    tparams = {
        'title': 'Countries',
        'message': 'List of countries',
        'year': datetime.now().year,
        'countries': country_names,
    }
    return render(request, 'countries.html', tparams)


def organizations(request):
    organization_names = tree.xpath('/mondial/organization/@name')

    tparams = {
        'title': 'Organizations',
        'message': 'List of organizations',
        'year': datetime.now().year,
        'organizations': organization_names,
    }
    return render(request, 'organizations.html', tparams)