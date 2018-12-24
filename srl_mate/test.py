import requests
import rdflib

g = rdflib.Graph()

url = 'http://192.168.1.97:8072/parse'

params = {'sentence':"我想知道你是谁？",'returnType':'rdf'}
r = requests.post(url,data=params,  headers={'content-type':'application/x-www-form-urlencoded'})
print(r.status_code)
print(r.content.decode())

rdf_out = r.content.decode()

g.parse(data=rdf_out, format="n3" )
print(len(g))
for s,p,o in g:
    print(s,p,o)


output = []
for s, p, o in g:
    if type(o) == rdflib.term.Literal:
        output.append(o.toPython())

print(', '.join(output))


result = g.parse(data=rdf_out, format='n3')
print(len(g))
for stmt in g:
    print(stmt)


