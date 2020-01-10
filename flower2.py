
class Flower:

    def __init__(self, name, num_petals, price):
        self._name = name
        self._petals = num_petals
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_petals(self):
        return self._petals

    def set_petals(self, num_petals):
        self._petals

    def get_price(self):
        return self._price

    def set_price(self, price):
        return self._price

    def __str__(self):
        return " ".join([str(self._name), str(self._petals), str(self._price)])


f = Flower("Rose", 20, 4.5)


class NewFlower(object):

    def __init__(self):
        self._plant = 0

    def grow(self, size):
        self._plant += size
        return self._plant


