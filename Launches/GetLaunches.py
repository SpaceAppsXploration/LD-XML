from rdflib import Graph, term
from rdflib.namespace import SKOS

def get_links():
    links = []

    g1 = Graph()
    result1 = g1.parse(u'http://dbpedia.org/page/Category:Spacecraft_by_year_of_launch')

    for s in g1.subjects(predicate=SKOS.broader, object=None):
        links.append(s)

    return links

def get_launches(link):
    launches = []

    DUBLIN = term.URIRef(u'http://purl.org/dc/terms/subject')

    g2 = Graph()
    result2 = g2.parse(link)

    for s in g2.subjects(predicate=DUBLIN, object=None):
        launches.append(s + "\n")

    return launches

links = get_links()

for link in links:
    launches = get_launches(link)
    
    out_file = open(link[-4:], "w")
    out_file.writelines(launches)
    out_file.close()