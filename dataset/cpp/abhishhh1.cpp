// รђгเ ﻮคภєรђคץ ภค๓คђ //  ןคเ ๒คןคгคภﻮ ๒คlเ // jለi ወለէለ ծi //
#include<bits/stdc++.h>
using namespace std;
#pragma GCC target ("avx2")
#pragma GCC optimization ("O3")
#pragma GCC optimization ("unroll-loops")
#define mod                   1000000007
#define ll                    long long
#define Author                std::ios_base::sync_with_stdio(0);
#define ABHISHEK_SHARMA       cout.tie(0);
#define IIIT_ALLAHABAD        cin.tie(0);
#define all(v)                v.begin(),v.end()
#define pb(a)                 push_back(a)
#define lb(v,t)               lower_bound(all(v),t)-v.begin()
#define ub(v,t)               upper_bound(all(v),t)-v.begin()
ll ans[100010];
vector<ll>tree[100010];
void dfs(ll u,ll p, ll a[], ll k) {
    ans[u]=-k;
    ll temp=a[u];
    for(auto it:tree[u]) {
        if(it!=p) {
            dfs(it,u,a,k);temp=temp+ans[it];
        }
    }
    ans[u]=max(ans[u],temp);
}
void solve(){
    ll n, i, j, k;
    cin>>n>>k;
    ll a[n+1];
    for(i=1; i<=n; i++){
        cin>>a[i];
    }
    for(i=1; i<100010; i++){
        tree[i].clear();
    }
    ll u, v;
    for(i=0; i<n-1; i++){
        cin>>u>>v;
        tree[u].pb(v);tree[v].pb(u);
    }
    dfs(1,0,a,k);
    cout<<ans[1];
}
int main(){
    //Booster
    Author
        ABHISHEK_SHARMA
        IIIT_ALLAHABAD
    //Driver Code here
    ll t=1, i;
    cin>>t;
    for(i=1; i<=t; i++){
        //cout<<"Case #"<<i<<": ";
        solve();
        cout<<"\n";
    }
    return 0;
}