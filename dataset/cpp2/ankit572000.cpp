#include <bits/stdc++.h>
using namespace std;
long long ans[100005];
int visit[100005];
long long k;
long long  dfs(vector <int> v[],int i,long long val[])
{
    visit[i]=1;
    long long res=val[i];
    for(int j=0;j<v[i].size();j++)
    {
        if(visit[v[i][j]]==0)
        {
            res+=dfs(v,v[i][j],val);
        }
    }
    ans[i]=res;
    return res;
}
long long dfs1(vector <int> v[],int i,long long val[])
{
    visit[i]=1;
    long long res=val[i];
    long long max1=(-1)*k;
    for(int j=0;j<v[i].size();j++)
    {
        if(visit[v[i][j]]==0)
        {
            res+=dfs1(v,v[i][j],val);
        }
    }
    return max(max1,res);
}
int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        cin>>k;
        vector <int> v[n+1];
        long long val[n+1];
        for(int i=1;i<=n;i++)
            cin>>val[i];
        for(int i=1;i<n;i++)
        {
            int x,y;
            cin>>x>>y;
            v[x].push_back(y);
            v[y].push_back(x);
        }
        long long sum=0;
        for(int i=1;i<=n;i++)
        {
            ans[i]=0;
            visit[i]=0;
        }
        long long x=dfs(v,1,val);
        for(int i=1;i<=n;i++)
             visit[i]=0;
         long long p=dfs1(v,1,val);
         cout<<p<<endl;
    }
    return 0;
}