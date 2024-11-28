from figures.Square import *
from figures.Rectangle import *
from figures.Triangle import *
from figures.Circle import *
from figures.Line import *
from figures.Rhombus import *

#creating list
list = []

# appending to list
list.append(Square(40, 20, 15, 25))
list.append(Rectangle(10, 20, 30, 40))
list.append(Triangle(30, 45, 25, 10, 50, 20))
list.append(Circle(95, 40, 90, 70))
list.append(Line(80, 80, 100, 110))
list.append(Rhombus(15, 45, 10, 30, 55, 60))

# output
for obj in list:
    obj.output()

