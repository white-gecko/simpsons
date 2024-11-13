from rdflib import Graph, Namespace
import importlib.resources

SIM = Namespace("https://simpsons.example.org/")
FAM = Namespace("https://vocab.example.org/family#")

class _Simpsons():
    _graph = None

    @property
    def graph(self):
        print("run")
        if self._graph is None:
            self._graph = Graph()
            with importlib.resources.path(__name__, "simpsons.ttl") as data_path:
                self._graph.parse(data_path, format="turtle")
        return self._graph

_simpsons = _Simpsons()
graph = getattr(_simpsons, "graph")
