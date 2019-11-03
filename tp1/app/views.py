import os

import feedparser
from django.http import HttpRequest
from django.shortcuts import render
from datetime import datetime


# Create your views here.

from lxml import etree
from tp1.settings import BASE_DIR

fname = 'mondial.xml'
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
        'message': 'Acerca do projecto',
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)


def list(request, selection, prev=None):
    print(selection)
    xsl = "list.xsl"

    if prev:
        print(prev)
        if prev == "continent":
            xpath = f'//*[@{prev}="{selection}"]/parent::*'

        elif ("cty" in selection) or ("city" in selection) or ("stadt" in selection):
            xpath = f'//*[@*="{selection}"]'

        elif "org" in selection:
            xpath = f'//*[@*="{selection}"]'

        else:
            xpath = f'//*[@id="{selection}"]/city'

    else:
        xpath = f'//{selection}'

    print(xpath)

    xslt_tree = etree.parse(os.path.join(BASE_DIR, 'app/data/' + xsl))
    transform = etree.XSLT(xslt_tree)
    tparams = {
        'year': datetime.now().year,
        'current': selection,
        'page': transform(root, selection=xpath),
    }

    return render(request, 'listDisplay.html', tparams)


def rss(request):
    feeds = feedparser.parse('https://news.google.com/rss?hl=en-US&gl=US&ceid=US%3Aen&x=1571747254.2933')

    tparams = {
        'title': 'RSS',
        'message': 'Noticias da Imprensa Americana',
        'year': datetime.now().year,
        'feeds': feeds,
    }
    return render(request, 'rss.html', tparams)