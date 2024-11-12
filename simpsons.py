from rdflib import Graph, Namespace
import importlib.resources

SIM = Namespace("http://simpsons.example.org/")

graph = Graph()
with importlib.resources.path(__name__, "simpsons.ttl") as data_path:
    graph.parse(data_path, format="turtle")
