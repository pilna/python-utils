from unittest import TestCase, main
from Coordinate2D import Coordinate2D

class TestCoordinate2D(TestCase):

    def test_euclidian_distance_int(self): 
        firstCoordinate = Coordinate2D(0, 3)
        secondCoordinate = Coordinate2D(3, 3)
        euclidianDistance = firstCoordinate.get_euclidian_distance(secondCoordinate)
        self.assertEqual(3, euclidianDistance)

    def test_euclidian_distance_float(self):
        firstCoordinate = Coordinate2D(0, 2)
        secondCoordinate = Coordinate2D(4, 7)
        euclidianDistance = firstCoordinate.get_euclidian_distance(secondCoordinate)
        delta = abs(euclidianDistance - 6.40312)
        self.assertEqual(True, delta < 0.00001)

    def test_manhattan_distance(self):
        firstCoordinate = Coordinate2D(3, 4)
        secondCoordinate = Coordinate2D(0, 13)
        manhattanDistance = firstCoordinate.get_manhattan_distance(secondCoordinate)
        self.assertEqual(12, manhattanDistance)

    def test_breseham_discretization(self):
        # TODO
        pass
    
    def test_get_angle(self):
        # TODO
        pass

    def test_polar_coordinate(self):
        # TODO
        pass

    def test_get_origin(self):
        self.assertEqual(True, Coordinate2D(0, 0) == Coordinate2D.get_origin())

    def test_le_ne(self):
        firstCoordinate = Coordinate2D(4, 4)
        secondCoordinate = Coordinate2D(1, 2)
        self.assertEqual(True, secondCoordinate <= firstCoordinate)

    def test_le_eq(self):
        firstCoordinate = Coordinate2D(3, 3)
        secondCoordinate = Coordinate2D(-3, -3)
        self.assertEqual(True, firstCoordinate <= secondCoordinate)

    def test_lt(self):
        firstCoordinate = Coordinate2D(4, 4)
        secondCoordinate = Coordinate2D(1, 2)
        self.assertEqual(True, secondCoordinate < firstCoordinate)

    def test_ge_eq(self):
        firstCoordinate = Coordinate2D(3, 3)
        secondCoordinate = Coordinate2D(-3, -3)
        self.assertEqual(True, firstCoordinate >= secondCoordinate)

    def test_ge_ne(self):
        firstCoordinate = Coordinate2D(4, 4)
        secondCoordinate = Coordinate2D(1, 2)
        self.assertEqual(False, secondCoordinate >= firstCoordinate)

    def test_gt(self):
        firstCoordinate = Coordinate2D(4, 4)
        secondCoordinate = Coordinate2D(1, 2)
        self.assertEqual(False, secondCoordinate > firstCoordinate)

    def test_ne(self):
        firstCoordinate = Coordinate2D(4, 2)
        secondCoordinate = Coordinate2D(6, 9)
        self.assertEqual(True, firstCoordinate != secondCoordinate)

    def test_eq(self):
        firstCoordinate = Coordinate2D(2, 7)
        secondCoordinate = Coordinate2D(2, 7)
        self.assertEqual(True, firstCoordinate == secondCoordinate)

    def test_add(self):
        firstCoordinate = Coordinate2D(3, 3)
        secondCoordinate = Coordinate2D(1, 2)
        self.assertEqual(True, firstCoordinate + secondCoordinate == Coordinate2D(4, 5))

    def test_sub(self):
        firstCoordinate = Coordinate2D(3, 5)
        secondCoordinate = Coordinate2D(2, 4)
        self.assertEqual(True, firstCoordinate - secondCoordinate == Coordinate2D(1, 1))

if __name__ == "__main__":
    main()
