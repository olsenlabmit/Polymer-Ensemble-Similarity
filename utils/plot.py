import matplotlib.pyplot as plt
import networkx as nx

def graph(tmp_graph):
    """Plots networkx graph."""
    node_list = [
        tmp_graph.nodes[idx]['label'] 
            for idx in range(len(tmp_graph.nodes))]
    nx.draw_networkx(tmp_graph)
    node_dict = dict(zip(range(len(node_list)), node_list))   
    print(node_dict)
    pos = nx.spring_layout(tmp_graph)
    plt.figure(figsize=(8, 8))
    plt.figure()
    plt.axis('off')

    color_list = []
    for i in range(0, len(node_list)):
        if node_list[i] == "R0":
            color_list.append('#0070C0')
        elif node_list[i] == "R1":
            color_list.append('#C00000')
        elif node_list[i] == "E1":
            color_list.append('#FFD966')
        elif node_list[i] == "E2":
            color_list.append('#A9D18E')
        elif node_list[i] == "R2":
            color_list.append('#00B0F0')
        elif node_list[i] == "R3":
            color_list.append('#D31DC2')

    nx.draw_networkx(g, pos, alpha = 1, node_size=300, node_color='white')
    nx.draw_networkx_nodes(g, pos, node_size=400, node_color=color_list, alpha = 1)
    nx.draw_networkx_edges(g, pos, alpha=1,width=4.0)

    plt.show()

def similarity_matrix(matrix):
    """Plots similarity matrix."""
    fig, ax = plt.subplots()

    plt.imshow(matrix,)
    plt.xlabel('Macromolecules', fontsize=18)
    plt.ylabel('Macromolecules', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.locator_params(axis='both', nbins=6)
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=16)
    cbar.set_label('Similarity', size=18)
    plt.show()

