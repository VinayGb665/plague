#include<bits/stdc++.h>
#define int long long
using namespace std;
void dfs(int v,int par,vector<int>adj[],int arr[],int dp[],int x)
{
    dp[v]=arr[v];
    for(int i=0;i<adj[v].size();i++)
    {
        if(adj[v][i]==par)continue;
        dfs(adj[v][i],v,adj,arr,dp,x);
        dp[v]+=dp[adj[v][i]];
    }
    dp[v]=max(dp[v],-1*x);
}
int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--)
    {
        int n,x;
        cin>>n>>x;
        vector<int>adj[n+1];
        int arr[n+1];
        int dp[n+1];
        for(int i=1;i<=n;i++)
        {
            cin>>arr[i];
            dp[i]=0;
        }
        for(int i=1;i<=n-1;i++)
        {
            int u,v;
            cin>>u>>v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        dfs(1,0,adj,arr,dp,x);
        cout<<dp[1]<<endl;
    }
    return 0;
}