#Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

import math
import numpy as np

def is_triangle(a, b, c):

    sides = [a,b,c]
    sides.sort()
    return bool(sum(sides[:2]) <=  sides[2])


print(is_triangle(3,4,5 ))
