#Morgen Nicodemus
#CS5001

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import community
from networkx.algorithms.community import centrality as c

#For sorting the degree
def sec_elem(el):
    return el[1]


def main():
    #Reading in the graph
    G=nx.read_edgelist("GameOfThrones.txt",delimiter=",",data=(('strength',int),('season',int)))

    #Displaying the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10,10))
    nx.draw_networkx(G, pos=pos, with_labels=True)
    plt.axis('off')
    plt.show()

    #Outputting info
    print(nx.info(G))

    #Outputting highest degree node name & degree
    nodes=list(G.degree())
    print("\nHighest degree node is:",nodes[0][0],"with degree",nodes[0][1])

    #Outputting num of connected components
    print("\nNumber of connected components:",len(list(nx.connected_components(G))))

    #Outputting the num of maximal cliques
    print("\nNumber of maximal cliques:",len(list(nx.find_cliques(G))))

    #Outputting num of nodes in main core and k val
    core_num = list(nx.k_core(G).nodes())
    for x in range(len(core_num)):
        if core_num == list(nx.k_core(G, k=x)):
            k_val=x
    print("\nNumber of nodes in main core:",len(core_num),"with k val:",k_val)

    #Outputting num of nodes in main crust
    print("\nNumber of nodes in main crust:",len(list(nx.k_crust(G).nodes())))

    #Output num of nodes in the k corona
    print("\nNumber of nodes in k corona:",len(list(nx.k_corona(G, k=k_val).nodes())))

    #Output num of nodes in main shell
    print("\nNumber of nodes in main shell:",len(list(nx.k_shell(G).nodes())))

    #Display graph, main core - red, main crust - blue
    color_map = []
    for node in G:
        if node in list(nx.k_core(G).nodes()):
            color_map.append('red')
        elif node in list(nx.k_crust(G).nodes()):
            color_map.append('blue')
    nx.draw_networkx(G, pos=pos,node_color=color_map, with_labels=False)
    plt.axis('off')
    plt.show()

    #Louvain Method, output num of communities, size or largest commnunity, size of smallest community, modularity of partition
    partition = community.best_partition(G)
    com_num = partition[max(partition, key=partition.get)]
    print("\nLouvain Method:")
    print("Number of communities:",com_num+1)
    count = []
    comm_list = list(partition.values())
    for x in range(com_num):
        count.append(comm_list.count(x))
    print("The largest community has count:",max(count))
    print("The smallest community has count:",min(count))
    print("The modularity of this partitioning:",community.modularity(partition,G))
        
    #Display graph using Louvain, with nodes in diff colors per partition
    cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
    nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,cmap=cmap, node_color=list(partition.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.axis('off')
    plt.show()

    #Girvan-Newman Method, output num of communities, size or largest commnunity, size of smallest community, modularity of partition
    print("\nGirvan-Newman Method:")
    components = c.girvan_newman(G)
    i = 0
    for row in components:
        if (i == 0):
            finalResult = row
        i = i + 1
    partitions = dict()
    L = list(finalResult)
    p = 0
    for comp in L:
        for entry in comp:
            partitions[entry] = p
        p = p + 1
    com_num = partitions[max(partitions, key=partitions.get)]
    print("Number of communities:",com_num+1)
    count = []
    comm_list = list(partition.values())
    for x in range(com_num):
        count.append(comm_list.count(x))
    print("The largest community has count:",max(count))
    print("The smallest community has count:",min(count))
    print("The modularity of this partitioning:",community.modularity(partitions, G))
    
    #Display graph using Girvan-Newman, with nodes in diff colors per partition
    cmap = cm.get_cmap('viridis', max(partitions.values()) + 1)
    nx.draw_networkx_nodes(G, pos, partitions.keys(), node_size=60,cmap=cmap, node_color=list(partitions.values()))
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
