from __future__ import annotations
from math import sqrt, cos, sin, asin, acos, atan

class PolarCoordinate2D:

    def __init__(self, distance: float, angle: float) -> None:
        self.distance = distance
        self.angle = angle

    def __str__(self) -> str:
        return f"(d: {self.distance}, r: {self.angle})"


class Coordinate2D:

    def __init__(self,x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def get_euclidian_distance(self, target: Coordinate2D) -> float:
        return sqrt((self.x - target.x)**2 + (self.y - target.y)**2)

    def get_manhattan_distance(self, target: Coordinate2D) -> int:
        return abs(self.x - target.x) + abs(self.y - target.y)

    def get_breseham_discretization(self, target: Coordinate2D) -> List[Coordinate2D]:
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
        pivot = pivot if pivot != None else Coordinate2.get_origin()
        fisrtAngle = atan(self.y - pivot.y / self.x - pivot.x)
        secondAngle = atan(target.y - pivot.y / target.x - pivot.x)
        return secondAngle - fisrtAngle

    def get_polar_coordinate(self) -> PolarCoordinate2D:
        distance = self.get_euclidian_distance(Coordinate2D.get_origin())
        angle = asin(self.y / distance)
        return PolarCoordinate2D(distance, angle)

    @classmethod
    def get_origin(cls) -> Coordinate2D:
        return cls(0, 0)

    def __le__(self, target: Coordinate2D) -> bool:
        return self.get_manhattan_distance() <= target.get_manhattan_distance()

    def __lt__(self, target: Coordinate2D) -> bool:
        return self.get_manhattan_distance() < target.get_manhattan_distance()

    def __ge__(self, target: Coordinate2D) -> bool:
        return self.get_manhattan_distance() >= target.get_manhattan_distance()

    def __gt__(self, target: Coordinate2D) -> bool:
        return self.get_manhattan_distance() > target.get_manhattan_distance()

    def __ne__(self, target: Coordinate2D) -> bool:
        return not self == target

    def __eq__(self, target: Coordinate2D) -> bool:
        return self.x == target.x and self.y == target.y

    def __add__(self, target: Coordinate2D) -> Coordinate2D:
        return Coordinate2D(self.x + target.x, self.y + target.y)

    def __sub__(self, target: Coordinate2D) -> Coordinate2D:
        return Coordinate2D(self.x - target.x, self.y - target.y)

    def __str__(self) -> str:
        return f"(x: {self.x} y: {self.y})"
