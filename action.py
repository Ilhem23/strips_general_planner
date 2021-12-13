import copy


class Action:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
        self.preconditions = []
        self.postconditions = []

    def get_parameters(self):
        return self.parameters

    # function to replace the parameters with parameters in initial state
    def apply_parameters(self, parameters):
        new_action = Action(self.name, parameters)
        for precondition in self.preconditions:
            new_parameter = []
            for param in precondition[1]:
                try:
                    idx = self.parameters.index(param)
                    new_parameter.append(parameters[idx])
                except ValueError:
                    new_parameter.append(param)
            new_action.add_preconditions((precondition[0], new_parameter))

        for postcondition in self.postconditions:
            new_parameter = []
            for param in postcondition[1]:
                try:
                    idx = self.parameters.index(param)
                    new_parameter.append(parameters[idx])
                except ValueError:
                    new_parameter.append(param)
            new_action.add_postconditions((postcondition[0], new_parameter))

        return new_action

    # function that returns the state reached performing the action
    # get the postcondition (states) after performing the action
    def generate_state(self, state):
        new_state = copy.deepcopy(state)
        for st in self.postconditions:
            # if the postcondition contain not before state so the state will be removed
            if st[0].startswith('not'):
                l_st = list(st)
                l_st[0] = ' '.join(l_st[0].split(' ')[1:])
                new_state.remove_state(tuple(l_st))
            else:
                new_state.add_state(st)
        return new_state

    def add_preconditions(self, preconditions):
        self.preconditions.append(preconditions)

    def add_postconditions(self, postconditions):
        self.postconditions.append(postconditions)

    def get_preconditions(self):
        return self.preconditions

    def get_postconditions(self):
        return self.postconditions

    def print(self):
        print(self.name, self.parameters)
        print(self.preconditions)
        print(self.postconditions)

    def print_name(self):
        print("{}({})".format(self.name, ', '.join(x for x in self.parameters)))


