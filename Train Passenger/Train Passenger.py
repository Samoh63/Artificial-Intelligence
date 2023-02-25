
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

start = input()
end = input()
n = int(input())

############### Creating nodes and edges#####################
lines = []
nodes = [start]
for i in range(n):
    station_1, station_2 = input().split()
    print(station_1, station_2, file=sys.stderr, flush=True)
    lines.append([station_1, station_2])

    if (station_1 not in nodes) & (station_1 != end):
        nodes.append(station_1)
    if (station_2 not in nodes) & (station_2 != end):
        nodes.append(station_2)
nodes.append(end)


############## finding neigbours of nodes##################
def neighbors(node):
    n = []
    for i in range(len(lines)):
        if lines[i][0] == node:
            n.append(lines[i][1])
        elif lines[i][1] == node:
            n.append(lines[i][0])
    return n


#######################reconstruction path#################
def reconstruction_path():
    path = []
    answer = '%s > ' % start
    current = end
    while current != start:
        path.append(current)
        current = came_from[nodes.index(current)]
    path.pop(0)
    path.reverse()
    for i in path:
        answer = answer+'%s > ' % i
    answer = answer + '%s' % end
    print(answer)


################### Breadth First Algorithm################
frontier = [start]
came_from = [str() for j in range(len(nodes))]
came_from[0] = 'A'

while frontier != []:
    current = frontier[0]
    frontier.pop(0)
    print(current, file=sys.stderr, flush=True)
    nn = neighbors(current)
    for next in neighbors(current):
        ind = nodes.index(next)
        nn = neighbors(current)
        print(nn, file=sys.stderr, flush=True)

        if current == end:
            reconstruction_path()
            break

        if came_from[ind] == '':
            frontier.append(next)
            came_from[ind] = current
            print('frontier=', frontier, file=sys.stderr, flush=True)
            print(came_from, file=sys.stderr, flush=True)


# # Write an answer using print
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)

# print("answer")
