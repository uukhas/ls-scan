import numpy
import math

class SimpleGrid:
    """
    Creates a simple rectangular grid of any dimensions.

    To use:
    >>> grid = SimpleGrid(first=(-3, -2, 2), second=(-1, 1, 11))
    >>> grid.first(1) # here i=1: floor(i/11) % 2
    -3
    >>> grid.second(35) # here i=35: i % 11
    -0.6
    """
    def __init__(self, **kwargs):
        items = sorted(kwargs.items(),
                       key=lambda el: el[1][2],
                       reverse = True)
        attrs = [el[0] for el in items]
        regs = [numpy.linspace(*el[1]) for el in items]
        den = [el[1][-1] for el in items]
        self.ndots = numpy.prod(den)
        mod = den.copy()
        for el in range(len(den)-2):
            den[el+1] = den[el+1] * den[el]
        setattr(self, attrs[0], lambda i: regs[0][i % den[0]])
        for el in range(len(den)-1):
            setattr(self,
                    attrs[el+1],
                    lambda i, el=el:
                        regs[el+1][math.floor(i/den[el]) % mod[el+1]])
