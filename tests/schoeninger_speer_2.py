# Creates teh CIDOC-CRM graph of the Schoeninger Speer II event (after S. Stead, and https://www.cidoc-crm.org/Entity/e16-measurement/version-6.2)

import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes with their respective labels
G.add_node("E16", label="E16 Measurement (C14 dating of Schoeninger Speer II)")
G.add_node("E52_dating", label="E52 Time-Span (time-span of C14 dating)")
G.add_node("E52_1996", label="E52 Time-Span (year 1996)")

# Add edges with properties as labels
G.add_edge("E16", "E52_dating", label="P4 has time-span")
G.add_edge("E52_dating", "E52_1996", label="P86 falls within")

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=7000, node_color="skyblue")
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color="k")
nx.draw_networkx_labels(G, pos, font_size=10)
nx.draw_networkx_edge_labels(G, pos, font_size=10, edge_labels=nx.get_edge_attributes(G, 'label'))

# Show plot
plt.title("CIDOC-CRM Graph for Schoeninger Speer II")
plt.axis('off')  # Turn off the axis
plt.show()
