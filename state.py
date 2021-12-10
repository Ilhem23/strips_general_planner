class State:
    def __init__(self, states=list()):
        self.states = states

    def remove_state(self, state):
        self.states.remove(state)

    def add_state(self, state):
        self.states.append(state)

    def get_states(self):
        return self.states

    def contains(self, state_to_check):
        for state in self.states:
            if state == state_to_check:
                return True
        return False

    def print(self):
        print(self.states)
