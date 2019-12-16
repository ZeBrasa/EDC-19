import urllib

from django.shortcuts import render
from datetime import datetime

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


def element(request, selection):
    selection = urllib.parse.unquote(selection)
    elemType = selection.split("/")[-3]
    print(elemType)

    if elemType == 'mondial':
        query = (
                """
                prefix mon: <http://www.semwebtech.org/mondial/10/meta#>
                prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                select ?name ?item
                where {
                    ?item rdf:type <%s> .
                    ?item mon:name ?name
                }
                """
                % selection)

    elif elemType == 'continents':
        query = (
                """
                prefix mon: <http://www.semwebtech.org/mondial/10/meta#>
                select ?name ?item
                where {
                    ?item mon:encompassed <%s> .
                    ?item mon:name ?name
                }
                """
                % selection)

    else:
        query = (
                """
                prefix mon: <http://www.semwebtech.org/mondial/10/meta#>
                prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                select ?is ?what ?name
                where {
                    <%s> ?is ?what .
                    optional { ?what mon:name ?name }
                }
                """
                % selection)

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,
                                 repo_name=repo_name)
    res = json.loads(res)

    if elemType == "mondial" or elemType == "continents":
        tparams = {
            'title': selection,
            'message': 'Your application description page.',
            'year': datetime.now().year,
            'elements': res['results']['bindings'],
        }
        return render(request, 'list.html', tparams)

    info = {}
    for e in res['results']['bindings']:
        if 'name' in e:
            info.update({e['is']['value'].split("#", 1)[1]: e['name']['value']})
        else:
            info.update({e['is']['value'].split("#", 1)[1]: e['what']['value']})

    tparams = {
        'title': selection,
        'message': 'Your application description page.',
        'year': datetime.now().year,
        'info': info,
    }

    if elemType == "countries":
        return render(request, 'country.html', tparams)

    elif elemType == "cities":
        return render(request, 'city.html', tparams)

    elif elemType == "organizations":
        return render(request, 'org.html', tparams)
