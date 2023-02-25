import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, e, start, goal = [int(i) for i in input().split()]

h = []
# heuristics function
for i in input().split():
    node = int(i)
    h.append(node)

# cost function between two points
g = []
for i in range(e):
    x, y, c = [int(j) for j in input().split()]
    g.append([x, y, c])
    # print(x,y,c)

# print(g)

# Finding neighbours


def neighbours(node):
    num = []
    if start == n-1:
        for i in range(len(g)-1, -1, -1):
            if g[i][1] == node:
                num.append(g[i][0])
            elif g[i][0] == node:
                num.append(g[i][1])
    else:
        for i in range(len(g)):
            if g[i][0] == node:
                num.append(g[i][1])
            elif g[i][1] == node:
                num.append(g[i][0])
    return num


def cost(current, neighbor):
    for i in range(len(g)):
        if ((g[i][0] == current and g[i][1] == neighbor) or (g[i][1] == current and g[i][0] == neighbor)):
            return g[i][2]


def filtered(fScore, openSet):
    ind_min = 0
    temp = math.inf
    for i in openSet:
        if fScore[i] < temp:
            temp = fScore[i]
            ind_min = i
    return ind_min


def A_Star(start, goal):
    # the set of frontier
    openSet = [start]
    # cameFrom = [0 for j in range(n)]

    gScore = [math.inf for j in range(n)]
    gScore[start] = 0

    fScore = [math.inf for j in range(n)]
    fScore[start] = h[start]

    while openSet != []:
        #  The set of discovered nodes that may need to be (re-)expanded.
        #  Initially, only the start node is known.
        #  This is usually implemented as a min-heap or priority queue rather than a hash-set.

        # the node in openSet having the lowest fScore[] value
        current = filtered(fScore, openSet)
        openSet.pop(openSet.index(current))

        if (current != goal):
            print("%i %i" % (current, fScore[current]))
        else:
            print("%i %i" % (current, fScore[current]))
            break

        for i in neighbours(current):  # each neighbor of current
            #  d(current,neighbor) is the weight of the edge from current to neighbor
            #  tentative_gScore is the distance from start to the neighbor through current

            tentative_gScore = gScore[current] + cost(current, i)

            if tentative_gScore < gScore[i]:
                #  This path to neighbor is better than any previous one. Record it!
                # cameFrom[i] = current
                gScore[i] = tentative_gScore
                fScore[i] = tentative_gScore + h[i]

                if i not in openSet:
                    openSet.append(i)


A_Star(start, goal)
