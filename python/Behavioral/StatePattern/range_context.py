class RangeContext:
    """ This object could be anything that contains a "State" pattern object.
    It doesn't have to be explicitly "Context".  It only needs to defer state
    based behavior to a state object that it owns.

    Context owns a RangeState object.

    RangeState can be NormalState, DeficitState, or SurplusState.
    
    """

    def __init__(self):
        self.state = None

    def set_state(self, state):
        old_state = self.state
        self.state = state
        print(f"Changing from {old_state} to {state}")

    def add(self, value):
        self.state.add(value)
        print(str(self.state))

    def sub(self, value):
        self.state.sub(value)
        print(str(self.state))