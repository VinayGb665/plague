import sys
def dfs(j):
    global vis
    v = r = 0
    for i in d[j]:
        if vis[i]:
            vis[i] = False
            t = dfs(i)
            r += t[0]
            v += t[1]
    v = a[j] + v
    return (min(r,v+x),v)
sys.setrecursionlimit(10**5+1)
t = int(input())
for test in range(t):
        nx = input().split()
    n  = int(nx[0])
    x = int(nx[1])
        d = [[] for i in range(n)]
    a = list(map(int,input().split()))
    for i in range(n-1):
        uv = input().split()
        u  = int(uv[0])
        v = int(uv[1])
        d[u-1].append(v-1)
        d[v-1].append(u-1)
        value = [0]*(n)
    vis = [True]*(n)
    vis[0] = False
    t = dfs(0)
    print(t[1]-t[0])