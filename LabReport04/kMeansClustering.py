import random

Width = 20
Height = 20
NumP = 100
NumC = 10
MaxI = 10

points = [(random.randint(0, Width-1), 
           random.randint(0, Height-1)) 
           for _ in range(NumP)]

clusters = [(random.randint(0, Width-1), 
             random.randint(0, Height-1)) 
             for _ in range(NumC)]

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

for iteration in range(MaxI):
    assignments = [[] for _ in range(NumC)]
    for point in points:
        dist = [manhattan_distance(point, center) for center in clusters]
        minI = dist.index(min(dist))
        assignments[minI].append(point)

    newC = []
    for group in assignments:
        if group:
            avg_x = sum(p[0] for p in group) / len(group)
            avg_y = sum(p[1] for p in group) / len(group)
            newC.append((round(avg_x), round(avg_y)))
        else:
            newC.append((random.randint(0, Width-1), random.randint(0, Height-1)))
    clusters = newC

grid = [['.' for _ in range(Width)] for _ in range(Height)]

for point in points:
    x, y = point
    grid[y][x] = 'P'

for center in clusters:
    x, y = center
    grid[y][x] = 'C'

for row in grid:
    print(' '.join(row))
