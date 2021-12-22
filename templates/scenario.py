from random import random

class Scenario:

    ndots = 100 # Overrides the value, defined by -P.

    def __init__(self, i): # Agrument i defines the number of the dot.
        self.input = dict(
            MODSEL_6 = 1
        )
        self.names = [*self.input] + ['MASS_35'] # Entries to save.
