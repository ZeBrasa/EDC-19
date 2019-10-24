import os

import feedparser
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


def list(request, prev, selection):
    print(f'/{prev}[@name="{selection}"]/*')

    elements = tree.xpath(f'/{prev}[@name="{selection}"]/*')
    print(elements)

    tparams = {
            'title': f'{selection}',
            'message': 'List:',
            'year': datetime.now().year,
            'current': selection,
            'selection': elements,
    }
    return render(request, 'list.html', tparams)


def continents(request):
    elements = tree.xpath('/mondial/continent/@name')

    tparams = {
        'title': 'Continents',
        'message': 'List of continents',
        'year': datetime.now().year,
        'current': 'continent',
        'elements': elements,
    }
    return render(request, 'continents.html', tparams)


def countries(request):
    country_names = tree.xpath('/mondial/country/@name')

    tparams = {
        'title': 'Countries',
        'message': 'List of countries',
        'year': datetime.now().year,
        'current': 'country',
        'elements': country_names,
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


def rss(request):
    feeds = feedparser.parse('http://feeds.jn.pt/JN-Mundo')

    tparams = {
        'title': 'RSS',
        'message': 'Your application description page.',
        'year': datetime.now().year,
        'feeds': feeds,
    }
    return render(request, 'rss.html', tparams)