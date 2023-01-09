import circuitgraph as cg

c = cg.from_file('../netlists/adder.v')
# Add an AND gate to the circuit that takes as input nets o0, o1, o2, o3
#c.add('g', 'and', fanin=[f'o{i}' for i in range(4)])
print(c.nodes())
print(c.edges())
cg.to_file(c, '../output/adder.v')
