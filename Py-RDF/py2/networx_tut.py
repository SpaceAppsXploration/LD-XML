import networkx as nx
import matplotlib.pyplot as pl

G = nx.Graph()
G.add_node(1)
G.add_node(2)

e = (1, 2)
G.add_edge(*e)

G.add_node("spam")

nx.connected_components(G)

A=nx.to_agraph(G)

B=nx.draw(G)

pl.show()




