from parcial1_2014.exercise4.Line import Line
from parcial1_2014.exercise4.Point import Point
from parcial1_2014.exercise4.Polygon import Polygon

p1 = Point(0, 0)
print("Point org: " + str(p1))
l1 = Line(p1, Point(0, 100))
print("Vertical line 100 pts.: " + str(l1))
polygon = Polygon([l1.getStart(), l1.getEnd(), Point(100, 100), Point(100, 0)])
print("Square: " + str(polygon))
