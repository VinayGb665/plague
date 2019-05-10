#include<bits/stdc++.h>
using namespace std; 
#define int long long
#define pb push_back
#define mp make_pair
#define debugg(x) cout<<"#"<<x<<endl;
const int mi=1e15; 
int getcost(int node,int p,vector<int>adj[],int arr[],int x){
    int ans=-x;
    int ans1=arr[node];
    bool f=true; 
    for(auto u:adj[node]){
        if(u==p) continue;
        ans1+=getcost(u,node,adj,arr,x); 
    }
    return max(ans,ans1);
}
signed main(){
    int t; cin>>t; 
    while(t--){
        int n,x; cin>>n>>x; 
        int arr[n+1];
        for(int i=1;i<=n;i++) cin>>arr[i];
        vector<int>adj[n+1];
        for(int i=1;i<n;i++){
            int u,v ;cin>>u>>v; 
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        int ans=getcost(1,-1,adj,arr,x);
        cout<<ans<<endl;
    }
}