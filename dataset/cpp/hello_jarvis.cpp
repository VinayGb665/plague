#include<bits/stdc++.h>
#define ll          long long
#define pb          push_back
#define vi          vector<ll int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define hell        1000000007
#define lbnd        lower_bound
#define ubnd        upper_bound
#define sll            set<ll int>
#define msll        multiset<ll int>
#define io    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;
ll t,n,x,val[300005];
vi a[300005];
ll dp[300005];
bool vis[300005];
ll go(ll node){
    if(a[node].empty()){
        return dp[node]=max(-x,val[node]);
    }
    if(dp[node]!=-1) return dp[node];
    vis[node]=1;
    ll tmp=val[node];
    for(auto i:a[node]){
        if(!vis[i]) tmp+=(go(i));
    }
    return dp[node]=max(-x,tmp);
}
int main()
{
    io
    ll i,j;
    cin>>t;
    while(t--){
        memset(dp,-1,sizeof dp);
        memset(vis,0,sizeof vis);
        cin>>n>>x;
        for(i=1;i<=n;i++){
            cin>>val[i];
            a[i].clear();
        }
        for(i=1;i<=n-1;i++){
            ll u,v;
            cin>>u>>v;
            a[u].pb(v);
            a[v].pb(u);
        }
        cout<<go(1)<<"\n";
    }
    return 0;
}