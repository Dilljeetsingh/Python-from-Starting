# calculate the circumference of a circle
# formula is C = 2 pie R

import math

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}")