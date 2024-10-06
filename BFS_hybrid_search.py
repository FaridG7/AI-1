import math
from typing import List, Set
from Node import Node
# from uselessFiles.Logger import Logger

# logger = Logger()


def BFShybridSearch(goal:int) -> str:
    if goal % 2 == 0: return f"{BFShybridSearch(goal / 2)}=>{goal}"
    frontier:List['Node'] = [Node(4.0, None)]
    explored:Set[int] = set()
    while len(frontier) > 0:
        # logger.log(f"frontier length:{len(frontier)}, explored length: {len(explored)}")
        L = frontier.pop(0)
        if L.state == int(L.state):
            explored.add(L.state)
        for expandedNode in [math.floor(L.state), math.sqrt(L.state), L.state * 2]:
            if expandedNode == goal:
                return f"{L}=>{expandedNode}"
            if not expandedNode in explored:
                frontier.append(Node(expandedNode, L))
    return "No path found to the Goal"
