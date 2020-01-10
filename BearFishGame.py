from random import randrange, random
from abc import ABCMeta, abstractmethod

BEAR = 1
FISH = 2

ANIMAL_AMOUNT = 2
RIVER_lENGTH = 5

MALE = 1
FEMALE = 2


class Animal(metaclass=ABCMeta):

    type = 0
    _picture = ''
    strength = 0.0
    gender = 0

    def _setParams(self, picture, gender=None, strength=None):
        self._picture = picture
        self.gender = gender if gender is not None else randrange(1, 3)
        self.strength = strength if strength is not None else random()

    def move(self, step_range):
        return randrange(0, step_range)

    def beats(self, animal):
        if self.type == animal.type and self.gender == animal.gender and self.strength >= animal.strength:
            return True
        else:
            return False

    def canPopulate(self, animal):
        if self.type == animal.type and self.gender != animal.gender:
            return True
        else:
            return False

    @abstractmethod
    def eats(self, animal):
        """Returns True if animal eats another animal of animal_type"""

    def __str__(self):
        return "Type: " + self._picture + ", gender: " + str(self.gender) + ", strength: " + str(self.strength)


class Bear(Animal):

    def __init__(self, gender=None, strength=None):
        self._setParams('bear', gender, strength)
        self.type = BEAR

    def eats(self, animal):
        return animal.type in [FISH]


class Fish(Animal):

    def __init__(self, gender=None, strength=None):
        self._setParams('fish', gender, strength)
        self.type = FISH

    def eats(self, animal):
        return animal.type in []


class River:

    def __init__(self, river_length):
        self._river = [None] * river_length
        self._river_length = river_length
        self.fill()

    def getRiver(self):
        return self._river

    def setAnimal(self, Animal, position):
        self._river[position] = Animal

    def findEmptyPlace(self):
        empty_places = []
        for i in range(0, self._river_length):
            if self._river[i] is None:
                empty_places.append(i)
        if empty_places:
            r = randrange(0, len(empty_places))
            return empty_places[r]
        else:
            return -1

    def removeAnimal(self, position):
        self._river[position] = None

    def getAnimal(self, position):
        return self._river[position]

    def fill(self):
        for i in range(0, self._river_length):
            r = randrange(0, ANIMAL_AMOUNT+1)
            if r == BEAR:
                self.setAnimal(Bear(), i)
            if r == FISH:
                self.setAnimal(Fish(), i)

    def __str__(self):
        res = ''
        for i in self._river:
            res += '\n' + str(i)
        return res


class Game:

    def __init__(self, river_length):
        self.river = River(river_length)
        print("River is ", str(self.river))
        self.river_length = river_length
        self.game_over = False

    def next_step(self):
        for i in range(0, self.river_length):
            print("Step ", i)
            animal1 = self.river.getAnimal(i)
            if not isinstance(animal1, Animal):
                print("Animal1 is not Animal")
                continue

            step_position = animal1.move(self.river_length)
            print("Animal ", str(animal1), " moves to ", step_position)
            animal2 = self.river.getAnimal(step_position)
            if animal2 is None:
                print("Animal ", str(animal1), " moves to empty place")
                self.river.setAnimal(animal1, step_position)
                self.river.removeAnimal(i)

            elif animal1.canPopulate(animal2):
                place = self.river.findEmptyPlace()
                print("Animals are of equal type. Creating new ", str(animal1), " at position ", place)
                if place >= 0:
                    self.river.setAnimal(type(animal1)(), place)
                else:
                    print("Game over")
                    self.game_over = True

            elif animal1.beats(animal2) or animal1.eats(animal2):
                print("Animal1 ", str(animal1), " eats/beats ", str(animal2), " and moves to ", step_position)
                self.river.setAnimal(animal1, step_position)

            elif animal2.beats(animal1) or animal2.eats(animal1):
                print("Animal2 ", str(animal2), " eats/beats ", str(animal1), ". Animal1 ", str(animal1), " disappears")
                self.river.removeAnimal(i)

            if self.game_over:
                print("Break")
                break

        print("River after step: ", str(self.river))


#g = Game()
#g.next_step()