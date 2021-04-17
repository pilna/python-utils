from __future__ import annotations
from math import sqrt, cos, sin, asin, acos, atan

class PolarCoordinate2D:

    def __init__(self, distance: float, angle: float) -> None:
        """
        Parameters
        ----------
        distance: float
            the distance between the coordinate and the origin
        angle: float
            the angle between the abscissa axis, origin and the coordinate
        """
        self.distance = distance
        self.angle = angle

    def get_cartesian_coordinate(self) -> Coordinate2D:
        """
        Calculate the cartesian coordinate of the current coordinate

        Returns
        -------
        Coordinate2D
            the cartesian coordinate of the current polar coordinate
        """
        x = self.distance * cos(self.angle)
        y = self.distance * sin(self.angle)
        return Coordinate2D(x, y)

    def __str__(self) -> str:
        return f"(d: {self.distance}, r: {self.angle})"


class Coordinate2D:

    def __init__(self,x: int, y: int) -> None:
        """
        Parameters
        ----------
        x: int
            the position of the coordinate on the abscissa axis
        y: int
            the position of the coordinate on the ordinate axis
        """
        self.x = x
        self.y = y
    
    def get_euclidian_distance(self, target: Coordinate2D) -> float:
        """
        Calculate the euclidian distance between this coordinate and the 
        coordinate given in parameter.

        Parameters
        ----------
        target: Coordinate2D
            the coordinate which we want to calculate the distance


        Returns
        ------- 
        float
            the euclidian distance between this coordinate and the targeted coordinate

        """
        return sqrt((self.x - target.x)**2 + (self.y - target.y)**2)

    def get_manhattan_distance(self, target: Coordinate2D) -> int:
        """
        Calculate the manhattan distance between this coordinate and the
        coordinate given in parameter.

        Parameters
        ----------
        target: Coordinate2D
            the coordinate which we want to calculate the distance

        Returns
        -------
        int 
            the manhattan distance between this coordinate and the targeted coordinate
        """
        return abs(self.x - target.x) + abs(self.y - target.y)

    def get_breseham_discretization(self, target: Coordinate2D) -> List[Coordinate2D]:
        """
        Calculate the discretization of the segment between this coordinate and the
        coordinate given in parameter.

        Parameters
        ----------
        target: Coordinate2D
            the coordinate which we want to calculate the discretization

        Returns
        -------
        List[Coordinate2D]
            the list of the coordinate needed to join the two Coordinate
        """
        discretization = []
        currentX, currentY = self.x, self.y
        deltaX, deltaY = abs(self.x - target.x), -abs(self.y - target.y)
        shiftX = 1 if self.x < target.x else -1
        shiftY = 1 if self.y < target.y else -1
        error = deltaX + deltaY
        
        while currentX != target.x and currentY != target.y:
            discretization.append(Coordinate2D(currentX, currentY))
            
            if 2 * error >= deltaY:
                error += deltaY
                currentX += shiftX
            if 2 * error >= deltaX:
                error += deltaX
                currentY += deltaY

        return discretization

    def get_angle(self, target: Coordinate2D, pivot: Coordinate2D = None) -> float:
        """
        Calculate the angle between 2 coordinate by contribution to a pivot
        if pivot is not definie we take the origin to calculate the angle

        Parameters
        ----------
        target: Coordinate2D
            the coordinate which we want to calculate the angle

        pivot: Coordinate2D, optional
            the pivot with respect to which the angle is calculated
            default is origin Coordinate(0, 0)

        Returns
        -------
        float
            the angle between this 2 coordinate by contribution to a pivot
        """
        pivot = pivot if pivot != None else Coordinate2D.get_origin()
        fisrtAngle = atan(self.y - pivot.y / self.x - pivot.x)
        secondAngle = atan(target.y - pivot.y / target.x - pivot.x)
        return secondAngle - fisrtAngle

    def get_polar_coordinate(self) -> PolarCoordinate2D:
        """
        Calculate the polar coordinate of the current coordinate

        Returns
        -------
        PolarCoordinate2D
            the polar coordinate of the current coordinate
        """
        distance = self.get_euclidian_distance(Coordinate2D.get_origin())
        angle = asin(self.y / distance)
        return PolarCoordinate2D(distance, angle)

    @classmethod
    def get_origin(cls) -> Coordinate2D:
        """
        return the origin of the plan

        Returns
        -------
        Coordinate2D
            the origin of the plan
        """
        return cls(0, 0)

    def __le__(self, target: Coordinate2D) -> bool:
        """
        Calculate if the current coordinate is the nearest from the origin by the contribution
        of the targeted coordinate.

        Parameters
        ----------
        target: Coordinate2D
            the coordinates with which we want to compare the distance

        Returns
        -------
        True if the current coordinate is nearest from the origin than the targeted coordinate else False
        """
        return self.get_manhattan_distance(self.get_origin()) <= target.get_manhattan_distance(self.get_origin())

    def __lt__(self, target: Coordinate2D) -> bool:
        """
        Calculate if the current coordinate is the nearest from the origin by the contribution
        of the targeted coordinate.

        Parameters
        ----------
        target: Coordinate2D
            the coordinates with which we want to compare the distance

        Returns
        -------
        True if the current coordinate is nearest from the origin than the targeted coordinate else False
        """
        return self.get_manhattan_distance(self.get_origin()) < target.get_manhattan_distance(self.get_origin())

    def __ge__(self, target: Coordinate2D) -> bool:
        """
        Calculate if the current coordinate is the farthest from the origin by the contribution
        of the targeted coordinate.

        Parameters
        ----------
        target: Coordinate2D
            the coordinates with which we want to compare the distance

        Returns
        -------
        True if the current coordinate is nearest from the origin than the targeted coordinate else False
        """
        return self.get_manhattan_distance(self.get_origin()) >= target.get_manhattan_distance(self.get_origin())

    def __gt__(self, target: Coordinate2D) -> bool:
        """
        Calculate if the current coordinate is the farthest from the origin by the contribution
        of the targeted coordinate.

        Parameters
        ----------
        target: Coordinate2D
            the coordinates with which we want to compare the distance

        Returns
        -------
        True if the current coordinate is nearest from the origin than the targeted coordinate else False
        """
        return self.get_manhattan_distance(self.get_origin()) > target.get_manhattan_distance(self.get_origin())

    def __ne__(self, target: Coordinate2D) -> bool:
        """
        Compare 2 Coordinate2D

        Parameters
        ----------
        target: Coordinate2D
            the coordinate we want to compare
        
        Returns
        -------
        True if the 2 coordinate are different  else False
        """
        return not self == target

    def __eq__(self, target: Coordinate2D) -> bool:
        """
        Compare 2 coordinate.

        Parameters
        ----------
        target: Coordinate2D
            the coordinate we want to compare

        Returns
        -------
        True if the 2 coordinate are the same else False
        """
        return self.x == target.x and self.y == target.y

    def __add__(self, target: Coordinate2D) -> Coordinate2D:
        """
        Add 2 coordinate

        Parameters
        ----------
        target: Coordinate2D
            the coordinate we want to add

        Returns
        -------
        Coordinate2D
            the result of the addition
        """
        return Coordinate2D(self.x + target.x, self.y + target.y)

    def __sub__(self, target: Coordinate2D) -> Coordinate2D:
        """
        Substract 2 coordinate

        Parameters
        ----------
        target: Coordinate2D
            the coordinate we want to substract

        Returns
        -------
        Coordinate2D
            the result of the substraction
        """
        return Coordinate2D(self.x - target.x, self.y - target.y)

    def __str__(self) -> str:
        return f"(x: {self.x} y: {self.y})"
