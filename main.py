from treeSearch import treeSearch
from Logger import Logger

logger = Logger()

def get_user_input() -> int:
    while True:
        user_input = input("Please enter an integer: ")
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("That is not a valid integer. Please try again.")

goal = get_user_input()

logger.log(f"user input(goal): {goal}")

print(treeSearch([goal]))

logger.log("run ended.")