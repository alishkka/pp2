import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

# Example usage
degree = 15
radian = degree_to_radian(degree)
print(f"Input degree: {degree}")
print(f"Output radian: {radian:.6f}")


def area_of_trapezoid(height, base1, base2):
    return (base1 + base2) * height / 2

# Example usage
height = 5
base1 = 5
base2 = 6
area = area_of_trapezoid(height, base1, base2)
print(f"Height: {height}")
print(f"Base, first value: {base1}")
print(f"Base, second value: {base2}")
print(f"Expected Output: {area}")


import math

def area_of_polygon(num_sides, side_length):
    return (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))

# Example usage
num_sides = 4
side_length = 25
area = area_of_polygon(num_sides, side_length)
print(f"Input number of sides: {num_sides}")
print(f"Input the length of a side: {side_length}")
print(f"The area of the polygon is: {area:.1f}")


def area_of_parallelogram(base, height):
    return base * height

# Example usage
base = 5
height = 6
area = area_of_parallelogram(base, height)
print(f"Length of base: {base}")
print(f"Height of parallelogram: {height}")
print(f"Expected Output: {area}")