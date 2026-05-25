from random import randint
from math import sqrt

total_iterations = 0
times_inside_circle = 0
radius = 500
centre = (radius,radius)

while True:
    random_point = (
        randint(0,2*radius),
        randint(0,2*radius)
        )
    distance_to_centre = sqrt(
        (centre[0] - random_point[0])**2
        + (centre[1] - random_point[1])**2
        )
    
    if distance_to_centre <= radius:
        times_inside_circle += 1
    total_iterations += 1
    
    if total_iterations % 10 == 0:
        print(times_inside_circle / total_iterations * 4)
    
    