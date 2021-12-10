class Action:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
        self.preconditions = []
        self.postconditions = []

    def add_preconditions(self, precondition):
        self.preconditions.append(precondition)

    def add_postconditions(self, postcondition):
        self.postconditions.append(postcondition)

    def get_preconditions(self):
        return self.preconditions

    def get_postconditions(self):
        return self.postcondition

    def print_name(self):
        print("{}({})".format(self.name, ', '.join(x for x in self.parameters)))
