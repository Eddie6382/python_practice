import numpy as np
from graph import *
        
if __name__ == "__main__":
    g = undirectGraph(4) 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3)
    g.printEdge()

    g.DFStraversal(2)
    g.printCyclic()
    g.printNode(0)
    g.printNode(1)
    g.printNode(2)
    g.printNode(3)
