import os
from io import BytesIO
from xml import etree

import rdflib
from django.http import HttpRequest, Http404
from django.shortcuts import render
from datetime import datetime

import xml.dom.minidom
from rdflib import ConjunctiveGraph

import json
from s4api.graphdb_api import GraphDBApi
from s4api.swagger import ApiClient

endpoint = "http://localhost:7200"
repo_name = "mondial"
client = ApiClient(endpoint=endpoint)
accessor = GraphDBApi(client)

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


def countries(request):

    query = """
     prefix mon: <http://www.semwebtech.org/mondial/10/meta#>
     prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
     select ?cname ?country
     where {
        ?country rdf:type mon:Country .
        ?country mon:name ?cname
    }
    """

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,
                                 repo_name=repo_name)
    res = json.loads(res)
    for e in res['results']['bindings']:
        print(e)

    tparams = {
        'title': 'Graphs',
        'message': 'Your application description page.',
        'year': datetime.now().year,
        'elements': res['results']['bindings'],
    }
    return render(request, 'list.html', tparams)
