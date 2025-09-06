from rdflib import URIRef

from simpsons_rdf import SIM, simpsons


def test_simpsons_homer_exists():
    """Check if any triple with Homer as subject exists."""
    assert len(list(simpsons.graph.triples((SIM.Homer, None, None)))) > 0


def test_simpsons_graph_identifier():
    """Check if the graph identifier is as expected."""
    assert simpsons.graph.identifier == URIRef("https://simpsons.example.org/")


def test_simpsons_get_file():
    """Check if the graph identifier is as expected."""
    assert simpsons.graph_file.name == "simpsons.ttl"
    assert simpsons.graph_file.exists()
