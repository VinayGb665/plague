#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
   #define IOS ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
ll mod=1e9+7;
ll power(ll a,ll b)
{
    if(b==0) return 1;
    else if(b%2==0)
        return power(a*a%mod,b/2);
    else return (a*power(a*a%mod,b/2))%mod;
}
//const ll mod =998244353;
const ll maxn=100001;
ll a[maxn],X;
ll sum[maxn];
bool visited[maxn];
bool children[maxn];
vector <vector < ll >> root(maxn);
vector< vector< ll>> childrenren(maxn);
void dfs()
{
    queue< ll > beta;    beta.push(0);     visited[0]=true;    while(!beta.empty
        ())    {
        ll temp=beta.front();
        beta.pop();
        for(auto x: root[temp])         {
            if(!visited[x])            {
                visited[x]=1;                childrenren[temp].push_back(x);
                                             beta.push(x);           
                 children[temp]=1;            }    }    }
    }
ll sumtree(ll h)
{
    if(children[h]==0)         {sum[h]=a[h];             return sum[h];         
        }
    else
    {         ll tempsum=0;         for(auto k: childrenren[h])         {       
              tempsum+=sumtree(k);
        }
        sum[h]=tempsum+a[h];         return sum[h];
    }
}
ll maxi(ll x)
{
    if(children[x]==0)
    {
        if(sum[x]<0&&abs(sum[x])>X)            return abs(sum[x])-X;         
            else 
            return 0;
    }
    ll tempsum=0;     for(auto k:childrenren[x])     {         tempsum+=maxi(k); 
            }     ll p=0,s=0;     return max(max(-sum[x]-X,max(tempsum,p)),s);
}
int main()
{
      #ifndef ONLINE_JUDGE
    // for getting input from input.txt
    freopen("input.txt", "r", stdin);
    // for writing output to output.txt
    freopen("output.txt", "w", stdout);
#endif
    IOS
    ll t;
    cin>>t;
    while(t--)
    {        
                        ll n;
        memset(children,0,sizeof(children));
        memset(visited,0,sizeof(visited));
        memset(sum,0,sizeof(sum));
        cin>>n>>X;
        ll tot=0;
                        for(ll i=0;i<n;i++)
        {
            cin>>a[i];
            tot+=a[i];
                    }
        if(n==1)
        {
            cout<<max(a[0],-X)<<endl;
            continue;
        }
        for(ll i=0;i<n-1;i++)
        {    
            ll u,v;
            cin>>u>>v;
            u--;
            v--;
            root[u].push_back(v);
            root[v].push_back(u);
        }
        dfs();
        sum[0]=sumtree(0);
        ll ans=tot+maxi(0);
        cout<<ans<<endl;
        for(ll i=0;i<=n;i++)
        {
            root[i].clear();
            childrenren[i].clear();
        }
    }
    }
     