import rdflib
from django.test import TestCase

# Create your tests here.
import json
from s4api.graphdb_api import GraphDBApi
from s4api.swagger import ApiClient

endpoint = "http://localhost:7200"
repo_name = "mondial"
client = ApiClient(endpoint=endpoint)
accessor = GraphDBApi(client)

query = ("""
        prefix mon: <http://www.semwebtech.org/mondial/10/meta#>
        select distinct ?attribute ?is ?what
        where {
            {
                <http://www.semwebtech.org/mondial/10/countries/P/> ?attribute ?is .
                optional { ?is mon:name ?what }
            }
            union      
            {
                ?who ?is ?what .
                <http://www.semwebtech.org/mondial/10/countries/P/> ?attribute ?who
            }      
        }
        """
         )

payload_query = {"query": query}
res = accessor.sparql_select(body=payload_query,
                             repo_name=repo_name)

res = json.loads(res)
#print(res['results']['bindings'])

info = {}
val = ""
for e in res['results']['bindings']:
    attr = e['attribute']['value'].split("#", 1)[1]
    sub_attr = e['is']['value']
    if '#' in e['is']['value']:
        sub_attr = sub_attr.split("#", 1)[1]
    if 'what' in e:
        val = e['what']['value']

    if "node" not in val and "node" not in sub_attr:
        if val != "":
            if attr not in info:
                info.update({attr: {sub_attr: val}})
            elif sub_attr not in info[attr]:
                info[attr].update({sub_attr: val})
            elif val not in info[attr][sub_attr]:
                info[attr][sub_attr] = [info[attr][sub_attr]] if isinstance(info[attr][sub_attr], str) else info[attr][sub_attr]
                info[attr][sub_attr].append(val)

        else:
            if 'general' not in info:
                info.update({'general': {attr: sub_attr}})
            elif attr not in info['general']:
                info['general'].update({attr: sub_attr})

print(json.dumps(info, indent=4))

#print(info)
print(info['general']['name'])
