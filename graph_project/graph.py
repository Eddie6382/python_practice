import numpy as np
from collections import deque
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
        self._parents = []

    def reset():
        self._discover = 0
        self._finish = 0
        self._color = WHITE
        self._parents = []

    def __str__(self):
        return ("node{}: parent is node{}, discover at {}, finish at {}"
                .format(self._idx, self._parents, self._discover, self._finish))

class Graph():
    def __init__(self, vertices):
        self._v = vertices
        self._adjList = [list() for i in range(vertices)]
        self._adjMatrix = [[0]*vertices]*vertices
        self._time = 0
        self._nodeList = dict()
        self._cycles = []

    def printEdge(self):
        print("Adjacent List")
        for i in range(self._v):
            print(i, self._adjList[i])
        print("")

    def printNode(self, idx):
        print(self._nodeList[idx])

    def DFStraversal(self, u_idx):
        u = self._nodeList[u_idx]
        self._time = self._time + 1
        u._discover = self._time
        u._color = GRAY
        for v_idx in self._adjList[u._idx]:
            v = self._nodeList[v_idx]
            if v._color == WHITE:
                v._parents.append(u._idx)
                self.DFStraversal(v_idx)
            if v._color == GRAY:
                v._parents.append(u._idx)
                self.findCycle(v)

        u._color = BLACK
        self._time = self._time + 1
        u._finish = self._time

    def findCycle(self, u):
        cycle = [u._idx]
        i = u._parents[-1]
        while i != u._idx:
            cycle.append(i)
            i = self._nodeList[i]._parents[-1]
        self._cycles.append(cycle)

    def printCyclic(self):
        for cycle in self._cycles:
            print("cycle:",cycle)

        
class undirectGraph(Graph):
    def __init__(self, vertices):
        Graph.__init__(self, vertices)
    
    def addEdge(self, m, n, weight = 1):
        self._nodeList[m] = Node(m)
        self._nodeList[n] = Node(n)
        self._adjList[m].append(n)
        self._adjMatrix[m][n] = weight
        self._adjMatrix[n][m] = weight

class directGraph(Graph):
    def __init__(self, vertices):
        Graph.__init__(self, vertices)

    def addEdge(self, m, n, weight = 1):
        self._nodeList[m] = Node(m)
        self._nodeList[n] = Node(n)
        self._adjList[m].append(n)
        self._adjMatrix[m][n] = weight
    

