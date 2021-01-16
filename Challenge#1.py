# Challenge from https://www.youtube.com/watch?v=pvimAM_SLic
# Challenge:
# Given a function that generates a number 0 - 1 (uniformly distributed)
# Calculate the value of PI

import random

num_points = int(input("Enter number of points: "))

def find_pi(num_points):
    num_point_circle = 0
    num_point_total = 0
    for i in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            num_point_circle += 1
        
        num_point_total += 1

    return 4 * num_point_circle/num_point_total

print(find_pi(num_points))