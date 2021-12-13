from action import Action


# general function to parse return the name and argument in tuple
def param_parser(line):
    name = line[:line.find('(')]
    rest_of_the_line = line[line.find(')') + 1:]
    rest_of_the_line = rest_of_the_line.strip(', ')
    line = line[line.find('(') + 1:line.find(')')]
    args = line.split(',')
    args = [a.strip(' ') for a in args]
    return name, args, rest_of_the_line


# parser function for actions
def parse_action(file):
    # retrieve the first line
    line = file.readline().split()
    if not line:
        return None
    # if the line is comment
    # retrieve the next line
    if line[0] == "//":
        line = file.readline().split()
    # call function that parse action line into a tuple of name and argument
    # retrieve the name and argument of action
    action_name, args, new_line = param_parser(' '.join(line))
    # create action with name and arguments
    action = Action(action_name, args)
    # loop to extract the precondition and the postcondition
    for i in range(0, 2):
        conditions = file.readline().split()
        conditions_cpy = conditions[1:]
        new_line = ' '.join(conditions_cpy)
        while len(new_line):
            # extract the name and params of each precondition or postcondition
            name, args, new_line = param_parser(new_line)
            # add condition to the action
            (action.add_preconditions((name, args)) if conditions[0] == 'Preconditions:'
             else action.add_postconditions((name, args)))
    return action


# general function to parse the initial state, actions, goal
def parser(file):
    # initial state list
    init_state = []
    # the goal list
    goal = []
    # the list of actions
    actions = []
    # for each line in the txt file
    for line in file:
        # convert the line string to list
        words = line.split()
        # verify if the list is not empty
        if not len(words):
            continue
        # verify if the first line contains the word state
        if len(words) > 1 and words[1] == "state:":
            # retrieve the whole line without the word state  and put it in new list
            words_copy = words[2:]
            # convert to string
            new_line = ' '.join(words_copy)
            # loop over the line
            while len(new_line):
                # parse the line into name and parameters using the param_parser function
                name, args, new_line = param_parser(new_line)
                # if the line contains the word Initial, so add the parameters in init list, else put it in goal
                (init_state.append((name, args)) if words[0] == "Initial"
                 else goal.append((name, args)))
        # verify if the line contains the word actions, if the line do not contain state word
        elif words[0] == 'Actions:':
            # read all actions in the file
            while True:
                # parse the action with the parse action function
                action = parse_action(file)
                # verify if the action is empty, get out of the loop, else add the action parsed in action list
                if action is None:
                    break
                actions.append(action)
                # next action
                file.readline()
        else:
            raise ValueError("Not a valid keyword: {}".format(words))
    return init_state, goal, actions
