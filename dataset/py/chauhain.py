from sys import *
setrecursionlimit(100000)
def update(ind, Tree, V, X):
    if Tree[ind] == []:
        return max(-X, V[ind])
    else:
        curV = V[ind]
        for ch in Tree[ind]:
            curV += update(ch, Tree, V, X)
        return max(-X, curV)
        T = int(stdin.readline())
for t in range(T):
        N, X = map(int, stdin.readline().split())
        V = list(map(int, stdin.readline().split()))
    E = [[] for i in range(N)]
    for i in range(N - 1):
        u, v = stdin.readline().split()
        u, v = int(u) - 1, int(v) - 1
        E[u] += [v]
        E[v] += [u] 
    Marked = [0] * N
    Tree = [[] for i in range(N)]
        cands = [0]
    Marked[0]= 1
    while cands:
        newCands = []
        for can in cands:
            for ch in E[can]:
                if Marked[ch] == 0:
                    Marked[ch] = 1
                    Tree[can].append(ch)
                    newCands.append(ch)
        cands = newCands
    print(update(0, Tree, V, X))
            