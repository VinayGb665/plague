#include <bits/stdc++.h> 
using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<ll> vl;
typedef pair<ll,ll> pll;
#define MOD 1000000007
#define INF 1000000000
#define mp make_pair
#define pb push_back
#define ss second
#define ff first
#define endl '\n'
#define pl cout<<endl;
ll maxi=LLONG_MIN;
ll mini=LLONG_MAX;
void fast() { ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL); }
ll t,i,j,k,n,x,temp,flag,ans,m;
vl ad[100005];
vl f(100005,0),v(100005,0);
vl a(100005);
void dfs(int u)
{
    v[u]=1;
    f[u]=a[u];
    for(int i=0;i<ad[u].size();i++)
    {
        if(!v[ad[u][i]])
        {
            dfs(ad[u][i]);
            f[u]+=f[ad[u][i]];
        }
            }
    f[u]=max(f[u],-1*x);
}
void dfs2(int u)
{
    v[u]=1;
    for(int i=0;i<ad[u].size();i++)
    {
        if(!v[ad[u][i]])
        {
            dfs2(ad[u][i]);
            f[u]+=f[ad[u][i]];
        }
    }
}
int main() {
    #ifndef ONLINE_JUDGE
    freopen("C:\\Users\\AJAY KRISSHAN N K\\Desktop\\Ajay\\Codes\\in.txt", "r", 
        stdin);
    freopen("C:\\Users\\AJAY KRISSHAN N K\\Desktop\\Ajay\\Codes\\out.txt", "w", 
        stdout);
    #endif
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n>>x;
                for(int i=1;i<=n;i++)
        {
            cin>>a[i];
            v[i]=0;
            ad[i].clear();
        }
        for(int i=1;i<=n-1;i++)
        {
            int c,d;
            cin>>c>>d;
            ad[c].pb(d);
            ad[d].pb(c);
        }
        dfs(1);
        cout<<f[1]<<"\n";
    }
    return 0;
}   