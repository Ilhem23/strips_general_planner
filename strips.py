import math
import sys
import multiprocessing
import time
from parser import parser
from state import State
from planner import breadth_first_search

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./strips FILE.TXT")
    file="world_of_cubes.txt"
    with open(sys.argv[1]) as f:
        init, goal, actions = parser(f)

    print("Initial state:")
    print(init)
    print("\n Goal state:")
    print(goal)
    print("\n Actions:")
    for a in actions:
        a.print()
        print()

    current_state = State(init)
    start_time = time.time()
    res = breadth_first_search(current_state, actions, init, goal)
    if res:
        for i in res[1]:
            i.print_name()
        print("Final state: ")
        res[0].print()
        print("--- %s seconds ---" % (time.time() - start_time))
        exit(0)
    else:
        print("--- %s seconds ---" % (time.time() - start_time))
        print("--- The problem have no solution or timeout ---")

