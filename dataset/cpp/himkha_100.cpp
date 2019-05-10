/*
    Author: @himkha_100
    Himanshu Khandelwal, NITW
*/
#include<bits/stdc++.h>
#define MOD 1000000007
#define INFI 1e15
#define INFIM 1e18
#define ll long long int
#define s(t) scanf("%d",&t)
#define p(t) printf("%d\n",t)
#define pb push_back
#define f(t) for(int i=0;i<t;i++)
#define fi first
#define se second
#define all(t) t.begin(),t.end()
#define ci(t) cin>>t
#define co(t) cout<<t
#define mii map<int,int>
#define pii pair<int,int>
using namespace std;
struct node{
    int val;
    int pos;
};
bool ac(int x,int y)
{
    return x>y;
}
ll a[100001];
vector<int> adj[100001];
ll tot[100001];
int pa[100001];
ll dp[100001][2];
void find(int curr, int par)
{
    pa[curr]=par;
    tot[curr]=a[curr];
    f(adj[curr].size())
    {
        if(adj[curr][i]!=par)
        {
            find(adj[curr][i],curr);
            tot[curr]+=tot[adj[curr][i]];
        }
    }
}
ll x;
ll find1(int curr,int fl)
{
    if(dp[curr][fl]!=-INFIM) return dp[curr][fl];
    if(fl==0)
    {
        return dp[curr][fl]=tot[curr]+x;
    }
    else
    {
        ll ans=0;
        f(adj[curr].size())
        {
            if(adj[curr][i]!=pa[curr])
            {
                ans+=min(find1(adj[curr][i],0),find1(adj[curr][i],1));
            }   
        }
        return dp[curr][fl]=ans;    
    }
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        ll n;
        cin>>n>>x;
        f(100001)
        {
            adj[i].clear();
            dp[i][0]=-INFIM;
            dp[i][1]=-INFIM;
        }
        f(n)
        {
            cin>>a[i+1];
        }
        f(n-1)
        {
            int u,v;
            cin>>u>>v;
            adj[u].pb(v);
            adj[v].pb(u);
        }
        find(1,0);
        ll ans=-INFIM;
        f(n)
        {
            ans=max(ans,max(tot[1]-find1(i+1,0),tot[1]-find1(i+1,1)));
        }
        cout<<ans<<endl;
    }
    return 0;
}