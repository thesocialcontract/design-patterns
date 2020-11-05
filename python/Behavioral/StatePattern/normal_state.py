import deficit_state as d
import surplus_state as s

class NormalState:

    def __init__(self, context, value, mini, maxi):
        self.context = context
        self.value = value
        self.min = mini
        self.max = maxi

    def add(self, value):
        self.value += value

        if self.value > self.max:
            self.context.set_state(s.SurplusState(self.context, self.value, self.min, self.max))

    def sub(self, value):
        self.value -= value

        if self.value < self.min:
            self.context.set_state(d.DeficitState(self.context, self.value, self.min, self.max))

    def __str__(self):
        return f"Normal: {self.value}"