# Train Passenger (Codingame Puzzle)

This problem is to find the shortest path between two stations. The environment is `fully observable` because the agent has access to all data about the environment at the first step and deterministic since the next state of the environment can be determined. In other word, the action is taken when the optimum way is derived. Furthermore, the environment remains unchanged while the agent is deliberating, then we can call it static. The agent program used for solving this problem is `Goal-based` agent and being at a particular destination through the shortest way is defined as the goal of this agent.

Based on the goal of this agent, `breadth-first search(BFS)` algorithm is the best choice because the other two, `depth-first search (DFS)` and `Best-first Search(BS)`, find the destination point through the faster way but not, essentially, through the shortest way. All actions in this problem have the same cost which means that BFS is cost-optimal for this. If each edge has the different cost, `Dijkstra’s` algorithm should be used.

The `BFS` algorithm is shown in the below figure. In this algorithm, all leaves are expanded in any stage and all of their successors are expanded in the next stage, and so on. These stages continue until a branch reaches the goal. As can be seen in the following pseudo code, all the successors are put in the frontier to be expanded in the next stages. After finding the optimal way, this way is reconstructed from end to begin by using came from variable as the final part of code. It is worth noting that non-recursive implementation is applied in order to gain better performance and to manage the memory.

```batch
frontier = Queue ()
frontier . put ( start )
came_from = dict ()
came_from [ start ] = None
while not frontier . empty ():
    current = frontier .get ()
    for next in graph . neighbors ( current ):
        if next not in came_from :
            frontier . put ( next )
            came_from [ next ] = current
############# reconstruction path ##############
current = goal
path = []
while current != start :
    path . append ( current )
    current = came_from [ current ]
path . append ( start )
path . reverse ()
```

## References

- https://www.redblobgames.com/
- https://www.codingame.com/training/medium/train-passenger
