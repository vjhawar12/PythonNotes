point = (1, 2, 3) # representaitno of a point in x y z coordinates 
 
print(point[1]) # to print out the y coordinate 

from collections import namedtuple 

Point = namedtuple('Point', ['x', 'y', 'z']) # creating a Point class that has x, y, z componenets

coordinates = Point(1, 2, 3) # creating an instance of a point class 

print(coordinates.x) # printing out the x coordinate
print(coordinates.y)
print(coordinates.z)










 