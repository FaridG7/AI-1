import timeit

from typing import Callable
from BFS_graph_search import BFSgraphSearch
from BFS_hybrid_search import BFShybridSearch
from BFS_tree_search import BFStreeSearch

def benchmark(func: Callable[[int], str], goal: int) -> str:
    start_time = timeit.default_timer()
    func(goal)
    time_taken = timeit.default_timer() - start_time
    return f"{func.__name__}({goal}) took {time_taken:.6f} seconds"
