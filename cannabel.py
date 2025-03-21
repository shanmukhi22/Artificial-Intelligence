from collections import deque
class State:
    def __init__(self, m, c, b, p=None): self.m, self.c, self.b, self.p = m, c, b, p
    def is_valid(self): return 0 <= self.m <= 3 and 0 <= self.c <= 3 and (self.m in {0, 3} or self.m >= self.c)
    def is_goal(self): return not (self.m or self.c or self.b)
    def get_successors(self): return [s for m, c in [(1,0), (2,0), (0,1), (0,2), (1,1)] if (s:=State(self.m-m*self.b, self.c-c*self.b, 1-self.b, self)).is_valid()]
def bfs():
    q, v = deque([State(3,3,1)]), set()
    while q:
        if (s:=q.popleft()).is_goal(): return get_solution(s)
        v.update({ns for ns in s.get_successors() if ns not in v}); q.extend(v - set(q))
def get_solution(s):
    p = []
    while s: p.append(s); s = s.p
    return p[::-1]
if __name__ == "__main__":
    if (sol:=bfs()): [print(f"Step {i}: (M={s.m}, C={s.c}, Boat={'Left' if s.b else 'Right'})") for i, s in enumerate(sol)], print("Solution found!")
    else: print("No solution found.")


