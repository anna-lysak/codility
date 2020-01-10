class SequenceIterator:
    """An iterator for any of Python s sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence # keep a reference to the underlying data
        self._k = -1 # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1 # advance to next index
        if self._k < len(self._seq):
            return self._seq[self._k] # return the data element
        else:
            raise StopIteration() # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


class SequenceReverseIterator:
    """An iterator for any of Python s sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence # keep a reference to the underlying data
        self._k = len(sequence) # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k -= 1 # advance to next index
        if self._k >= 0:
            return self._seq[self._k] # return the data element
        else:
            raise StopIteration() # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


from abc import ABCMeta, abstractmethod # need these definitions


class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__ (self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__ (self, j):
        """Return the element at index j of the sequence."""

    def __contains__ (self, val):
        if len(self) - val > val:
            """Return True if val found in the sequence; False otherwise."""
            for j in range(0, len(self)):
                if self[j] == val: # found match
                    return True
        else:
            for j in range(len(self)-1, -1, -1):
                if self[j] == val: # found match
                    return True
        return False

    def __eq__(self, other):
        """Return true if two sequences are equal"""
        if len(self) != len(other):
            return False
        for j in range(len(self)):
            if self[j] != other[j]:
                return False
        return True

    def __lt__(self, other):
        """Return true if sequence is less than other"""
        for j in range(len(self)):
            if self[j] >= other[j]:
                return False
        return True

    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val: # leftmost match
                return j
        raise ValueError("value not in sequence") # never found a match

    def count(self, val):
        """Return the number of elements equal to given value."""
        k=0
        for j in range(len(self)):
            if self[j] == val: # found a match
                k += 1
        return k


class MySequence(Sequence):

    def __len__(self):
        return len(self)

    def __getitem__(self, j):
        return self[j]


class BookNavigation:

    def selectBook(self, Book):
        pass

    def openBook(self, Book):
        pass

    def moveForward(self):
        pass

    def moveBack(self):
        pass

    def moveDown(self):
        pass

    def moveUp(self):
        pass


class eBookReader(BookNavigation):

    _opened = True

    def __init__(self):
        pass

    def open(self):
        pass

    def close(self):
        pass

    def _getBooks(self, nBooks, purchased):
        pass

    def displayBooklist(self, Books):
        pass

    def displayPurchasedBookslist(self, Books):
        pass

    def goToBookslist(self, purchased):
        pass


class BookMixin:

    def buyBook(self, name):
        pass

    def _charge(self, name, price):
        pass

    def getBooks(self, startFromN, amount, purchased):
        pass


class Book(BookMixin):

    name = ''
    author = ''
    description = ''
    picture = 'path'
    price = 0.0
    bought = True

    def preview(self):
        pass

    def open(self):
        pass

    def nextPage(self):
        pass

    def prevPage(self):
        pass

    def searchPage(self, pNumber):
        pass

    def _displayPage(self, pNumber):
        pass


class Booklist(BookMixin, BookNavigation):
    lst = 'lst'
    grid = 'grid'
    mode = (lst, grid)
    nRows = 0
    nCols = 0
    nBooks = 0

    def __init__(self, nRows, nCols, nBooks, mode):
        pass

    def displaylist(self, Books):
        pass

    def displayGrid(self, Books):
        pass

    def scroll(self, mode):
        pass

    def searchBook(self, searchString):
        pass

    def _getNextBooks(self, amount):
        return Book

    def switchMode(self):
        pass


class PurchasedBooklist(Booklist):
    _purchased = True






