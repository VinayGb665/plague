#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cstring>
typedef long long ll;
using namespace std;
const int nmax = 100006;
vector<int> adj[nmax];
int weight[nmax];
ll solve(int root, int par, ll X)
{
    ll S = weight[root];
        for(int i = 0;i < (int) adj[root].size();++i)
    {
        int nod = adj[root][i];
        if(nod != par)
        {
            S += solve(nod, root, X);
        }
    }
    return max(-X, S);
}
int main()
{
    int t;
        scanf("%d", &t);
    for(int i = 0;i < t;++i)
    {
        int N, X;
        scanf("%d %d", &N, &X);
                for(int j = 1;j <= N;++j)
        {
            scanf("%d", &weight[j]);
            adj[j].clear();
        }
        for(int j = 0;j < N - 1;++j)
        {
            int a, b;
            scanf("%d%d", &a, &b);
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        printf("%lld\n", solve(1, -1, X));
    }
}