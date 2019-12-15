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


def list(request, selection):
    query = (
            """
            prefix mon: <http://www.semwebtech.org/mondial/10/meta#>
            prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            select ?cname ?country
            where {
                ?country rdf:type mon:%s .
                ?country mon:name ?cname
            }
            """
            % selection)
    #print(query)
    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,
                                 repo_name=repo_name)
    res = json.loads(res)
    for e in res['results']['bindings']:
        print(e)

    tparams = {
        'title': selection,
        'message': 'Your application description page.',
        'year': datetime.now().year,
        'elements': res['results']['bindings'],
    }
    return render(request, 'list.html', tparams)
