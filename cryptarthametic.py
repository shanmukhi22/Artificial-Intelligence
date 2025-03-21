from itertools import permutations

def cryptarithmetic():
    for p in permutations(range(10), 8):
        S, E, N, D, M, O, R, Y = p
        if S and M and (SEND := S*1000 + E*100 + N*10 + D) + (MORE := M*1000 + O*100 + R*10 + E) == (MONEY := M*10000 + O*1000 + N*100 + E*10 + Y):
            return f"Solution Found:\nS={S}, E={E}, N={N}, D={D}, M={M}, O={O}, R={R}, Y={Y}\n\n{SEND} + {MORE} = {MONEY}"

print(cryptarithmetic() or "No solution found.")


