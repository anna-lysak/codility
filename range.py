class Range:
    """A class that mimic s the built-in range class."""

    def __init__ (self, start, stop=None, step=1):
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError("step cannot be 0")

        if stop is None: # special case of range(n)
            start, stop = 0, start # should be treated as if range(0,n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support getitem
        self._start = start
        self._step = step
        self._stop = stop

    def __len__ (self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__ (self, k):
        """Return entry at index k (using standard interpretation if negative)."""
        if k < 0:
            k += len(self) # attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexError("index out of range")

        return self._start + k * self._step


    def __contains__(self, item):
        """Checks """
        if self._step < 0 and (item < self._stop or item > self._start):
            return False

        if self._step > 0 and (item < self._start or item > self._stop):
            return False

        # if we can find integer K (index of element in range) then item is from range
        if (item - self._start) % self._step == 0:
            return True

        return False


x = Range(0, 10, 2)
y = Range(10, 0, -2)

print(4 in x)
print(5 in x)
print(12 in x)
print(-2 in x)

print(4 in y)
print(5 in y)
print(12 in y)
print(-2 in y)
