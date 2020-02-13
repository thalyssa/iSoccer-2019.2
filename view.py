class View:

    def __init__(self, state):
        self.state = state

    def prompt(self):
        pass

    def run(self, option):
        pass

    def back(self):
        if len(self.state.view_stack) > 0:
            self.state.view = self.state.view_stack.pop()

    def switch_view(self, next_view):
        self.state.view_stack.append(self)
        self.state.view = next_view
