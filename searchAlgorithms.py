import math
from typing import List, Set
from Node import Node
from Logger import Logger

logger = Logger()

def BFStreeSearch(Goals:List[int]) -> str:
    frontier:List['Node'] = [Node(4.0, None)]
    while len(frontier) > 0:
        logger.log(f"frontier:{frontier}")
        L = frontier.pop(0)
        for expandedNode in [math.floor(L.state), math.sqrt(L.state), L.state * 2]:
            if expandedNode in Goals:
                return f"{L}=> {expandedNode}"
            if not expandedNode in [1, 2, 4, L.state]:
                frontier.append(Node(expandedNode, L))
    return "No path found to the Goal"

def BFShybridSearch(goal:int) -> str:
    if goal % 2 == 0: return f"{BFShybridSearch(goal / 2)}=>{goal}"
    frontier:List['Node'] = [Node(4.0, None)]
    explored:Set[int] = set()
    while len(frontier) > 0:
        logger.log(f"frontier length:{len(frontier)}, explored length: {len(explored)}")
        L = frontier.pop(0)
        if L.state == int(L.state):
            explored.add(L.state)
        for expandedNode in [math.floor(L.state), math.sqrt(L.state), L.state * 2]:
            if expandedNode == goal:
                return f"{L}=>{expandedNode}"
            if not expandedNode in explored:
                frontier.append(Node(expandedNode, L))
    return "No path found to the Goal"

def graphSearch(goal:int) -> str:
    if goal % 2 == 0: return f"{hybridSearch(goal / 2)}=>{goal}"
    frontier:List['Node'] = [Node(4.0, None)]
    explored:Set[float] = set()
    while len(frontier) > 0:
        logger.log(f"frontier length:{len(frontier)}, explored length: {len(explored)}")
        L = frontier.pop(0)
        explored.add(L.state)
        for expandedNode in [math.floor(L.state), math.sqrt(L.state), L.state * 2]:
            if expandedNode == goal:
                return f"{L}=>{expandedNode}"
            if not expandedNode in explored:
                frontier.append(Node(expandedNode, L))
    return "No path found to the Goal"

