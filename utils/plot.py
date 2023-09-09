import matplotlib.pyplot as plt
import networkx as nx

def graph(tmp_graph):
    """Plots networkx graph."""

    node_list = [
        tmp_graph.nodes[idx]['label'] 
            for idx in range(len(tmp_graph.nodes))]

    node_dict = dict(zip(range(len(node_list)), node_list))

    node_set = sorted(list(set(node_list)))

    pos = nx.spring_layout(tmp_graph)  

    plt.figure(figsize=(8, 8))
    plt.axis('off')

    color_list = []
    color_dict = {
        "R0":'#0070C0',
        "R1":'#C00000',
        "E1":'#FFD966',
        "E2":'#A9D18E',
        "R2":'#00B0F0',
        "R3":'#D31DC2',
        "unknown":'#D9D9D9',  
    }


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
        else:
            color_list.append('#D9D9D9')
          
    nx.draw_networkx(tmp_graph, pos, alpha = 1, node_size=300, node_color='white')
    nx.draw_networkx_nodes(tmp_graph, pos, node_size=400, node_color=color_list, alpha = 1)
    nx.draw_networkx_edges(tmp_graph, pos, alpha=1,width=4.0)

    for i in range(0,len(node_set)):
        plt.gca().scatter([],[], color=color_dict[node_set[i]] , label=node_set[i])
    
    plt.legend(loc='lower right',fontsize = 10)
    plt.show()

    print(node_dict)


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

