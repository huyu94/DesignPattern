import math
class RoundHole:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def fits(self, peg):
        return self.get_radius() >= peg.get_radius()



class RoundPeg:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

class SquarePeg(RoundPeg):
    def __init__(self, width):
        self._width = width

    def get_width(self):
        return self._width


