#include <bits/stdc++.h>
#define debug(x) cout << #x << " = " << x << endl
#define REP(i,n) for(Long i = 0; i < (Long)n; i++)
#define pb push_back
using namespace std;
typedef long long Long;
const Long MAX = 1e5;
Long X;
Long A[MAX];
struct Graph {
    vector <Long> adj[MAX];
    bool vis[MAX];
        void clear(Long N = MAX) {
        REP( i , N) {
            adj[i].clear();
            vis[i] = false;
        }
    }
        void addEdge(Long u, Long v) {
        u--;
        v--;
        adj[u].pb(v);
        adj[v].pb(u);
    }
        Long dfs(Long u){
        vis[u] = true;
                Long ans = A[u];
        for(Long v : adj[u]) {
            if(!vis[v]) {
                ans += dfs(v);
            }
        }
                ans = max(ans , -X);
                return ans;
    }
} G;
void test() {
    G.clear();
    Long N;
    cin >> N >> X;
    REP(i , N) {
        cin >> A[i];
    }
        REP(i , N - 1 ) {
        Long u,v;
        cin >> u >> v;
        G.addEdge(u , v);
    }
    cout << G.dfs(0) << endl;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Long T;
    cin >> T;
    REP(t , T) {
        test();
    }
    return 0;
}