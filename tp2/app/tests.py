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

selection = 'Country'
query = ("""
            prefix mon: <http://www.semwebtech.org/mondial/10/meta#>
            prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            select ?cname
            where {
               ?country rdf:type mon:%s .
               ?country mon:name ?cname
           }
           """
         % selection)

payload_query = {"query": query}
res = accessor.sparql_select(body=payload_query,
                             repo_name=repo_name)
res = json.loads(res)
for e in res['results']['bindings']:
    print(e)
