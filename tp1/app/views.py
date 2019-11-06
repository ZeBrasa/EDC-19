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


def list(request, selection):
    #print(selection)
    xsl = "simpleList.xsl"

    if selection == "continent" or selection == "country" or selection == "organization":
        xpath = f'//{selection}'

    elif ("cty" in selection) or ("city" in selection) or ("stadt" in selection):
        xpath = f'//*[@id="{selection}"]'
        xsl = 'city.xsl'

    elif ("europe" in selection) or ("asia" in selection) or ("africa" in selection) or ("america" in selection) or ("australia" in selection):
        xpath = f'//country/encompassed[@continent="{selection}"]/parent::*'

    elif "org" in selection:
        xpath = f'//organization[@id="{selection}"]'
        xsl = 'organization.xsl'

    else:
        xpath = f'//country[@id="{selection}"]'
        xsl = 'country.xsl'
    #print(xpath)

    xslt_tree = etree.parse(os.path.join(BASE_DIR, 'app/data/' + xsl))
    transform = etree.XSLT(xslt_tree)
    print(transform(root, selection=xpath))
    tparams = {
        'year': datetime.now().year,
        'current': selection,
        'page': transform(root, selection=xpath),
    }

    return render(request, 'xsltDisplay.html', tparams)


def rss(request):
    feeds = feedparser.parse('https://news.google.com/rss?hl=en-US&gl=US&ceid=US%3Aen&x=1571747254.2933')

    tparams = {
        'title': 'RSS',
        'message': 'Noticias da Imprensa Americana',
        'year': datetime.now().year,
        'feeds': feeds,
    }
    return render(request, 'rss.html', tparams)
