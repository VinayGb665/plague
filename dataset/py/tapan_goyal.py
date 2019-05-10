from math import gcd
import bisect
import itertools
import sys
from collections import deque
I=lambda : sys.stdin.readline()
mod=10**9 +7
sys.setrecursionlimit(1000000)
'''fact=[1]*100001
ifact=[1]*100001
for i in range(1,100001):
    fact[i]=((fact[i-1])*i)%mod
    ifact[i]=((ifact[i-1])*pow(i,mod-2,mod))%mod
def ncr(n,r):
    return (((fact[n]*ifact[n-r])%mod)*ifact[r])%mod
def npr(n,r):
    return (((fact[n]*ifact[n-r])%mod))
    '''
def modu(a,m):
    if a%m:
        return a%m
    return m
def mindiff(a):
    b=a[:]
    b.sort()
    m=10000000000
    for i in range(len(b)-1):
        if b[i+1]-b[i]<m:
            m=b[i+1]-b[i]
    return m
    def lcm(a,b):
    return a*b//gcd(a,b)
    def merge(a,b):
    i=0;j=0
    c=0
    ans=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            ans.append(a[i])
            i+=1
        else:
            ans.append(b[j])
            c+=len(a)-i
            j+=1
    ans+=a[i:]
    ans+=b[j:]
    return ans,c
def mergesort(a):
    if len(a)==1:
        return a,0
    mid=len(a)//2   
    left,left_inversion=mergesort(a[:mid])
    right,right_inversion=mergesort(a[mid:])
    m,c=merge(left,right)
    c+=(left_inversion+right_inversion)
    return m,c
    def is_prime(num):
    if num == 1: return False
    if num == 2: return True
    if num == 3: return True
    if num%2 == 0: return False
    if num%3 == 0: return False
    t = 5
    a = 2
    while t <= int(math.sqrt(num)):
        if num%t == 0: return False
        t += a
        a = 6 - a
    return True
      def ceil(a,b):
    if a%b==0:
        return a//b
    else:
        return (a//b + 1)
def ncr1(n,r):
    s=1
    for i in range(min(n-r,r)):
        s*=(n-i)
        s%=mod
        s*=pow(i+1,mod-2,mod)
        s%=mod
    return s
def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
    if (m == 1) : 
        return 0
    while (a > 1) : 
        q = a // m 
        t = m 
        m = a % m 
        a = t 
        t = y 
        y = x - q * y 
        x = t 
    if (x < 0) : 
        x = x + m0 
    return x 
#///////////////////////////////////////////////////////////////////////////////
    //////////////////
def getsum(e,val,ver,v):
    #print(val,ver)
    if len(e[ver])==0:
        val[ver]=v[ver]
        return val[ver]
    if val[ver]!=-10**9:
        return val[ver]
    else:
        val[ver]=v[ver]
        for i in e[ver]:
            val[i]=getsum(e,val,i,v)
            val[ver]+=val[i]
        return val[ver]    
        def check(e,i,v,c):
    x=v[i]
    for j in e[i]:
        x+=check(e,j,v,c)
    return max(x,-c)
                            for _ in range(int(input())):
    n,xx=map(int,input().split())
    v=[0 ] +  list(map(int,I().split()))
    a=[[] for i in range(n+1)]
    for i in range(n-1):
        x,y=map(int,I().split())
        a[x].append(y)
        a[y].append(x)
    if n==1:
        print(max(-xx,v[1]))
        continue
    q=deque([1])
    e=[[] for i in range(n+1)]
    # val=[-10**9]*(n+1)
    vis=[0]*(n+1)
    vis[1]=1
    while q:
        #print(q)
        k=q.popleft()
        for i in a[k]:
            if vis[i]==0:
                e[k].append(i)
                vis[i]=1
                q.append(i)
                # p[i]=k
    sys.stdout.write(str(check(e,1,v,xx))+'\n')
    