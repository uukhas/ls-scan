class Points:
    """
    Tracks number of successfull and total points.
    """

    def __init__(self, arguments, Scenario):
        try:
            self._ndots = Scenario(1).ndots
        except:
            try:
                self._ndots = arguments.ndots
            except AttributeError:
                print("Either 'arguments' or 'Scenario' must have 'ndots'!")
        self._good = 0

    @property
    def all(self):
        """
        Get number of all points.
        """
        return self._ndots

    def update(self):
        self._good += 1

    def __del__(self):
        print("Total amount of successfull points is", self._good)
