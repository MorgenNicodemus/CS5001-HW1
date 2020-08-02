#HW5
#Morgen Nicodemus
import networkx as nx
import csv
import matplotlib.pyplot as plt

def displayGraphWithEdgeLabels(G, edgeAttribute):
  pos = nx.spring_layout(G, k=1000, scale=1000)
  plt.figure(figsize=(10,10))
  nx.draw_networkx(G,pos)
  labels = nx.get_edge_attributes(G, edgeAttribute)
  nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
  plt.axis('off')
  plt.show()

def main():
    #Start graph
    G = nx.DiGraph()
    usrlist = []
    users = open("users_noColHdrs.csv")
    for x in users:
        G.add_node(x[0:-1],user='1')
        usrlist.append(x[0:-1])

    with open("movies_noColHdrs.csv", mode ='r') as file:
        Users = csv.reader(file)
        for line in Users:
            G.add_node(line[0],title=line[0], year=line[1], netflixRating=line[2])

    with open("userRatedMovie_noColHdrs.csv", mode ='r') as file:
        Edges = csv.reader(file)
        for line in Edges:
            G.add_edge(line[0],line[1],rating=line[2])

    print("Node info: ",G.nodes.data())
    print("\nEdge info: ",G.edges.data())

    displayGraphWithEdgeLabels(G, 'rating')

    for n in usrlist:
        for y in usrlist:
            if n == y:
                continue
            else:
                G.add_edge(n,y,similarity=nx.simrank_similarity(G,n,y))
    displayGraphWithEdgeLabels(G, 'similarity')

    
    for n in usrlist:
        for x in list(G.out_edges(n)):
            if x[1] in usrlist:
                continue
            for y in usrlist:
                if n == y:
                    continue
                for z in list(G.out_edges(y)):
                    if z[1] in usrlist:
                        continue
                    if x[1] == z[1]:
                        G.add_edge(n,y,is_like="is_like")
    displayGraphWithEdgeLabels(G,'is_like')

if __name__ == "__main__":
    main()
    
