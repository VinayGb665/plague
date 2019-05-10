#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define FASTIO std::ios::sync_with_stdio(false);
vector<int>g[100005];
int val[100005]={0};
//vector<pair<long long int, lo
vector<long long int> a, b;
vector <pair<long long int, long long int >> res;
bool vis[100005];
long long int  dfs(long long int s, long long int count)
{
    long long int x=a[s];
    if(vis[s]) return 0;
    vis[s]=true;
    for(int i=0;i<g[s].size();i++){
        if(!vis[g[s][i]]){
        x+=dfs(g[s][i], count);
        }
    }
    if(x<-1*count){
        x=-1*count;
    }
    else val[s]=x;
    return x;
}
int main(){
    FASTIO
    int t;
    cin>>t;
    while(t--){
        long long int n,x, y, z,total;
                cin>>n>>x;
        for(int i=0;i<n;i++){
            cin>>y;
            a.push_back(y);
        }
        memset(vis, false, sizeof vis);
        for(int i=0;i<n-1;i++){
            cin>>z>>y;
            g[y-1].push_back(z-1);
            g[z-1].push_back(y-1);
        }
                        total=dfs(0,x);
        //cout<<total<<endl;
        for(int i=0;i<n;i++){
            g[i].clear();
            vis[i]=false;
        }
        a.clear();
        res.clear();
        cout<<total<<endl;
    }
}