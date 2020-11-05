import normal_state as n
import surplus_state as s

class DeficitState():
    def __init__(self, context, value, mini, maxi):
        self.context = context
        self.value = value
        self.min = mini
        self.max = maxi

    def add(self, value):
        self.value += value

        if self.min <= self.value and self.value <= self.max:
            self.context.set_state(n.NormalState(self.context, self.value, self.min, self.max))
        elif self.max < self.value:
            self.context.set_state(s.SurplusState(self.context, self.value, self.min, self.max))

    def sub(self, value):
        print(f"In deficit, cannot subtract.  Value ({self.value}) is outside of range.")

    def __str__(self):
        return f"Deficit:\t{self.value}"