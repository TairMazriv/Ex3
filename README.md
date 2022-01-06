# Ex3
In this assignment, we implemented a data structure of a weighted and directed graph.
We were given two interfaces that we needed to implement, DiGraph and AlgoGraph, and in addition we needed to find a data structure that would suit our needs.

**DiGraph:**

In this Interface we constructed a graph consisting of nodes and edges with weight. also, It include functions to change the graph,
like add node or edge or remove node or edge, and functions that return data about the graph.

**GraphAlgo:**

In this interface, we made some functions that run on the graph. Like shortest-path between tow nodes, that return list of 
the nodes in the path, and the center point of the graph, or TSP function that solve the travelling salesman problem.
also in this class we wrote function that load data of graph from json file, and a function that save the data to new file.

------------------------------------------------------------------------------------------------------------------------------


**Comprasion:**
We compare the running time of the functions between Java and Python: 

| Function | Python | java |
| --- | --- | --- |
| Load | 6671.79 ms | 9157.8 ms |
| Save | 27339.5 ms | 74385.6ms |
| Shorted-path | 25158.9 ms  | 43658.3 ms  |
| Center-point | 76249.5 ms | 61193.0 ms |
| TSP |  606591.9 ms | 1056397.8 ms |

The compration was run on this computer:

* Intel(R) Core(TM) i5-5300U CPU @ 2.30GHz   2.29 GHz
* RAM installed 8.00 GB (7.70 GB usable)
* System type 64-bit operating system, x64-based processor



-----------------------------------------------------------------------------------------------


**Plotting graphs:**
        
				
Graph A1:

![](https://github.com/TairManzaly/pic/blob/main/Graphs/A1.png)

Graph A4:

![](https://github.com/TairManzaly/pic/blob/main/Graphs/A4.png)

Graph A5:

![](https://github.com/TairManzaly/pic/blob/main/Graphs/A5.png)

Graph T0:

![](https://github.com/TairManzaly/pic/blob/main/Graphs/T0.png)

-------------------------------------------------------------------------------------------------------------------------------------------------





