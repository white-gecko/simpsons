from simpsons import graph, SIM

def test_simpsons():
    assert len(list(graph.triples((SIM.Homer, None, None)))) > 0
