import math
import numpy as np

def is_triangle(a, b, c):

    sides = [a,b,c]
    sides.sort()
    return bool(sum(sides[:2]) <=  sides[2])


print(is_triangle(3,4,5 ))
