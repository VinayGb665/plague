#include <bits/stdc++.h>
using namespace std;
#if DEBUG && !ONLINE_JUDGE
    #include "header.h"
#else
    #define debug(args...)
#endif
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long lli;
typedef long double ld;
#define pb push_back
#define all(x) x.begin(),x.end()
#define SZ(x) (int)(x).size()
#define fi first
#define se second
#define lb lower_bound
#define ub upper_bound
#define rep(i,a,b) for(auto i=(a);i<b;i++)
#define INF (int)1e9
#define EPS 1e-9
#define MOD 1000000007
void preprocess(void) {
    return;
}
vector<vi> adj;
vi ar;
int X;
lli solve(int v, int p) {
    lli fans = 0, ans = 0;
    for(auto x: adj[v]) {
        if(x != p) {
            ans +=  solve(x,v);
        }
    }
    fans = max(-(lli)X, ar[v] + ans);
    return fans;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.precision(20);
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    preprocess();
    int t; cin>>t;
    while(t--) {
        int n; cin>>n>>X;
        adj.clear();
        adj.resize(n+1,vi(0));
        ar.clear();
        ar.resize(n+1);
        rep(i,1,n+1) cin>>ar[i];
        rep(i,0,n-1) {
            int u, v; cin>>u>>v;
            adj[u].pb(v);
            adj[v].pb(u);
        }
        lli ans = solve(1,-1);
        cout<<ans<<endl;
    }
}