from collections import defaultdict
import atexit
import io
import sys
 _INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
  @atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
def dfs(s):
    global value
    for i in d[s]:
        if i!=par[s]:
            par[i] = s
            value[s]+=dfs(i)
    value[s]+=a[s]
    return value[s]
def dfs2(s):
    m = value[s] + x
    t = 0
    for i in d[s]:
        if i!=par[s]:
            t+=dfs2(i)
    return min(t,m)
sys.setrecursionlimit(10**5+1)
for _ in range(int(input())):
        n ,x = map(int,input().split())
    d = [[] for i in range(n)]
    a = list(map(int,input().split()))
    for i in range(n-1):
        u,v = map(int,input().split())
        d[u-1].append(v-1)
        d[v-1].append(u-1)
        value = [0]*(n)
    par = [0]*(n)
    k = dfs(0)
    t = dfs2(0)
    print(k-t)