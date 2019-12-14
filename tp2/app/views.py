import os

import rdflib
from django.http import HttpRequest, Http404
from django.shortcuts import render
from datetime import datetime

from rdflib import ConjunctiveGraph

# Create your views here.


def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
    }
    return render(request, 'index.html', tparams)


def contact(request):
    tparams = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    }
    return render(request, 'contact.html', tparams)


def about(request):
    tparams = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)


def graphs(request):
    graph = ConjunctiveGraph()
    graph.parse('app/data/mondial.rdf', format="xml")
    qres = graph.query(
        """
        prefix mon: <http://www.semwebtech.org/mondial/10/meta#>
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        select ?cname
        where {
            ?city mon:name 'London' .
            ?country rdf:type mon:Country .
            ?country mon:capital ?city .
            ?country mon:name ?cname
        }
        """
    )

    tparams = {
        'title': 'Graphs',
        'message': 'Your application description page.',
        'year': datetime.now().year,
        'elements': qres,
    }
    return render(request, 'list.html', tparams)
