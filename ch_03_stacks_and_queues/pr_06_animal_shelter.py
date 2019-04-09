# -*- coding: utf-8 -*-
"""
Animal Shelter

An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out"
basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked list data structure.

"""
import unittest
from .queues import Queue, EmptyQueueError


class Animal:
    """
    Base class for dogs, cats and other animals.

    Attributes:
        name (str): Name of the pet.
        order (int): Serial number of the animal according to the order of entering the shelter.
            Starts from 1. Every animal has unique order regardless of its kind.

    """

    def __init__(self, name, order=None):
        self.name = name
        self.order = order

    def __repr__(self):
        return "{}('{}', {})".format(self.__class__.__name__, self.name, self.order)

    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name and self.order == other.order


class Dog(Animal):
    """
    A dog.
    """
    pass


class Cat(Animal):
    """
    A cat.
    """
    pass


class AnimalShelter:
    """
    Animal shelter implementation using two separate queues for cats and dogs.
    """

    def __init__(self):
        self._dogs = Queue()
        self._cats = Queue()
        self._order = 1

    def add(self, animal):
        """
        Add an animal to the shelter.

        Args:
            animal (Animal): Either Cat or Dog instance.

        Raises:
            TypeError: If animal is neither Dog nor Cat.

        """
        if isinstance(animal, Dog):
            self._dogs.add(animal)
        elif isinstance(animal, Cat):
            self._cats.add(animal)
        else:
            raise TypeError("Unknown species '{}'.".format(type(animal).__name__))
        animal.order = self._order
        self._order += 1

    def remove(self):
        """
        Adopt the animal with the oldest arrival time.

        Returns:
            Animal: First animal in the queue, either Dog or Cat.

        Raises:
            EmptyQueueError: If shelter is empty.

        """
        if self._cats.is_empty():
            return self._dogs.remove()
        if self._dogs.is_empty():
            return self._cats.remove()
        if self._dogs.peek().order < self._cats.peek().order:
            return self._dogs.remove()
        return self._cats.remove()

    def remove_dog(self):
        """
        Adopt the dog with the oldest arrival time.

        Returns:
            Dog: First dog in the queue.

        Raises:
            EmptyQueueError: If there are no dogs in the queue.

        """
        return self._dogs.remove()

    def remove_cat(self):
        """
        Adopt the cat with the oldest arrival time.

        Returns:
            Cat: First cat in the queue.

        Raises:
            EmptyQueueError: If there are no cats in the queue.

        """
        return self._cats.remove()


class TestAnimalShelter(unittest.TestCase):

    def setUp(self):
        self.shelter = AnimalShelter()

    def _test_empty(self):
        self.assertRaises(EmptyQueueError, self.shelter.remove)
        self.assertRaises(EmptyQueueError, self.shelter.remove_dog)
        self.assertRaises(EmptyQueueError, self.shelter.remove_cat)

    def test_animal_shelter(self):
        # []
        s = self.shelter
        self._test_empty()

        # [D1]
        s.add(Dog('D1'))
        self.assertRaises(EmptyQueueError, s.remove_cat)

        # []
        self.assertEqual(s.remove_dog(), Dog('D1', 1))
        self._test_empty()

        # [C2]
        s.add(Cat('C2'))
        self.assertRaises(EmptyQueueError, s.remove_dog)

        # []
        self.assertEqual(s.remove_cat(), Cat('C2', 2))

        # [C3, D4]
        s.add(Cat('C3'))
        s.add(Dog('D4'))

        # []
        self.assertEqual(s.remove(), Cat('C3', 3))
        self.assertEqual(s.remove(), Dog('D4', 4))
        self._test_empty()

        # [D5, D6, C7]
        s.add(Dog('D5'))
        s.add(Dog('D6'))
        s.add(Cat('C7'))

        # [D6, C7]
        self.assertEqual(s.remove_dog(), Dog('D5', 5))

        # [D6, C7, C8, D9]
        s.add(Cat('C8'))
        s.add(Dog('D9'))

        # [D6, C8, D9]
        self.assertEqual(s.remove_cat(), Cat('C7', 7))

        # [D6, C8, D9, C10, D11, D12]
        s.add(Cat('C10'))
        s.add(Dog('D11'))
        s.add(Dog('D12'))

        # [D9, C10, D11, D12]
        self.assertEqual(s.remove(), Dog('D6', 6))
        self.assertEqual(s.remove(), Cat('C8', 8))

        # [D9, C10, D11, D12, C13, C14, D15]
        s.add(Cat('C13'))
        s.add(Cat('C14'))
        s.add(Dog('D15'))

        # [C10, D12, C13, C14, D15]
        self.assertEqual(s.remove_dog(), Dog('D9', 9))
        self.assertEqual(s.remove_dog(), Dog('D11', 11))

        # [C10, D12, C13, C14, D15, D16, C17, C18]
        s.add(Dog('D16'))
        s.add(Cat('C17'))
        s.add(Cat('C18'))

        # [D12, C14, D15, D16, C17, C18]
        self.assertEqual(s.remove_cat(), Cat('C10', 10))
        self.assertEqual(s.remove_cat(), Cat('C13', 13))

        # [D12, C14, D15, D16, C17, C18, C19, D20]
        s.add(Cat('C19'))
        s.add(Dog('D20'))

        # [D16, C17, C18, C19, D20]
        self.assertEqual(s.remove(), Dog('D12', 12))
        self.assertEqual(s.remove(), Cat('C14', 14))
        self.assertEqual(s.remove(), Dog('D15', 15))

        # [D16, C17, C18, C19, D20, C21, D22]
        s.add(Cat('C21'))
        s.add(Dog('D22'))

        # [C18, C19, C21, D22]
        self.assertEqual(s.remove(), Dog('D16', 16))
        self.assertEqual(s.remove_dog(), Dog('D20', 20))
        self.assertEqual(s.remove_cat(), Cat('C17', 17))

        # [C18, C19, C21, D22, D23]
        s.add(Dog('D23'))

        # [C21, D22, D23]
        self.assertEqual(s.remove_cat(), Cat('C18', 18))
        self.assertEqual(s.remove_cat(), Cat('C19', 19))

        # [C21, D22, D23, D24]
        s.add(Dog('D24'))

        # [D23, D24]
        self.assertEqual(s.remove_dog(), Dog('D22', 22))
        self.assertEqual(s.remove(), Cat('C21', 21))
        self.assertRaises(EmptyQueueError, s.remove_cat)

        # [D23, D24, C25]
        s.add(Cat('C25'))

        # [D24]
        self.assertEqual(s.remove_cat(), Cat('C25', 25))
        self.assertEqual(s.remove(), Dog('D23', 23))
        self.assertRaises(EmptyQueueError, s.remove_cat)

        # [D24, C26]
        s.add(Cat('C26'))

        # []
        self.assertEqual(s.remove(), Dog('D24', 24))
        self.assertEqual(s.remove(), Cat('C26', 26))
        self._test_empty()

        with self.assertRaises(TypeError) as cm:
            s.add(Animal('Coco'))
        self.assertEqual(str(cm.exception), "Unknown species 'Animal'.")
