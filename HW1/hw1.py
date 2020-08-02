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
    print("Processing Aqualung Wiki")
    Aq = Aqualung()
    print("Processing Ian Anderson Wiki")
    IanA = Ian()

    
    print("Generating Similarity rankings for Aqualung")
    As = nx.simrank_similarity(Aq)
    A = [[As[u][v] for v in sorted(As[u])] for u in sorted(As)]
    sim_array = array(A)

    print("Generating Similarity rankings for Ian Anderson")
    Ia = nx.simrank_similarity(Aq)
    IanAr = [[Ia[u][v] for v in sorted(Ia[u])] for u in sorted(Ia)]
    Ian_array = array(IanAr)
    
    AqL = list(Aq.nodes)
    IanAL = list(IanA.nodes)

    print("\nSimilarities for Aqualung")
    for x in range(len(sim_array)):
        for y in range(len(sim_array[x])):
            if x == y:
                break
            elif sim_array[x][y] >= 0.01:
                print(AqL[x]," | ",AqL[y]," | ",sim_array[x][y])

    print("\nSimilarities for Ian Anderson")
    for x in range(len(Ian_array)):
        for y in range(len(Ian_array[x])):
            if x == y:
                break
            elif Ian_array[x][y] >= 0.01:
                print(IanAL[x]," | ",IanAL[y]," | ",Ian_array[x][y])
            

    #removing nodes for networkx.difference
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
    print("\nComputing Difference")

    D = nx.difference(Aq, IanA)
    D.remove_nodes_from(list(nx.isolates(D)))
    print(nx.info(D))

    #Computing Intersection
    print("\nIntersection")
    I = nx.intersection(Aq,IanA)
    I.remove_nodes_from(list(nx.isolates(I)))
    print(nx.info(I))

if __name__ == '__main__':
    main()
