from __future__ import annotations
from abc import ABC, abstractmethod
from part1 import DirectedWeightedGraph
import min_heap

# The following classes are for Strategy Design Pattern

class SPAlgorithm():

    @abstractmethod
    def calc_sp(self, G: DirectedWeightedGraph, source: int, k: int):
        pass

class Dijkstra(SPAlgorithm):

    def dijkstra_approx(G, source, k):
        pred = {} 
        dist = {} 
        Q = min_heap.MinHeap([])
        nodes = list(G.adj.keys())
        relaxCounter = {}
        for i in G.adj.keys():
            relaxCounter[i] = 0

        #Initialize priority queue/heap and distances
        for node in nodes:
            Q.insert(min_heap.Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(source, 0)

        #Meat of the algorithm
        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value
            dist[current_node] = current_element.key
            for neighbour in G.adj[current_node]:
                relaxCounter[neighbour] += 1
                if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour] and relaxCounter[neighbour] <= k:
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                    pred[neighbour] = current_node
        return dist

class Bellman_Ford(SPAlgorithm):

    def bellman_ford_approx(G, source, k):
        pred = {} 
        dist = {} 
        nodes = list(G.adj.keys())
        relaxCounter = {}
        for i in G.adj.keys():
            relaxCounter[i] = 0
        #Initialize distances
        for node in nodes:
            dist[node] = float("inf")
        dist[source] = 0

        #Meat of the algorithm
        for _ in range(G.number_of_nodes()):
            for node in nodes:
                for neighbour in G.adj[node]:
                    relaxCounter[neighbour] += 1
                    #Relaxtion is done at most k time for each node
                    if dist[neighbour] > dist[node] + G.w(node, neighbour) and relaxCounter[neighbour] <= k: 
                        dist[neighbour] = dist[node] + G.w(node, neighbour)
                        pred[neighbour] = node
        return dist
    
class A_star:

    def sortByHCost(nodesToExplore, h, dist, source):
        ls = {}
        re = []
        for i in dist.keys():
            if i in nodesToExplore:
            #print(source, " ", i, " must be a station")
                ls[i] = h[(source, i)] + dist[i]
        #print([(x, ls[x]) for x in ls.keys()])
        while bool(ls) != False:
            min = float("inf")

            for i in ls.keys():
                if ls[i] <= min:
                    min = ls[i]
                    minKey = i
                    
            #print(minKey, " ", min)      
            re += [minKey]
            ls.pop(minKey)
        return re

    def a_star(G, source, destination ,h):
        pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {} #Distance dictionary
        Q = min_heap.MinHeap([])
        nodes = list(G.adj.keys())

        #Initialize priority queue/heap and distances
        for node in nodes:
            Q.insert(min_heap.Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(source, 0)

        #Meat of the algorithm
        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value
            dist[current_node] = current_element.key
            if current_node == destination:
                break
            nodesToExplore = G.adj[current_node]
            #print(nodesToExplore)
            nodesToExplore = sortByHCost(nodesToExplore, h, dist, source)
            #print("Sorted: ", nodesToExplore)
            #Explore neighboors with the smallest edge cost + heuristic function value

            for neighbour in nodesToExplore:
                if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                    pred[neighbour] = current_node
        path = []
        node = destination
        while node in pred:
            path.append(node)
            node = pred[node]
        path.append(source)
        path.reverse()

        return (pred, path)
    
class Adapter(SPAlgorithm):

    def __init__(self):
        self.class_a_star = A_star()
    
    def a_star(self):
        self.class_a_star.a_star()
    
# The following classes are for Graphs

class Graph(ABC):

    def __init__(self):
        self.adj = {}
        self.weights = {}

    @abstractmethod
    def adjacent_nodes(self, node):
        pass

    @abstractmethod
    def add_node(self, node):
        pass

    @abstractmethod
    def add_edge(self, node1, node2, weight):
        pass

    @abstractmethod
    def number_of_nodes(self):
        pass
    
    @abstractmethod
    def w(self, node):
        pass

class WeightedGraph(Graph):

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]
    
class HeuristicGraph(WeightedGraph):

    def  __init__(self, __heuristic):
        self.__heuristic = __heuristic

    @property
    def get_heuristic(self):
        return self.__heuristic

# The following is the ShortPathFinder class, which "has" <Graph> and <SPAlgorithm>

class ShortPathFinder:

    def __init__(self):
        self.Graph = Graph()
        self.SPAlgorithm = SPAlgorithm()

    def calc_short_path(self, source, dest) -> float:
        dist = self.SPAlgorithm(self.Graph, source, dest)
        total = 0
        for key in dist.keys():
            total += dist[key]
        return total

    @property
    def set_graph(self):
        self._Graph

    @set_graph.setter
    def set_graph(self, graph):
        self._Graph = graph

    @property
    def set_algorithm(self,):
        self._SPAlgorithm
    
    @set_algorithm.setter
    def set_algorithm(self, algorithm):
        self._SPAlgorithm = algorithm