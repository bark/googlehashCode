import itertools
import math

# Takes a list of houses (x,y) and starting point (x, x),
# returns length and path as (pathLength, [start, node1, ... , start])
def shortestPath(houseList, start):
    permu = list(itertools.permutations(houseList))
    allRoutes = []
    while permu:
        route = list(permu.pop())
        route.append(start)
        route.insert(0, (0,0))
        allRoutes.append(route)
    lengths = map(pathLength, allRoutes)
    lengthAndRoute = zip(lengths, allRoutes)
    return min(lengthAndRoute)

def pathLength(houses):
    length = 0
    for x in range(len(houses) - 1):
        x1 = houses[x][0]
        y1 = houses[x][1]
        x2 = houses[x+1][0]
        y2 = houses[x+1][1]
        length = length + math.ceil(distance(x1, y1, x2, y2))
    return length

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)