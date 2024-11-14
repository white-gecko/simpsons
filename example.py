from simpsons_rdf import simpsons, SIM, FAM

print({p: o for _, p, o in simpsons.graph.triples((SIM.Homer, None, None))})
print(
    [
        spouse
        for _, _, spouse in simpsons.graph.triples((SIM.Homer, FAM.hasSpouse, None))
    ]
)
print(simpsons.graph.serialize(format="turtle"))
