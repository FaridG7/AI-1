import os
import platform

from BFS_graph_search import BFSgraphSearch
from BFS_hybrid_search import BFShybridSearch
from BFS_tree_search import BFStreeSearch



def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def main():
    algorithms = {
        '1': BFStreeSearch,
        '2': BFSgraphSearch,
        '3': BFShybridSearch
    }

    while True:
        clear_console()
        print("Select an algorithm:")
        print("1. BFStreeSearch")
        print("2. BFSgraphSearch")
        print("3. BFShybridSearch")

        choice = input("Enter the number of your choice (1-3): ")

        if choice not in algorithms:
            print("Invalid choice! Please select a number between 1 and 3.")
            continue

        goal = input("Enter the goal (an integer): ")

        try:
            goal = int(goal)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue  # Retry the goal input

        result = algorithms[choice](goal)
        print(f"Result: {result}")
        exit()

main()