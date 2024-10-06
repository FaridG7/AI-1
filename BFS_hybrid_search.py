import math
from typing import Deque, Set
from Node import Node
from collections import deque



def BFShybridSearch(goal:int) -> str:
    if goal % 2 == 0: return f"{BFShybridSearch(goal / 2)}=>{goal}"
    frontier:Deque['Node'] = deque([Node(4.0, None)])
    explored:Set[int] = set()
    while len(frontier) > 0:
        L = frontier.popleft()
        if L.state == int(L.state):
            explored.add(L.state)
        for expandedNode in [math.floor(L.state), math.sqrt(L.state), L.state * 2]:
            if expandedNode == goal:
                return f"{L}=>{expandedNode}"
            if expandedNode != int(expandedNode):
                frontier.append(Node(expandedNode, L))
            elif expandedNode not in explored:
                frontier.append(Node(expandedNode, L))
    return "No path found to the Goal"

