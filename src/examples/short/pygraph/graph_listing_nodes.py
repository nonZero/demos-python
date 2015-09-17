#!/usr/bin/python2

from __future__ import print_function
# Import the module and instantiate a graph object
from pygraph.classes.graph import graph
from pygraph.algorithms.searching import depth_first_search
gr = graph()
# Add nodes
gr.add_nodes(['X', 'Y', 'Z'])
gr.add_nodes(['A', 'B', 'C'])
# Add edges
gr.add_edge(('X', 'Y'))
gr.add_edge(('X', 'Z'))
gr.add_edge(('A', 'B'))
gr.add_edge(('A', 'C'))
gr.add_edge(('Y', 'B'))

print(gr.nodes())
