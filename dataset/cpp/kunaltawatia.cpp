#include <iostream>
#include <vector>
using namespace std;
#define limit 100005
vector< vector <int> > successor;
vector <long long> price(limit);
long long visited[limit]={};
long long n,x;
long long dfs(int parent){
    visited[parent]=1;
    long long sum=price[parent];
    for( auto child : successor[parent]){
        if(visited[child]) continue;
        sum+=dfs(child);
    }    
    return max(-x,sum);
}   
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int test;
    cin>>test;
    while(test--){
        cin>>n;
        successor.clear();
        successor.resize(n);
        cin>>x;
        for(int i=0;i<n;i++){
            cin>>price[i];
            visited[i]=0;
        }
        int u,v;
        for(int i=0;i<n-1;i++){
            cin>>u>>v;
            u--;v--;
            successor[u].push_back(v);
            successor[v].push_back(u);
        }
        long long ans = dfs(0);
        cout<<ans<<endl;
    }
}