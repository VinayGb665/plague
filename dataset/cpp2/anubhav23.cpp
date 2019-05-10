#include <bits/stdc++.h>
using namespace std;
vector <int> e[100003];
int x,a[100003];
long long sum[100003];
long long dfs(int node,int parent){
    long long tot=0;
    sum[node] = a[node];
    for(int i=0;i<e[node].size();++i){
        if(e[node][i]!=parent){
            tot+=dfs(e[node][i],node);
        }
    }
    for(int i=0;i<e[node].size();++i){
        if(e[node][i]!=parent)
            sum[node]+=sum[e[node][i]];
    }
    //cout<<node<<" "<<sum[node]<<" "<<e[node].size()<<" "<<tot<<endl;
    return max(tot,-sum[node]-x);
}
int main(){
     int t,n,u,v;
     scanf("%d",&t);
     while(t--){
         scanf("%d %d",&n,&x);
         for(int i=1;i<=n;++i){
            scanf("%d",&a[i]);
            e[i].clear();
            sum[i]=0;
         }
         for(int i=1;i<n;++i){
             scanf("%d %d",&u,&v);
             e[u].push_back(v);
             e[v].push_back(u);
         }
         long long ans = dfs(1,-1);
         printf("%lld\n",sum[1]+ans);
     }
    return 0;
}