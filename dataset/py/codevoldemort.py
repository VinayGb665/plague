from sys import setrecursionlimit as sr,stdin,stdout
input=stdin.readline
sr(1000000)
def dfs(i):
    x=a[i]
    for j in b[i]:
        if vis[j]==0:
            vis[j]=1
            dfs(j)
            x+=r[j]
    r[i]=x 
def cc(j):
    m=r[j]+x
    t=0
    for i in b[j]:
        if vis[i]==0:
            vis[i]=1
            t+=cc(i)
    return min(t,m)
for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=[[] for i in range(n)]
    r=[0]*n
    vis=[0]*n
    su=sum(a)
    for i in range(n-1):
        c,d=map(int,input().split())
        b[c-1].append(d-1)
        b[d-1].append(c-1)
    vis[0]=1
    dfs(0)
    vis=[0]*n
    vis[0]=1
    m=cc(0)
    stdout.write(str(su-m)+'\n')