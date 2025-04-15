# calculate the hypotenuse of a right triangle

import math

a = float(input("Enter the value A for a triangle: "))
b = float(input("Enter the value B for a triangle: "))

C = math.sqrt( (pow( a, 2)) + (pow (b, 2)) )

print(f"The hypotenuse of right triangle is: {round(C , 2)}cm")