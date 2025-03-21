import math

def minimax(B, M):
    W = lambda p: any(all(c == p for c in r) for r in B) or any(all(B[r][c] == p for r in range(3)) for c in range(3)) or all(B[i][i] == p for i in range(3)) or all(B[i][2-i] == p for i in range(3))
    if W("X"): return 1
    if W("O"): return -1
    if "-" not in sum(B, []): return 0
    return max((minimax(B, M) if B[r][c] == "-" else -math.inf, B[r][c] := M) for r in range(3) for c in range(3))[0]

def tic_tac_toe():
    B, P = [["-"]*3 for _ in range(3)], "XO"
    for t in range(9):
        print("\n".join(" ".join(r) for r in B))
        m = max(((r, c) for r in range(3) for c in range(3) if B[r][c] == "-"), key=lambda x: minimax(B, "X")) if P[t%2] == "O" else tuple(map(int, input().split()))
        B[m[0]][m[1]] = P[t%2]
        if any(all(B[i][j] == P[t%2] for j in range(3)) for i in range(3)) or any(all(B[j][i] == P[t%2] for j in range(3)) for i in range(3)) or all(B[i][i] == P[t%2] for i in range(3)) or all(B[i][2-i] == P[t%2] for i in range(3)):
            return print("\n".join(" ".join(r) for r in B)), print(f"Player {P[t%2]} wins!")
    print("\n".join(" ".join(r) for r in B)), print("Draw!")

tic_tac_toe()
