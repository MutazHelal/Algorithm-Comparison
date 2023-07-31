## Algorithm-Comparison

- 1 Shortest Paths Algorithms
   - 1.1 Approximation of Dijkstra and Bellman-Ford Experiments
      - 1.1.1 Dijkstra and Bellman Approximation
      - 1.1.2 Number of Relaxation
      - 1.1.3 Edge Weight Range Value
      - 1.1.4 Relaxation Limit
      - 1.1.5 Graph edge density
   - 1.2 All Source Dijkstra and Bellman-Ford
   - 1.3 Mystery function
- 2 Dijkstra and A∗
   - 2.1 How does A* it work?
   - 2.2 What issues with Dijkstra’s algorithm is A* trying to address?
   - 2.3 How would you empirically test Dijkstra’s vs A*?
      - Dijkstra’s algorithm compare to A*? 2.4 If you generated an arbitrary heuristic function (similar to randomly generating weights), how would
   - 2.5 What applications would you use A* instead of Dijkstra’s?
   - 2.6 A* Implementation
- 3 A* vs Dijkstra Performance on Networks
   - 3.1 Experiment Outline
   - 3.2 Stations on the Same line
   - 3.3 Stations on the Adjacent lines
   - 3.4 Stations with Several Transfers
- 4 Code Refactor
   - 4.1 Design Principles
   - 4.2 Design Patterns
   - 4.3 Modifying the design in Figure 2 to be robust to these potential changes.
   - 4.4 Other types of Graphs and different implementations
   - 1 Dijkstra Approximation vs BellmanFord Approximation List of Figures
   - 2 Dijkstra Approximation vs BellmanFord Required number of Relaxation
   - 3 Dijkstra Approximation vs BellmanFord edge weight limit
   - 4 Dijkstra Approximation vs BellmanFord number of relaxation limit
   - 5 Dijkstra Approximation vs BellmanFord edge density limit
   - 6 Dijkstra Approximation vs BellmanFord edge density and relaxation limit
   - 7 Mystery function log-log scaled graph
   - 8 A* vs Dijkstra 1000 combinations with distance edge-weight
   - 9 A* vs Dijkstra all combinations with distance edge-weight
   - 10 A* vs Dijkstra 1000 combinations with distance + time edge-weight
   - 11 A* vs Dijkstra 1000 combinations with line edge-weight
   - 12 A* vs Dijkstra 1000 combinations with time edge-weight
   - 13 A* vs Dijkstra Stations on the same line
   - 14 A* vs Dijkstra Stations on adjacentLines
   - 15 A* vs Dijkstra Stations with multiple transfers


## 1: Shortest Paths Algorithms

### 1.1 Approximation of Dijkstra and Bellman-Ford Experiments

Both ”dijkstraapprox” and ”bellmanfordapprox” are implemented by taking the original algorithms, modifying
them such that this the following code, which relaxes the nodes, is run at most k times per node.

```
if d[u]+w(u,v)¡d[v]
d[v] = d[u]+w(u,v)
```
The following are experiments run, each testing a different aspect of the performance of these two algorithms.

#### 1.1.1 Dijkstra and Bellman Approximation

Outline

- Graph size: 30 nodes and maximum edge weight is 50
- Number of Edges: 870
- Both algorithms’ approximations are run till achieving the actual shortest path
  
![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/883165ab-4713-4f2f-9542-5cd471da01af)
```
Figure 1: Dijkstra Approximation vs BellmanFord Approximation
```

Outline Explanation
This is a very simple experiment which should showcase how close each of both approximations are to the the actual
shortest path and how many relaxations per node are needed to get the shortest path. It is a general performance
gauge.

Observation
Dijkstra is a lot closer to the total distance of the actual shortest path and for this specific experiment reaches the
actual shortest path with only around 20 relaxations per node while Bellman needed a bit over 50. Therefore, we
conclude that Dijkstra’s approximation is a lot more accurate.


#### 1.1.2 Number of Relaxation

Outline

- Number of Graphs: 50 graphs, from 1 node to 50 node graph
- Number of Edges: (number of nodes) times (number of nodes - 1)
- Edge Weight: from 1 to 50
- Both algorithms’ approximations are run till achieving the actual shortest path

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/4ec1de8c-5e66-4ead-8b16-4de3846b8c73)
```
Figure 2: Dijkstra Approximation vs BellmanFord Required number of Relaxation
```
Outline Explanation
This experiment while not much different from the first experiment, focuses on the number of relaxations needed to
get from the approximation to the actual shortest path. The two variables on the graph are the number of nodes
and the number of relaxations to get the actual shortest path.

Observation
Similar to experiment 1, Bellman almost always requires a higher number of relaxation per node to get the shortest
path. These two experiments suggest that Dijkstra is a more efficient algorithm and Bellman should be used only
when having negative edge-weight values.

#### 1.1.3 Edge Weight Range Value

Outline

- Graph Size: 20 nodes
- Number of Edges: (number of nodes) times (number of nodes - 1)
- Edge Weight: from 1 to 100


- Both algorithms’ approximations are run till achieving the actual shortest path

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/a7fa5ed8-3d8f-4398-8326-40013101f1ed)
```
Figure 3: Dijkstra Approximation vs BellmanFord edge weight limit
```

Outline Explanation
This experiment focuses on the variation in the range of values a weight of an edge can take. A lower range means an
increase in the number of shortest paths. The parameter should not have a huge impact on the number of relaxations
needed for each algorithm. However, it could highlight how the scenario is dealt with by both procedures.

Observation
While still confirming what was previously established by experiments 1 and 2 when it comes to efficiency. These
experiments show how less stable Bellman is compared to Dijkstra which is somewhat evident in experiment 2 (see
Figure 2). This might be due to Bellman having to recheck nodes that are already visited. For Dijkstra, once a node
is marked it is never visited again.

#### 1.1.4 Relaxation Limit

Outline

- Graph Size: 100 graphs from 1 node graph to 100 nodes graph
- Number of Edges: (number of nodes) times (number of nodes - 1)
- Edge Weight:1 to 50
- Number of relaxations: at most 20

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/cef7f592-2ebc-44fe-a9b6-c4f022874aa1)
```
Figure 4: Dijkstra Approximation vs BellmanFord number of relaxation limit
```

Outline Explanation
This experiment is a different take on the approximation of both algorithms. Limiting node relaxations to 20 per
node while increasing the graph size and comparing how close each algorithm is to the actual shortest path.

Observation
Dijkstra clearly outperforms Bellman. Bellman approximations start getting very inaccurate at graphs with around
20 nodes. On the other hand, Dijkstra, even though results are not exact, paths are really close to the actual shortest
path all the way to graphs with 100 nodes. This suggests that for very large graphs and when results don’t have to
be exact, Dijkstra’s approximation might prove very useful.

#### 1.1.5 Graph edge density

Outline

- Graph Size: fixed to 50 nodes for all graphs
- Number of Edges: (number of nodes) times (number of nodes - 1) for the first graph and less (limited) for the
    second graph
- Edge Weight:1 to 50
- Number of relaxations: As many as needed for the first graph and limited for the second graph from 1 to 50

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/7b4d0d87-c31a-4590-a051-3c533964f5d8)
```
Figure 5: Dijkstra Approximation vs BellmanFord edge density limit
```

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/8c114535-32b5-4692-802b-3ff1da3e85f7)
```
Figure 6: Dijkstra Approximation vs BellmanFord edge density and relaxation limit
```
Outline Explanation
This experiment consists of limiting the number of edges. This is done by limiting the number of nodes connected to
all nodes. For instance, in a 10-node graph, if the limit is 2, it means only the first and second nodes are connected


to all other nodes. A prediction of the results of this experiment was an increasing number of relaxations required
to find the shortest path compared to experiment 2.

As for graph 2, the number of edges is limited in the same way with the addition of limiting the number of relax-
ations along with the edge limit. The number on the x-axis represents both the edge limit and relaxation limit. This
is done in order to gauge the degree of accuracy both algorithms perform when dealing with graphs that are less dense.

Observation
For graph 1, as expected, the number of relaxation is higher for Bellman-Ford but surprisingly it is around the same
(if not less) for Dijkstra (see Figure 2). This suggests that graph Dijkstra has equal efficiency with graphs of different
edge density.

For graph 2, Dijkstra always resulted in the actual shortest path, which makes sense given how this experiment was
done (n nodes connected to all = n relaxations per node). Bellman-Ford was slightly inaccurate but not too far off.

### 1.2 All Source Dijkstra and Bellman-Ford

Running an all-source Dijkstra and Bellman-Ford algorithms using algorithms by running them once for each node
and saving each predecessor dictionary in a single list yields a mapping of the shortest map from any node to all nodes.

The complexities of all source algorithms would be O (V^3 ) for Dijkstra and O (V^4 ) for Bellman-Ford. This is self-
evident by the fact that we run each algorithm V times which represents the number of nodes in the graph.

### 1.3 Mystery function

The function seems to be a matrix of an all-source shortest-path algorithm. Whoever through testing, the function is
found not to be able to handle negative weight edges which might suggest it is a generalization from Dijkstra rather
than Bellman-Ford.
By code inspection, it seems that the function is O(V^3 ) for a dense graph. However, we run further experiments to
confirm or deny this time complexity.

Mystery function empirical testing

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/b529d192-ee65-47fb-8bd3-97b8ed1c98ac)
```
Figure 7: Mystery function log-log scaled graph
```
Observation
Using a log-log graph to plot the performance of the function we can determine the degree of the polynomial time
to be around 2.7 (the slope of the line log(y) = n*log(x)+log(c)), which we could round to 3. This number,O(V^3 )
agrees with the time complexity prediction based on the code inspection. This also makes sense, given that the
algorithm has 2 nested loops. These results reaffirm two initial claims stated above, which state that the Mystery
function is a variation of Dijkstra for all source paths and that the time complexity is O(V^3 ) for dense graphs.

## 2: Dijkstra and A∗

### 2.1 How does A* it work?

This algorithm is very similar to Dijkstra’s pathfinding algorithm but it follows a heuristic. In the regular Dijkstra’s
algorithm, we take as inputs the weighted edge graph, the start node, and our destination node; in the A* algorithm
we take in an extra parameter which is a heuristic function. The function takes in a node and estimates the minimum
cost from that node to the destination node. The estimate might be based on the Euclidean distance between the
two nodes. This way we keep track of the total cost so far to reach a node ’n’ from the start node + the estimated
cost from n to our destination node. The sum gives us the total estimated path to our destination node, through
node ’n’.


### 2.2 What issues with Dijkstra’s algorithm is A* trying to address?

The problem with Dijkstra’s algorithm is that it tries to explore every node in the graph before it can come up with
the shortest path between two nodes. Although, this might not seem like a massive issue with smaller graphs, 
in graphs with more nodes and edges, running Dijkstra’s algorithm is very slow. This is where the A* algorithm
steps in and makes Dijkstra’s algorithm more efficient by using the heuristic function described earlier. The heuristic
essentially guides the algorithm towards the destination node by making it explore the most promising paths first
which in turn leads to a faster search for the shortest path.

Also, Dijkstra’s algorithm cannot handle negative edge weights as it would lead to sub-optimal solutions or might
as well lead to a non-termination of the algorithm. Meanwhile, the A* algorithm can handle negative edge weights
because it never expands a node such that the sum of the heuristic and the path has taken so far is greater than the
optimal path length.

### 2.3 How would you empirically test Dijkstra’s vs A*?

We can empirically test the difference in performance between these two algorithms by comparing their run times
along with the number of nodes expanded for the same graph. So we randomly generate edge-weighted graphs of
different sizes and edge numbers. For each of those graphs we randomly choose the start and the end node and then
run Dijkstra’s and A* algorithms. We then record their run time and the number of nodes expanded during the
search and then repeat the same steps for a different graph. Finally, we use those two metrics to produce a graph
and find some correlation.

We can also repeat the same experiment for different heuristic functions to figure out which performs the best.

### 2.4 If you generated an arbitrary heuristic function (similar to randomly generating

### weights), how would Dijkstra’s algorithm compare to A*?

Since the efficiency of the A* algorithm depends heavily on the type and quality of the heuristic we follow, it may
very likely degrade if we just use any heuristic function. If the heuristic function is arbitrary and does not reflect the
underlying graph structure, A* may not be able to exploit the heuristic information effectively. Also, it might not
necessarily prevent the algorithm itself from exploring unnecessary nodes. This makes the algorithm at best similar
to Dijkstra’s or probably even worse.

In such cases where we use an arbitrary heuristic, Dijkstra’s algorithm can guarantee consistence performance than
A* as it does not depend on any heuristic.

### 2.5 What applications would you use A* instead of Dijkstra’s?

The A* algorithms can be used in almost any place where it requires finding the shortest path between two points
among many other channels efficiently.

The most common application is in satellite navigation where the algorithm needs to find the shortest path between
two places in a geographic location. The heuristic function can be designed to consider the distance and the traffic
conditions of the roads that vary over time.

A* algorithm may be used in robotics where a robot needs to go from point A to B using the shortest path available.
The heuristic function can be designed to consider the robot’s ultrasound sensor readings from the obstacles in its
environment


Network routers commonly used the A* algorithm to find the quickest path to send a packet of data from the sender
to the receiver. The heuristic function can be designed to consider the distance and the traffic in the network channel.

### 2.6 A* Implementation

Along with this file, the astar.py file contains a simple implementation of A∗which works like Dijkstra with key
differences being the order in which neighbours are explored, which is reordered on the basis of the value of f(x) =
g(x) + h(x). g(x) is the edge cost and h(x) is the heuristic function cost. This allows a good path to be explored
first. Thus, potentially resulting in better performance, giving a good choice for the heuristic function.

## 3: A* vs Dijkstra Performance on Networks

### 3.1 Experiment Outline

This experiment was run by constructing the graph from the London map(tube) database.
Different parameters were taken as edge weights, these parameters are distance (x + y value), time, distance + time,
and distance + line.
As for the heuristic function, it generates a dictionary that contains the distance from any station to all stations if
they were connected by a straight line.
It is important to note that both algorithms result in a shortest path. The difference lies in the order that explores
nodes which also results in different paths that are equally short (follows from the definition of both algorithms).

All the following graphs run through a lot of different combinations of source destination nodes and plot a time
performance graph.

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/e88e7529-9158-47c3-ae0f-47e6f80883cb)
```
Figure 8: A* vs Dijkstra 1000 combinations with distance edge-weight
```

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/8edb40e6-1618-4dfb-abbd-3ae746c7d936)
```
Figure 9: A* vs Dijkstra all combinations with distance edge-weight
```

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/0fed70da-b354-45c8-ab73-57660b6a86e6)
```
Figure 10: A* vs Dijkstra 1000 combinations with distance + time edge-weight
```

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/2f0755a7-8c7a-4de4-b401-61ab24625930)
```
Figure 11: A* vs Dijkstra 1000 combinations with line edge-weight
```

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/6e2977b6-6187-4643-8eb2-2074bc77202d)
```
Figure 12: A* vs Dijkstra 1000 combinations with time edge-weight
```

Observation
No matter what parameter is taken for edge-weight, A* proves to be a hindrance rather than an improvement over
Dijkstra. The difference is constant which suggests that while A* is not inherently worse, it adds an unnecessary
overhead cost. It is also important to note that A* is highly dependent on the heuristic function. We conclude from
these experiments that for this network, carefully chosen paths aren’t any better than random ones. However, a differ-
ent choice for the heuristic function might prove this wrong since it could be any function that prioritizes certain paths.

### 3.2 Stations on the Same line


![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/02646572-3d7d-49b3-8109-4132ea3ec6f7)
```
Figure 13: A* vs Dijkstra Stations on the same line
```
Observation
When only considering stations on the same line, the performance difference between both algorithms is very
minuscule, this makes sense since the path is very short, to begin with and does not require many iterations to reach the
destination.


### 3.3 Stations on the Adjacent lines

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/cb828433-8e8b-4d05-b7b0-586b16a5a9fa)
```
Figure 14: A* vs Dijkstra Stations on adjacentLines
```
Observation
Much like the other experiments above. Dijkstra still outperforms A*. This graph reveals more about the relation
between finding a shortest path for different parts of the network than about how A* and Dijkstra perform relative
to each other. The periodic shape in the graph can easily be explained by how far two adjacent line stations are from
the connecting intersection. Stations start getting far apart until there is a new intersection that connects them.


### 3.4 Stations with Several Transfers

![image](https://github.com/MutazHelal/Algorithm-Comparison/assets/42630919/20bce925-3aee-48e2-a9a6-dca7471b2f31)
```
Figure 15: A* vs Dijkstra Stations with multiple transfers
```
Observation
Results are very similar to adjacent stations which could be explained with the same reasoning as well. However, the
only difference is that this graph has a bump for later combinations which might suggest that some in-adjacent
lines are further apart than others.

## 4: Code Refactor

### 4.1 Design Principles

Single Responsibility Principle:

Figure 2 shows that every single module is responsible for a singular task. E.g The AStar module only does the
A* pathfinding, similarly BellmanFord only does that unique path finding only. No module does more than one task.

Open-Closed Principle:

In Figure 2 we are using the two interfaces ”Graph” and ”SPAlgorithm” which we extend to make new classes. These
new classes can be given additional functionality, which means the original interface is open for extension but is also
closed for any modification.

Interface Segregation Principle:

In Figure 2 it can be seen that the modules only depend on/use the interfaces they are supposed to use. E.g. Heuristic-
Graph depends on WeightedGraph and in turn that depends on ”Graph” only, similarly Dijkstra, BellmanFord and
AStar only depends on ”SPAlogrithm” because they don’t need any other interfaces to function correctly.


Dependency Inversion Principle:

Figure 2 shows that the lower-level module HeuristicGraph depends on the higher-level module WeightedGraph and both
in turn depend upon abstraction for their details. Similarly, Dijkstra, BellmanFord, and AStar also depend upon
abstraction for details, and not the other way round.

### 4.2 Design Patterns

Strategy:

As seen in figure 2 the set algorithm function in ShortPathFinder is responsible for choosing which path-finding
algorithm is going to be used. The interface ”SPAlgorithm” contains the method for the algorithms Dijkstra, Bell-
Manford and AStar. During the execution of the program, the client code will set the strategy object for the context
class ”ShortPathFinder” to determine which algorithm to use.

### 4.3 Modifying the design in Figure 2 to be robust to these potential changes.

The simple fix to this problem is to make the classes Generic. This means that every method within our generic
classes will also be generic. The data type will not be any primitive type, instead, we can specify the parameter
during object creation which can be integer, string, list, float, etc. This will allow us to use any kind of data type
and also have multiple data types passed into a single method.

### 4.4 Other types of Graphs and different implementations

Apart from the obvious way of implementing a graph using an adjacency set like the graph in Figure 2, we can also
implement the graph structure using an adjacency list and adjacency matrix.

In adjacency list, we use a linked list to keep track of which nodes are reachable from a particular node. In the adjacency
matrix, we use a 2D matrix where each cell represents an edge between two vertices. The value of the cell represents
the edge weight (Or it could be a negative value to indicate an edge does not exist).

