import os
import grakel
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from scipy.spatial import distance
from sklearn import decomposition, manifold
import umap.umap_ as umap

import warnings
warnings.filterwarnings("ignore")

def edit_distance(graph1, graph2, node_attr='h', edge_attr='e', upper_bound=100, indel_mul=1, sub_mul=1):
    """
    Calculates exact graph edit distance between 2 graphs.

    Args:
    graph1 : networkx graph, graph with node and edge attributes 
    graph2 : networkx graph, graph with node and edge attributes 
    node_attr : str, key for node attribute
    edge_attr : str, key for edge attribute
    upper_bound : int, maximum edit distance to consider
    indel_mul: float, insertion/deletion cost
    sub_mul: float, substitution cost

    Returns:
    np.float, distance, how similar graph1 is to graph2
    """
    def node_substitution_scoring(dict_1, dict_2):
        """Calculates node substitution score."""
        multiplier = sub_mul
        
        return multiplier*(distance.jaccard(
            dict_1[node_attr], dict_2[node_attr]))
    
    def constant_value(dict_1):
        """Returns constant score for insertion/deletion."""
        return indel_mul

    graph1 = feature_conversion(graph1, node_attr, edge_attr)
    graph2 = feature_conversion(graph2, node_attr, edge_attr)

    return min(
        nx.optimize_graph_edit_distance(
        graph1, graph2, 
            node_subst_cost = node_substitution_scoring,
            upper_bound  = upper_bound,
            node_del_cost = constant_value, 
            node_ins_cost = constant_value, 
            edge_del_cost = constant_value, 
            edge_ins_cost = constant_value, 
        ))

def feature_conversion(graph, node_attr, edge_attr):
    """Converts networkx graph features from tensors to np array."""
    for node in graph.nodes:
        graph.nodes[node][node_attr] = np.array(graph.nodes[node][node_attr])
    for edge in graph.edges:
        graph.edges[edge][edge_attr] = np.array(graph.edges[edge][edge_attr])
    return graph