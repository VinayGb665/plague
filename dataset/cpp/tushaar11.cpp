// @tushaar11
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define PSET(x,y) fixed<<setprecision(y)<<x
#define pb push_back
#define pf push_front
#define mp make_pair
#define pii pair<int,int>
#define pid pair<int,double>
#define vi vector<int>
#define ff first
#define ss second
#define int long long int
#define ull unsigned long long
#define SIZE 200010
#define MOD 1000000007
#define BIG 998244353
#define s(t) scanf("%d",&t)
#define p(t) printf("%d\n",t)
#define mii map<int,int>
#define tc int tcs;cin>>tcs;while(tcs--)
#define set_bit __builtin_popcount
#define MSET(table,i) memset(table, i, sizeof(table))
int toint(const string &s) {stringstream ss; ss << s; int x; ss >> x; return x;}
string tostring ( int number ){stringstream ss; ss<< number; return ss.str();}
vector<vector<int> > adjlist;
vector<pair<int,int> > answer;
int n,x;
int arr[100010];
int mod[100010];
int gcd(int a,int b)
{
    if(b==0) return a;
    return gcd(b,a%b);
}
void input()
{
    for(int i=1;i<=n;i++)
        {
                cin>>arr[i];
        }
    for(int i=1;i<n;i++)
        {
                int a,b;
                cin>>a>>b;
                adjlist[a].pb(b);
                adjlist[b].pb(a);
        }
    }
int get_answer(int node,int g,int p)
{
    int ans=0;
    for(int x=0;x<adjlist[node].size();x++)
    {
        if(adjlist[node][x]!=p)
        ans+=get_answer(adjlist[node][x],g,node);
    }
    ans=max(ans+arr[node],-x);
    return ans;
}
int32_t main()
{
    fast;
    tc{
        cin>>n>>x;
        adjlist.resize(n+1);
        input();
        cout<<get_answer(1,0,-1);
        cout<<endl;
        answer.clear();
        adjlist.clear();
    }
    return 0;
}