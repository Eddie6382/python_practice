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
    def __init__(self):
        self.discover = 0
        self.finish = 0
        self.color = WHITE

    def reset():
        self.discover = 0
        self.finish = 0
        self.color = WHITE

class Graph():
    def __init__(self, vertices):
        self._v = vertices
        self._adjList = [list() for i in range(vertices)]
        self._adjMatrix = [[0]*vertices]*vertices
        self._time = 0

    def printEdge(self):
        for i in range(self._v):
            print(i, self._adjList[i])

    def DFStraversal(self, dfslist):
        self._time = self._time + 1
        


class undirectGraph(Graph):
    def __init__(self, vertices):
        Graph.__init__(self, vertices)
    
    def addEdge(self, u, v, weight = 1):
        self._adjList[u].append(v)
        self._adjMatrix[u][v] = weight
        self._adjMatrix[v][u] = weight

class directGraph(Graph):
    def __init__(self, vertices):
        Graph.__init__(self, vertices)

    def addEdge(self, u, v, weight = 1):
        self._adjList[u].append(v)
        self._adjMatrix[u][v] = weight
    

