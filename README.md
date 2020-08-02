# CS5001 - Applied Social Network Analysis

## Homework 1
Starts on the wikipedia pages for "Aqualung" and "Ian Anderson", collects the links from each page and those page's links, and builds two graphs for each. Compares the graphs looking for nodes that have a similarity rank >= 0.01 and outputs those node pairs. Then, removes nodes not in both graphs in order to compute the difference and the intersection of the two graphs.

## Homework 3
Creates a networkx graph from the GameOfThrones.txt. Process and displays graph statistics, highest degree node, number of maximal cliques, k-core, k-crust, k-corona, number of main shell nodes. Displays the graph with main core nodes in red and main crust in blue. Uses Louvain method to output number of communities, size of largest community, and modularity of the partitioning. Displays graph with Louvain partitioning. Uses Girvan-Newman method to output number of communities, size of largest community, and modularity of the partitioning. Displays graph with Girvan-Newman partitioning.

## Homework 5
Reads in given files to create a graph of users and movies with edges of user ratings of certain movies. Displays the graph. Creates edges between uses based on their ratings of movies they've both watch, and displays the graph with the new edges. Creates a social network by creating edges between users based on movies they've both seen, and displays the social network graph.

## Homework 6
Parses the XML of the given Flickr to find the photo link and the description of each post. Uses VADER Sentiment Intensity Analyzer to determine the compound value of the description, and if it is not zero, retireves the html of the found url. Parses the html to find the static url of the image, which is then passed to Google Vision AI. Determines a compound score for the picture by averaging of compound VADER score of each descriptive term Google Vision returns. If both the description compound score and the image compund score are not zero, outputs the description, Google Vision's descriptive labels, the description compound score, and the image compound score for the first 12 images that match.
