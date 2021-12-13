import queue
import copy
import itertools as it
import time
from collections import deque


def breadth_first_search(current_state, actions, init, goal):
    time_duration = 120
    time_start = time.time()
    # create an empty FIFO queue that represent the state graph
    # where each state is a couple: State of the world and list of actions
    # that lead from the state of the initial world to the state in question.
    tuple_queue = queue.Queue()
    # initialise the queue with the initial state and empty list of plan(chain of actions)
    # the first node
    tuple_queue.put((current_state, []))
    # get the parameters in the states of initial and goal
    parameters = get_parameters(init, goal)
    # list to save the node visited
    explored = []
    # seen that the Queue is not iterable, I initialise the dequeue to use it in verification
    frontier = deque([(current_state, [])])
    # While the Queue is not empty and time of execution reached the max (2 minute)
    # time to avoid infinite loop
    while tuple_queue and time.time() < time_start + time_duration:
        try:
            # list of new states after applying the action
            new_states = []
            # get the first node in the FIFO : node is tuple{ states, chain_actions}
            node = tuple_queue.get(False)
            # get the list of states in the node
            current_state = node[0]
            # add the current state to the explored set ( mark node as visited)
            explored.append(current_state)
            # function that establish which actions are possible to perform in a current state
            good_actions = get_possible_actions(actions, current_state, parameters)
            # for each action in possible actions according to the current state
            for action in good_actions:
                # create list of chain actions and initialise with the current list of actions
                chain_action = copy.deepcopy(node[1])
                # add the action to the chain actions
                chain_action.append(action)
                # function that returns the state reached performing the action
                # get the postcondition (states) after performing the action
                new_state = action.generate_state(current_state)
                # add the new states and the chain of actions to the Queue
                new_states.append((new_state, chain_action))
            # verify that the node is not visited
            if new_states not in explored and new_states not in frontier:
                # check that all states correspond to the goal state
                for state in new_states:
                    # if the goal node found, the program reach the end, return the node
                    if goal_test(state[0], goal):
                        return state
                # add the node to the Queue
                for state in new_states:
                    tuple_queue.put(state)
                    frontier.append(state)

        except queue.Empty:
            break


# function that retrieve the parameters in the states of initial and goal
def get_parameters(init, goal):
    res = []
    # get the parameters in initial states
    for i in init:
        res += (x for x in i[1])
    # get the parameters in goal state
    for i in goal:
        res += (x for x in i[1])
    # remove the duplicated parameters
    res = list(dict.fromkeys(res))
    return res


# function that verify that the state match to the state goal
def goal_test(curr_state, goal):
    # for each state in goal
    for state in goal:
        # if the state contain the word not,
        # and it is in goal state so the function return false
        if state[0].startswith('not'):
            cp_state = list(state)
            cp_state[0] = ' '.join(state[0].split(' ')[1:])
            if curr_state.contains(tuple(cp_state)):
                return False
        else:
            if not curr_state.contains(state):
                return False
    return True


# function that establish which actions are possible to perform in a current state
def get_possible_actions(listAction, state, parameters):
    res = []
    # for each action
    for action in listAction:
        # get the parameters
        for i in it.permutations(parameters, r=len(action.get_parameters())):
            # for each parameter apply it to the action
            new_action = action.apply_parameters(list(i))
            # check if the current state match to the preconditions of the action
            if goal_test(state, new_action.get_preconditions()):
                res.append(new_action)
    return res
