
class Vector:
    """ Represent a vector in a multidimensional space. """

    def __init__(self, val):
        """ Create d-dimensional vector of zeros."""
        if type(val) == int:
            self._coords = [0] * val
        else:
            try:
                if len(val) != 0:
                    self._coords = [0] * len(val)
                    index = 0
                    for i in val:
                        self._coords[index] = int(i)
                        index += 1

            except (TypeError, ValueError):
                raise ValueError("Sequence of integers is expected")

    def __len__(self):
        """ Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other): # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        """Return sum of two vectors. Other first in addition"""
        if len(self) != len(other): # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = other[j] + self[j]
        return result

    def __sub__(self, other):
        """Return difference between two vectors."""
        if len(self) != len(other): # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        """Return negative values of vector."""
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result

    def __mul__(self, other):
        result = 0  # start with vector of zeros
        if isinstance(other, int):
            for j in range(len(self)):
                result += self[j] * other
        else:
            """Return scalar from multiplication of two vectors"""
            if len(self) != len(other): # relies on len method
                raise ValueError("dimensions must agree")
            for j in range(len(self)):
                result += self[j] * other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other # rely on existing eq definition

    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self._coords)[1:-1] + ">"  # adapt


class DVector(Vector):

    def __init__(self, d, e):
        super().__init__(d)
        self._dcoords = self._coords * e

    def __str__(self):
        return str(self._dcoords)

