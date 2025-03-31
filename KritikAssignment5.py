import matplotlib.pyplot as plt
import random

vertices = [(0, 0), (1, 0), (0.5, 0.866)]


def isInside(x1, y1, x2, y2, x3, y3, x, y):
    def area(x1, y1, x2, y2, x3, y3):

        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)

    return A == A1 + A2 + A3

while True:
    try:
        seed_x = float(input("Enter the x-coordinate of the seed point: "))
        seed_y = float(input("Enter the y-coordinate of the seed point: "))
        if isInside(0, 0, 1, 0, 0.5, 0.866, seed_x, seed_y):
            print("Valid seed point entered.")
            break
        else:
            print("The point is not inside the triangle. Please try again.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")
seed=(seed_x, seed_y)
points = [seed]
while True:
    try:
        num_steps = int(input("Enter the number of steps: "))
        if num_steps > 0:
            print(f"Number of steps set to {num_steps}.")
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
for i in range(num_steps):
     # choose a random vertex to move toward from the list 'vertices'
     # You can use the python code random.randint(0, 2) to
     # choose a random integer between 0 and 2. Then you can use
     # that random integer as the index for a vertex.
     # your code should look like "next_vertex = vertex[ a random choice of index]"

    next_vertex = vertices[random.randint(0,2)]
    next_point = ((points[-1][0]+next_vertex[0])/2,(points[-1][1]+next_vertex[1])/2)
    points.append(next_point)

def plot_solution(points):
    plt.scatter([p[0] for p in points], [p[1] for p in points], s=0.1)
    plt.show()

plot_solution(points)
