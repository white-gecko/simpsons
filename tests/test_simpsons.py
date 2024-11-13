from simpsons import simpsons, SIM

def test_simpsons():
    assert len(list(simpsons.graph.triples((SIM.Homer, None, None)))) > 0
