from simpsons_rdf import simpsons, SIM
from rdflib import URIRef


def test_simpsons():
    assert len(list(simpsons.graph.triples((SIM.Homer, None, None)))) > 0

def test_simpsons():
    assert simpsons.graph.identifier == URIRef("https://simpsons.example.org/")
