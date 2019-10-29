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
    xslt_tree = etree.parse(os.path.join(BASE_DIR, 'app/data/' + 'countries.xsl'))
    transform = etree.XSLT(xslt_tree)

    tparams = {
        'year': datetime.now().year,
        'current': selection,
        'page': transform(root, selection=f'//{selection}')
    }

    return render(request, 'xslttest.html', tparams)
    '''
    print(prev)
    if not prev:
        print(f'//{selection}/')
        elements = tree.xpath(f'//{selection}')

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
    return render(request, 'listXSLT.xhtml', tparams)
'''

def rss(request):
    feeds = feedparser.parse('https://news.google.com/rss?hl=en-US&gl=US&ceid=US%3Aen&x=1571747254.2933')

    tparams = {
        'title': 'RSS',
        'message': 'Your application description page.',
        'year': datetime.now().year,
        'feeds': feeds,
    }
    return render(request, 'rss.html', tparams)