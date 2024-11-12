from rdflib import Graph, Namespace
import importlib.resources

SIM = Namespace("https://simpsons.example.org/")
FAM = Namespace("https://vocab.example.org/family#")

graph = Graph()
with importlib.resources.path(__name__, "simpsons.ttl") as data_path:
    graph.parse(data_path, format="turtle")
