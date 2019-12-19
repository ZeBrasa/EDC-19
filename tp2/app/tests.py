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
select distinct ?attribute ?is ?what ?name
where
{	
    {
 		<http://www.semwebtech.org/mondial/10/countries/D/> ?attribute ?is .
		optional { ?is mon:name ?what }
    }
    union
	{
     	?who ?is ?what .
       	<http://www.semwebtech.org/mondial/10/countries/D/> mon:languageInfo ?who .
       	?who rdf:type ?attribute .
      	optional { ?what mon:name ?name }
    }
   	union
    {
        ?who ?is ?what .
       	<http://www.semwebtech.org/mondial/10/countries/D/> mon:religionInfo ?who .
       	?who rdf:type ?attribute .
      	optional { ?what mon:name ?name }
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
                info[attr][sub_attr] = [info[attr][sub_attr]] if isinstance(info[attr][sub_attr], (str, tuple)) else info[attr][sub_attr]
                info[attr][sub_attr].append(val)
        elif isinstance(val, tuple):
            if val[1] not in info[attr][sub_attr]:
                info[attr][sub_attr] = [info[attr][sub_attr]] if isinstance(info[attr][sub_attr], (str, tuple)) else info[attr][sub_attr]
                info[attr][sub_attr].append(val)


    else:
        if 'general' not in info:
            info.update({'general': {attr: sub_attr}})
        elif attr not in info['general']:
            info['general'].update({attr: sub_attr})


with open("dict.json", 'w') as f:
    f.write(json.dumps(info, indent=2))
#print(json.dumps(info, indent=2))
print(info['SpokenBy']['onLanguage'][1])
