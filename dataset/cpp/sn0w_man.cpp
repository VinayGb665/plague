/* BISMILLAHIR RAHMANIR RAHIM */
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll inf = 1e14;
const int mxn = 100005;
ll n, X, a[mxn];
vector<int> G[mxn];
ll ff[mxn];
void dfs( int u = 1, int p = 0 ) {
    ll& ret = ff[u];
    ret = a[u];
    for(auto& v : G[u]) {
        if( v == p ) continue;
        dfs( v, u );
        ret += max( -X, ff[v] );
    }
}
int main() {
    int cases;
    scanf("%d", &cases);
    while( cases-- ) {
        scanf("%lld %lld", &n, &X);
        for(int i = 1; i <= n; i++) {
            scanf("%lld", a + i);
            G[i].clear();
        }
        for(int i = 1, u, v; i < n; i++) {
            scanf("%d %d", &u, &v);
            G[u].push_back(v);
            G[v].push_back(u);
        }
        for(int i = 1; i <= n; i++) {
            ff[i] = -inf;
        }
        dfs();
        printf("%lld\n", ff[1]);
    }
    return 0;
}