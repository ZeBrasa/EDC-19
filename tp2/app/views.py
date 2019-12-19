import urllib

from django.http import HttpRequest
from django.shortcuts import render
from datetime import datetime

import json
from s4api.graphdb_api import GraphDBApi
from s4api.swagger import ApiClient

from app import rules

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
    # print("selection = " + selection)
    elemType = selection.split("/")[-3]
    # print(elemType)

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
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                prefix mon: <http://www.semwebtech.org/mondial/10/meta#>
                select distinct ?attribute ?is ?what ?name
                where
                {	
                    {
                        <%s> ?attribute ?is .
                        optional { ?is mon:name ?what }
                    }
                    union
                    {
                        ?who ?is ?what .
                        <%s> mon:languageInfo ?who .
                        ?who rdf:type ?attribute .
                        optional { ?what mon:name ?name }
                    }
                    union
                    {
                        ?who ?is ?what .
                        <%s> mon:religionInfo ?who .
                        ?who rdf:type ?attribute .
                        optional { ?what mon:name ?name }
                    }
                }
                """
                % (selection, selection, selection))

    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,
                                 repo_name=repo_name)
    res = json.loads(res)

    if elemType == "mondial" or elemType == "continents":
        tparams = {
            'year': datetime.now().year,
            'elements': res['results']['bindings'],
        }
        return render(request, 'list.html', tparams)

    info = {}
    for e in res['results']['bindings']:
        val = ""
        attr = e['attribute']['value']
        if '#' in e['attribute']['value']:
            attr = attr.split("#", 1)[1]
        sub_attr = e['is']['value']
        if '#' in e['is']['value']:
            sub_attr = sub_attr.split("#", 1)[1]
        if 'what' in e:
            val = e['what']['value']
        if 'name' in e:
            val = (val, e['name']['value'])

        if val != "":
            if attr not in info:
                info.update({attr: {sub_attr: val}})
            elif sub_attr not in info[attr]:
                info[attr].update({sub_attr: val})
            elif isinstance(val, str):
                if val not in info[attr][sub_attr]:
                    info[attr][sub_attr] = [info[attr][sub_attr]] if isinstance(info[attr][sub_attr],(str, tuple))\
                        else info[attr][sub_attr]
                    info[attr][sub_attr].append(val)
            elif isinstance(val, tuple):
                if val[1] not in info[attr][sub_attr]:
                    info[attr][sub_attr] = [info[attr][sub_attr]] if isinstance(info[attr][sub_attr], (str, tuple))\
                        else info[attr][sub_attr]
                    info[attr][sub_attr].append(val)

        else:
            if 'general' not in info:
                info.update({'general': {attr: sub_attr}})
            elif attr not in info['general']:
                info['general'].update({attr: sub_attr})

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


def add_org(request):
    assert isinstance(request, HttpRequest)
    if 'name' in request.POST and 'acro' in request.POST and 'acro' in request.POST:
        name = request.POST['name']
        abbrev = request.POST['acro']
        members = request.POST.getlist('members[]')
        established = datetime.today().strftime('%Y-%m-%d')
        if name and abbrev:
            print(name)
            print(abbrev)
            print(established)
            print(members)
            basicInfo = (
                """
                prefix mon: <http://www.semwebtech.org/mondial/10/meta#>
                prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                insert data {
                    <http://www.semwebtech.org/mondial/10/organizations/%s/>    rdf:type mon:Organization ;
    			                                                                mon:name '%s' ;
        					                                                    mon:abbrev '%s';
        					                                                    mon:established '%s'
        		"""
            % (abbrev, name, abbrev, established))
            memberList = ""
            for member in members:
                memberList += (" ;\nmon:hasMember <%s>" % member)

            update = basicInfo + memberList + '}'
            print(update)
            payload_query = {"update": update}
            accessor.sparql_update(body=payload_query, repo_name=repo_name)
            return element(request, 'http://www.semwebtech.org/mondial/10/meta#Organization')

    query = (
        """
        prefix mon: <http://www.semwebtech.org/mondial/10/meta#>
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        select ?name ?item
        where {
            ?item rdf:type mon:Country .
            ?item mon:name ?name
        }
        """
    )
    payload_query = {"query": query}
    res = accessor.sparql_select(body=payload_query,
                                 repo_name=repo_name)
    res = json.loads(res)

    tparams = {
        'year': datetime.now().year,
        'countries': res['results']['bindings'],
    }

    return render(request, 'add_org.html', tparams)


def apply_inference():
    # dictionary for the rule
    rule = rules.code_country

    # carCode = 2 letter code of the country
    q_str = """ 
            prefix ns0: <http://xmlns.com/foaf/spec/>
            select distinct ?v
            where{
                ?sub ns0: carCode ?v
            }
            """
    result = query(q_str)
    result = result['results']['bindings']
    for r in result:
        value = r['v']['value']
        for pc in rule.keys():
            # incerto aqui neste if se está a fazer correctamente
            if int(value.split("-")[0]) >= pc[0] and int(value.split("-")[0]) <= pc[1]:
                region = rule[pc]
                # country code and the local name
                q_regional = """
                            prefix ns0: <http://xmlns.com/foaf/spec/>
                            select distinct ?o
                            where {
                                ?s ns0:carCode '""" + value + """'.
                                ?s ns0:localname ?o.
                            }
                            """
                res = query(q_regional)
                try:
                    reg = res['results']['bindings'][0]['o']['value']
                    region = reg.split()[0].replace(",", "") + ", " + region
                except Exception:
                    reg = ""

                qstr = """ 8
                            prefix ns0: <http://xmlns.com/foaf/spec/>
                            delete {?sub ns0:localname '""" + reg + """'}
                            where {?sub ns0:codeCar '""" + value + """'};
                            insert {?sub ns0:localname '""" + region + """'}
                            where {?sub ns0:codeCar '""" + value + """'}
                            """
                print(qstr)
                query(qstr)

    return


def query(str):
    query = str

    payload_query = {"query": query}
    try:
        res = accessor.sparql_select(body=payload_query, repo_name=repo_name)
        res = json.loads(res)
        return res
    except Exception:
        payload_query = {"update": query}
        res = accessor.sparql_update(body=payload_query, repo_name=repo_name)
        print(res)
