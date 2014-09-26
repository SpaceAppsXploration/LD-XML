##############################################################################################
# Py3.3 script to navigate DBpedia URIs
# install latest RDFlib with 'pip install rdflib'
# https://github.com/RDFLib/rdflib/
##############################################################################################

from rdflib import Graph, term
from rdflib.namespace import SKOS


def print_list():
    ### These lines print the list of links about pages containing spacecraft launched per year

    # create the empty graph
    g1 = Graph()
    # load the graph from URI of the document
    result1 = g1.parse(u'http://dbpedia.org/page/Category:Spacecraft_by_year_of_launch')

    # print length of doc
    print("graph has %s statements." % len(g1))

    # filter the entities in the doc by the predicate SKOS:broader (W3C standard)
    for s in g1.subjects(predicate=SKOS.broader, object=None):
        print(s)

print_list()


def print_1968_launches():
    ### These lines print the links to actual pages about each spacecraft launched in 1968, for example

    # load the term for the predicate we are going to filter (Dublin Core Standard)
    DUBLIN = term.URIRef(u'http://purl.org/dc/terms/subject')

    # same procedure as above
    g2 = Graph()
    result2 = g2.parse(u'http://dbpedia.org/resource/Category:Spacecraft_launched_in_1968')

    print("graph has %s statements." % len(g2))


    for s in g2.subjects(predicate=DUBLIN, object=None):
        print(s)

print_1968_launches()