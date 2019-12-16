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
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        select ?country ?is ?what ?name
        where {
            <http://www.semwebtech.org/mondial/10/countries/P/> ?is ?what .
            optional { ?what mon:name ?name }
        }
        """
        )

payload_query = {"query": query}
res = accessor.sparql_select(body=payload_query,
                             repo_name=repo_name)

res = json.loads(res)
info = {}
for e in res['results']['bindings']:
    #print(e)
    if 'name' in e:
        info.update({e['is']['value'].split("#", 1)[1]: e['name']['value']})
        #print(f"{e['is']['value']} -> {e['name']['value']}")
    else:
        info.update({e['is']['value'].split("#", 1)[1]: e['what']['value']})
        #print(f"{e['is']['value']} -> {e['what']['value']}")

print(info)