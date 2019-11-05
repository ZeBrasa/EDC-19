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
    #print(selection)
    xsl = "simpleList.xsl"

    if prev:
        print(prev)
        if prev == "continent":
            xpath = f'//*[@{prev}="{selection}"]/parent::*'
            title = "'Countries'"

        elif ("cty" in selection) or ("city" in selection) or ("stadt" in selection):
            xpath = f'//*[@*="{selection}"]'
            title = "'?'"
            #xsl = 'state.xsl'

        elif "org" in selection:
            xpath = f'//*[@*="{selection}"]'
            title = "'Organization'"
            xsl = 'listOrg.xsl'

        else:
            xpath = f'//*[@id="{selection}"]'
            title = "'Cities'"
            xsl = 'country.xsl'

    else:
        xpath = f'//{selection}'
        title = f"'{selection}'"

    #print(xpath)

    '''
    if "continent" in selection:
        xslt_tree = etree.parse(os.path.join(BASE_DIR, 'app/data/' + "listContinent.xsl"))
    elif "org" in selection:
        xslt_tree = etree.parse(os.path.join(BASE_DIR, 'app/data/' + "listOrg.xsl"))
    else:
    '''

    xslt_tree = etree.parse(os.path.join(BASE_DIR, 'app/data/' + xsl))
    transform = etree.XSLT(xslt_tree)
    #print(transform(root, selection=xpath, header=title))
    tparams = {
        'year': datetime.now().year,
        'current': selection,
        'page': transform(root, selection=xpath, header=title),
    }

    return render(request, 'xsltDisplay.html', tparams)


def save_city_info(request):
    print(request.POST)

    c_country = request.POST.get("country")
    c_id = request.POST.get("id")
    c_name = request.POST.get("name")
    c_lat = request.POST.get("latitude")
    c_lon = request.POST.get("longitude")
    c_elev = request.POST.get("elevation")
    c_date = request.POST.get("year")
    c_pop = request.POST.get("population")

    q_str = "xquery for $a in collection('Mondial')//continent/country" \
            "where contains ($a/cityID, {} " \
            "return replace node $a with " \
            "<city id = {} country = {}>" \
                "<name>{}</name>" \
                "<latitude>{}</latitude>" \
                "<longitude>{}</longitude>" \
                "<elevation>{}</elevation>" \
                "<population date={}></population>" \
            "</city>".format(c_id,c_country,c_name,c_lat,c_lon,c_elev,c_date,c_pop)

    XMLinsert(q_str)

    c_info={[]}
    c_info[0].append(c_name)
    c_info[1].append(c_lat)
    c_info[2].append(c_lon)
    c_info[3].append(c_elev)
    c_info[4].append(c_pop)

    return render(request,"listDisplay.html",{
        "city" : c_info,
        "name" : c_name,
    })


def rss(request):
    feeds = feedparser.parse('https://news.google.com/rss?hl=en-US&gl=US&ceid=US%3Aen&x=1571747254.2933')

    tparams = {
        'title': 'RSS',
        'message': 'Noticias da Imprensa Americana',
        'year': datetime.now().year,
        'feeds': feeds,
    }
    return render(request, 'rss.html', tparams)

def XMLinsert(str):
    session = app.BaseXClient.Session('localhost',1984,'admin','admin')  #pelo o que vi, cria-se uma sessão pelo BaseX
    try:
        session.execute(str)
    finally:
        if session:
            session.close()
