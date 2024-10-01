import math
from typing import List
from Node import Node
from Logger import Logger

logger = Logger()

def treeSearch(Goals:List[int]) -> str:
    frontier:List['Node'] = [Node(4.0, None)]
    while len(frontier) > 0:
        logger.log(f"frontier:{frontier}")
        L = frontier.pop(0)
        
        for expandedNode in [math.floor(L.state), math.sqrt(L.state), L.state * 2]:
            if expandedNode in Goals:
                return f"{L}, {expandedNode}"
            if not expandedNode in [1, 2, 4, L.state]:
                frontier.append(Node(expandedNode, L))
    return "No path found to the Goal"