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


def list(request, selection, prev=None):
    print(prev)
    if not prev:
        print(f'//{selection}/')
        elements = tree.xpath(f'//{selection}')
        print(type(elements))
        print(elements[0].get("name"))

    else:
        print(f'/{prev}[@id="{selection}"]/*')
        elements = tree.xpath(f'/{prev}[@id="{selection}"]/*')
        selection = prev.append("/" + selection)

    tparams = {
            'title': f'{selection}',
            'message': 'List:',
            'year': datetime.now().year,
            'current': selection,
            'elements': elements,
    }
    return render(request, 'list.html', tparams)


def rss(request):
    feeds = feedparser.parse('http://feeds.jn.pt/JN-Mundo')

    tparams = {
        'title': 'RSS',
        'message': 'Your application description page.',
        'year': datetime.now().year,
        'feeds': feeds,
    }
    return render(request, 'rss.html', tparams)