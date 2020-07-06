#Morgen Nicodemus
#CS5001 Homework 1
import wikipedia
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter
from numpy import array
import math
from itertools import product

#Do Aqualung
def Aqualung():
    # Specify name of the starting page
    SEED = "Aqualung".title()

    # Keep track of pages to process; we'll only do 2 layers,
    # process links as a BFS
    toDo_lst = [(0, SEED)]
    toDo_set = set(SEED)
    done_set = set()

    # Create a directed graph
    F = nx.DiGraph()

    layer, page = toDo_lst[0]
    count = 0
    while layer < 2:
        del toDo_lst[0]
        done_set.add(page)
        #print(layer, page)
        try:
            # Download the selected page
            wiki = wikipedia.page(page)
        except:
            layer, page = toDo_lst[0]
            print("Could not load", page)
            continue

        for link in wiki.links:
            link = link.title()
            if not link.startswith("List Of"):
                if link not in toDo_set and link not in done_set:
                    toDo_lst.append((layer + 1, link))
                    toDo_set.add(link)
                F.add_edge(page, link)

        layer, page = toDo_lst[0]
        count += 1
        if count == 50:
            break

    F.remove_edges_from(nx.selfloop_edges(F))

    core = [node for node, deg in dict(F.degree()).items() if deg >= 2]
    G = nx.subgraph(F, core)
    # G is a lot smaller (3426 nodes, 15634 edges)
    #print("{} nodes, {} edges".format(len(G), nx.number_of_edges(G)))

    # Display the smaller graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(100, 100))
    nx.draw_networkx(G, pos=pos, with_labels=True)
    # plt.axis('off')
    # plt.show()

    # Display a list of subjects sorted by in-degree
    #top_indegree = sorted(dict(G.in_degree()).items(),
    #                      reverse=True, key=itemgetter(1))[:100]
    #print("\n".join(map(lambda t: "{} {}".format(*reversed(t)), top_indegree)))
    return nx.DiGraph(G)

#Do Ian Anderson
def Ian():
    # Specify name of the starting page
    SEED = "Ian Anderson".title()

    # Keep track of pages to process; we'll only do 2 layers,
    # process links as a BFS
    toDo_lst = [(0, SEED)]
    toDo_set = set(SEED)
    done_set = set()

    # Create a directed graph
    F = nx.DiGraph()

    layer, page = toDo_lst[0]
    count = 0
    while layer < 2:
        del toDo_lst[0]
        done_set.add(page)
        #print(layer, page)
        try:
            # Download the selected page
            wiki = wikipedia.page(page)
        except:
            layer, page = toDo_lst[0]
            print("Could not load", page)
            continue

        for link in wiki.links:
            link = link.title()
            if not link.startswith("List Of"):
                if link not in toDo_set and link not in done_set:
                    toDo_lst.append((layer + 1, link))
                    toDo_set.add(link)
                F.add_edge(page, link)

        layer, page = toDo_lst[0]
        count += 1
        if count == 50:
            break

    F.remove_edges_from(nx.selfloop_edges(F))

    core = [node for node, deg in dict(F.degree()).items() if deg >= 2]
    G = nx.subgraph(F, core)

    # Display the smaller graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(100, 100))
    nx.draw_networkx(G, pos=pos, with_labels=True)
    # plt.axis('off')
    # plt.show()

    # Display a list of subjects sorted by in-degree
    #top_indegree = sorted(dict(G.in_degree()).items(),
    #                      reverse=True, key=itemgetter(1))[:100]
    #print("\n".join(map(lambda t: "{} {}".format(*reversed(t)), top_indegree)))
    return nx.DiGraph(G)


def main():
    print("Generating Aq")
    Aq = Aqualung()
    print("Generating IanA")
    IanA = Ian()
    print("Computing similarity")
    nx.write_edgelist(Aq, "aq.edgelist")
    #As = nx.simrank_similarity(Aq,max_iterations=5)
    #print("Done with simrank")

    G1 = nx.DiGraph()
    G1.add_nodes_from([1,2,3,4,5])
    G1.add_edges_from([(1,2),(1,3),(1,4),(4,5)])

    #s = nx.simrank_similarity(G1)
    #A = [[s[u][v] for v in sorted(s[u])] for u in sorted(s)]
    #sim_array = array(A)
    #print(sim_array)
    #AqL = list(Aq.nodes)
    #IanAL = list(IanA.nodes)

    #for node in AqL:
     #   for node2 in AqL:
     #       print("Checking",node," ",node2)
     #       sim_val = nx.simrank_similarity(Aq,source=node,target=node2)
     #       if sim_val >= 0.01:
     #           print(node, node2, sim_val)

    #removing nodes for networkx.difference
    AqL = list(Aq.nodes)
    IanAL = list(IanA.nodes)

    for node in AqL:
        if (node in IanAL):
            continue
        else:
            Aq.remove_node(node)

    for node in IanAL:
        if (node in AqL):
            continue
        else:
            IanA.remove_node(node)
    print("Computing Difference")

    D = nx.difference(Aq, IanA)
    D.remove_nodes_from(list(nx.isolates(D)))
    print(nx.info(D))

if __name__ == '__main__':
    main()
