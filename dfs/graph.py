import numpy as np
'''
2D dynamic array: [list() for i in range(length)]

class undirectGraph(Graph):
    def __init__(self, vertices):
        super(undirectGraph, self).__init__(vertices)

super() and all subclass stuff only works with new-style class
it is recommanded that always typing (object) on any class definition
class Graph(object)

func DFS-visit(u)
    time = time + 1
    u.discover = time
    u.color = gray
    for each v in _adjList[v]
        if v.color == white then
            v.parent = u
            DFS-visit(v)
    u.color = black
    time = time + 1
    u.finish = time

'''

WHITE = 0
GRAY = 1
BLACK = 2

class Node():
    def __init__(self, idx):
        self._discover = 0
        self._finish = 0
        self._color = WHITE
        self._idx = idx
        self._parent = -1

    def reset():
        self._discover = 0
        self._finish = 0
        self._color = WHITE
        self._parent = -1

    def __str__(self):
        print("node{}: parent is {}, discover at {}, finish at {}"
                .format(self._idx, self._parent, self._discover, self._finish))

class Graph():
    def __init__(self, vertices):
        self._v = vertices
        self._adjList = [list() for i in range(vertices)]
        self._adjMatrix = [[0]*vertices]*vertices
        self._time = 0

    def printEdge(self):
        for i in range(self._v):
            print(i, self._adjList[i])

    def DFStraversal(self, u):
        self._time = self._time + 1
        u._discover = self._time
        u._color = GRAY
        for v in self._adjList[u._idx]:
            if v._color == WHITE:
                v._parent = u._idx
                DFStraversal(self, v)
        u._color = BLACK
        self._time = self._time + 1
        u._finish = self._time

        
class undirectGraph(Graph):
    def __init__(self, vertices):
        Graph.__init__(self, vertices)
    
    def addEdge(self, m, n, weight = 1):
        self._adjList[m].append(Node(n))
        self._adjMatrix[m][n] = weight
        self._adjMatrix[n][m] = weight

class directGraph(Graph):
    def __init__(self, vertices):
        Graph.__init__(self, vertices)

    def addEdge(self, m, n, weight = 1):
        self._adjList[m].append(n)
        self._adjMatrix[m][n] = weight
    

