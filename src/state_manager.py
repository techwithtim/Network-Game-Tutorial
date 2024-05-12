class StateManager:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def change_state(self, new_state):
        self.current_state = new_state

    def run(self, entity):
        self.current_state.run(entity)
