import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

rooms = []
room_splited = []

for i in range(n):
    room = input()
    room_splited = room.split(' ')
    ############convert string to digit#####################
    for i in range(0, len(room_splited)):
        if room_splited[i] == 'E':
            room_splited[i] = n
        else:
            room_splited[i] = int(room_splited[i])

    rooms.append(room_splited)
rooms.append([n, 0, n, n])


############## finding neigbours of nodes##################
def neighbors(node):
    nn = []
    if rooms[node][2] == rooms[node][3]:
        nn.append(rooms[node][2])
    else:
        for j in [2, 3]:
            nn.append(rooms[node][j])
            visited[rooms[node][j]] = visited[rooms[node][j]] + 1
    return nn

########################Creating priority queue for frontier#########


def priority_queue(frontier, next):

    if frontier == []:
        frontier.append(next)
    else:
        for i in range(0, len(frontier)):

            if next[1] > frontier[i][1]:
                frontier.insert(i, next)
                return frontier
            elif i == len(frontier)-1:
                frontier.append(next)
                return frontier

################### Dijkstra’s Algorithm ##################


frontier = [[0, rooms[0][1]]]
cost_so_far = [0 for i in range(n+1)]
came_from = ['' for i in range(n+1)]
visited = [0 for i in range(n+1)]

while True:

    current = frontier[0]
    frontier.pop(0)

    if visited[current[0]] > 400 and current[0] != n+1:
        continue

    for next in neighbors(current[0]):
        new_cost = current[1] + rooms[next][1]
        if new_cost > cost_so_far[next]:  # next not in cost_so_far or
            cost_so_far[next] = new_cost
            priority_queue(frontier, [next, new_cost])
            came_from[next] = current

    if frontier == []:
        break

print(cost_so_far[n])
