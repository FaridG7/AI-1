from collections import deque
import math
from typing import Deque
from Node import Node


def BFStreeSearch(goal:int) -> str:
    if goal % 2 == 0: return f"{BFStreeSearch(goal / 2)}=>{goal}"
    frontier:Deque['Node'] = deque([Node(4.0, None)])
    while len(frontier) > 0:
        L = frontier.popleft()
        for expandedNode in [math.floor(L.state), math.sqrt(L.state), L.state * 2]:
            if expandedNode == goal:
                return f"{L}=> {expandedNode}"
            if expandedNode not in [1, 2, 4, L.state]:
                frontier.append(Node(expandedNode, L))
    return "No path found to the Goal"
