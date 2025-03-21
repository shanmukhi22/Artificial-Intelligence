import numpy as np
from queue import PriorityQueue
def heuristic(state): return sum(state[i] != (i + 1) % 9 for i in range(9))
def a_star(start):
    goal, pq, visited = [1, 2, 3, 4, 5, 6, 7, 8, 0], PriorityQueue(), {tuple(start)}
    pq.put((0, start, []))
    while pq:
        cost, current, path = pq.get()
        if current == goal: return path + [current]
        for i in range(9):
            if current[i] == 0:
                for j in [-1, 1, -3, 3]:
                    if 0 <= i + j < 9 and (i % 3 != 0 or j != -1) and (i % 3 != 2 or j != 1):
                        next_state = current[:]
                        next_state[i], next_state[i + j] = next_state[i + j], next_state[i]
                        if tuple(next_state) not in visited:
                            visited.add(tuple(next_state))
                            pq.put((cost + heuristic(next_state), next_state, path + [current]))
    return None
solution_path = a_star([1, 2, 3, 4, 5, 6, 0, 7, 8])
if solution_path: 
    for state in solution_path: print(np.array(state).reshape(3, 3), "\n")
else: 
    print("No solution.")
