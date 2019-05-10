#include <bits/stdc++.h>
using namespace std;
#define maxn 100001
#define ll long long
vector<int> adj[maxn];
int vis[maxn],n;
ll a[maxn],ans[maxn],x;
void dfs(int v){
    ans[v]=a[v];
    vis[v]=1;
    for(int u:adj[v]){
        if(vis[u]) continue;
        dfs(u);
        ans[v]+=ans[u];
    }
    ans[v]=max(ans[v],-x);
    return;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);cout.tie(0);
    int t,u,v;
    cin>>t;
    while(t--){
        cin>>n>>x;
        for(int i=1;i<=n;i++){
            cin>>a[i];
            adj[i].clear();
            vis[i]=0;
        }
        for(int i=1;i<n;i++){
            cin>>u>>v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        dfs(1);
        cout<<ans[1]<<"\n";
    }
    return 0;
}