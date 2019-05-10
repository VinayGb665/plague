#include<bits/stdc++.h>
#define ll long long int
using namespace std;
ll fun2(ll a[],vector<ll>v[],ll n,ll cur,ll x,ll lol[])
{
    if(lol[cur]==1){return 0;}
    lol[cur]=1;
    if(v[cur].size()==0)
    {
        if(a[cur]*-1>=x)
        {
            return -1*x;
        }
        else{return a[cur];}
    }
    else
    {
        ll ans1=x*-1,ans2=a[cur];
        for(ll i=0;i<v[cur].size();i++)
        {
            ans2+=fun2(a,v,n,v[cur][i],x,lol);
        }
        if(ans1>ans2){return ans1;}
        return ans2;
    }
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        ll n,x,k=0;
        cin>>n>>x;
        ll a[n];
        for(ll i=0;i<n;i++)
        {
            cin>>a[i];
        }
        vector<ll>v[n];
        for(ll i=0;i<n-1;i++)
        {
            ll gg1,gg2;
            cin>>gg1>>gg2;
            gg1--;gg2--;
            v[gg1].push_back(gg2);
            v[gg2].push_back(gg1);
        }
        ll lol[n]={0};
        k=fun2(a,v,n,0,x,lol);
        cout<<k<<endl;
    }
    return 0;
}