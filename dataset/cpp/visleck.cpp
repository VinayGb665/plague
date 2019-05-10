#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair
#define X first
#define Y second
ll A[100005],ans[100005];
ll S[100005],siz[100005];
vector<int>v[100005];
ll x;
ll dfs(int n,int p) {
    bool flag=true;
    ll z=0,m;
    for(int i=0;i<v[n].size();++i) {
        if(v[n][i]!=p) {
            flag=false;
            m=dfs(v[n][i],n);
            if(m<0) z+=m;
            S[n]+=S[v[n][i]];
            siz[n]+=siz[v[n][i]];
        }
    }
    siz[n]++;
    S[n]+=A[n];
    ans[n]=S[n]+x;
    if(ans[n]<z) return ans[n];
    else return z;
}
int main() {
    int t,a,b;
    ll n,an;
    cin>>t;
    while(t--) {
        cin>>n>>x;
        for(int i=1;i<=n;++i) {
            cin>>A[i];v[i].clear();S[i]=0;siz[i]=0;
        }
        for(int i=1;i<n;++i) {
            cin>>a>>b;
            v[a].pb(b);
            v[b].pb(a);
        }
        an=dfs(1,-1);
        cout<<S[1]-an<<"\n";
    }
    return 0;
}