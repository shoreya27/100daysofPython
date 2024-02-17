import math
height = float(input('Enter the height of wall (m) ? '))
width = float(input('Enter the width of wall (m) ? '))

coverage = 5

def paint_calc(height, width, coverage):
    return math.ceil((height * width) / coverage)

print(paint_calc(height=height, coverage=coverage, width=width))