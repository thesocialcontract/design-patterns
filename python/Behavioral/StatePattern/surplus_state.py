import normal_state as n 
import deficit_state as d

class SurplusState:
    def __init__(self, context, value, mini, maxi):
        self.context = context
        self.value = value
        self.min = mini
        self.max = maxi

    def sub(self, value):
        self.value -= value

        if self.min <= self.value and self.value <= self.max:
            self.context.set_state(n.NormalState(self.context, self.value, self.min, self.max))
        elif self.value < self.min:
            self.context.set_state(d.DeficitState(self.context, self.value, self.min, self.max))

    def add(self, value):
        print(f"In surplus, cannot add.  Value ({self.value}) is outside of range.")

    def __str__(self):
        return f"Surplus:\t{self.value}"