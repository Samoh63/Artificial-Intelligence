# A-Star Exercise (Codingame Puzzle)

In this problem, the shortest path between two cities must be found. We are given an undirected graph and unlike the previous problem, there are weighted edges and for each node the heuristic value, which is the estimated distance to the end, is determined. This problem, also, is `fully observable`, `deterministic` and `static` and its agent program is Goal-based. Since the amount of heuristic function for each point is defined, the A-star algorithm is the best choice for this problem. The A-star search algorithm developed for writing code is shown in the following figure. In this method, all the successors are put in the `frontier` but the point with the minimum cost function is selected for expanding in each stage. The cost function for point n in this method is the cost from the initial state to the node, `new case` variable, plus the estimated cost of the shortest path from `n` to a goal state, heuristic variable.

```batch
frontier = PriorityQueue ()
frontier . put (start , 0)
came_from = dict ()
cost_so_far = dict ()
came_from [ start ] = None
cost_so_far [ start ] = 0
while not frontier.empty ():
    current = frontier .get ()
    if current == goal :
        break
    for next in graph . neighbors ( current ):
        new_cost = cost_so_far [ current ] + graph . cost ( current , next )
        if next not in cost_so_far or new_cost < cost_so_far [ next ]:
            cost_so_far [ next ] = new_cost
            priority = new_cost + heuristic (goal , next )
            frontier . put (next , priority )
            came_from [ next ] = current

```

## References

- https://www.redblobgames.com/
- https://www.codingame.com/training/medium/a-star-exercise
