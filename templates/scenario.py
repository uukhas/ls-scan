from random import random

class Scenario:

    ndots = 100 # Overrides the value, defined by -D.

    def __init__(self, i): # Agrument i defines the number of the dot.
        self.input = dict(
            MODSEL_6 = 1
        )
        self.output = [*self.input] + ['MASS_35'] # Entries to save.
